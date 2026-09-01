// SPDX-License-Identifier: GPL-3.0-or-later
// Proper Linux keeps KWin's ordinary floating model. This script only moves
// normal, visible windows on the current workspace and output, and retains the
// exact pre-arrangement geometry so the operation is reversible.

const OUTER_GAP = Math.max(0, Number(readConfig("OuterGap", 14)));
const INNER_GAP = Math.max(0, Number(readConfig("InnerGap", 12)));

let activeSnapshot = null;
let lastLayout = "primary";

function windowsInStackingOrder() {
    if (workspace.stackingOrder) {
        return Array.from(workspace.stackingOrder).reverse();
    }
    if (typeof workspace.windowList === "function") {
        return workspace.windowList().slice().reverse();
    }
    return workspace.clientList().slice().reverse();
}

function isOnDesktop(window, desktop) {
    if (window.onAllDesktops || !window.desktops || window.desktops.length === 0) {
        return true;
    }
    for (let i = 0; i < window.desktops.length; i++) {
        if (window.desktops[i] === desktop || window.desktops[i].id === desktop.id) {
            return true;
        }
    }
    return false;
}

function isOnActivity(window) {
    if (!window.activities || window.activities.length === 0) {
        return true;
    }
    return window.activities.indexOf(workspace.currentActivity) !== -1;
}

function isEligible(window, output, desktop) {
    return Boolean(window && window.normalWindow && !window.dialog &&
        !window.specialWindow && !window.fullScreen && !window.minimized &&
        !window.skipSwitcher && window.moveable && window.resizeable &&
        window.output === output && isOnDesktop(window, desktop) &&
        isOnActivity(window));
}

function currentContext() {
    const active = workspace.activeWindow;
    const output = active && active.output ? active.output : workspace.activeScreen;
    if (!output) {
        return null;
    }
    const desktop = typeof workspace.currentDesktopForScreen === "function"
        ? workspace.currentDesktopForScreen(output)
        : workspace.currentDesktop;
    return { output, desktop };
}

function contextKey(context) {
    return context.output.name + "::" + context.desktop.id + "::" + workspace.currentActivity;
}

function eligibleWindows(context) {
    const result = windowsInStackingOrder().filter(function(window) {
        return isEligible(window, context.output, context.desktop);
    });
    const active = workspace.activeWindow;
    const activeIndex = result.indexOf(active);
    if (activeIndex > 0) {
        result.splice(activeIndex, 1);
        result.unshift(active);
    }
    return result;
}

function copyGeometry(geometry) {
    return {
        x: Number(geometry.x),
        y: Number(geometry.y),
        width: Number(geometry.width),
        height: Number(geometry.height)
    };
}

function approximatelyEqual(left, right) {
    return Math.abs(left.x - right.x) <= 1 &&
        Math.abs(left.y - right.y) <= 1 &&
        Math.abs(left.width - right.width) <= 1 &&
        Math.abs(left.height - right.height) <= 1;
}

function usableArea(context) {
    const area = workspace.clientArea(KWin.MaximizeArea, context.output, context.desktop);
    return {
        x: Math.round(area.x + OUTER_GAP),
        y: Math.round(area.y + OUTER_GAP),
        width: Math.max(1, Math.round(area.width - (2 * OUTER_GAP))),
        height: Math.max(1, Math.round(area.height - (2 * OUTER_GAP)))
    };
}

function makeRect(x, y, width, height) {
    return {
        x: Math.round(x),
        y: Math.round(y),
        width: Math.max(1, Math.round(width)),
        height: Math.max(1, Math.round(height))
    };
}

function splitRows(x, y, width, height, count) {
    const result = [];
    const rowHeight = (height - (INNER_GAP * (count - 1))) / count;
    for (let row = 0; row < count; row++) {
        result.push(makeRect(x, y + row * (rowHeight + INNER_GAP), width, rowHeight));
    }
    return result;
}

function gridLayout(area, count) {
    if (count === 1) {
        return [makeRect(area.x, area.y, area.width, area.height)];
    }
    const columns = count === 2 ? 2 : Math.ceil(Math.sqrt(count));
    const rows = Math.ceil(count / columns);
    const cellWidth = (area.width - (INNER_GAP * (columns - 1))) / columns;
    const cellHeight = (area.height - (INNER_GAP * (rows - 1))) / rows;
    const result = [];
    for (let index = 0; index < count; index++) {
        const row = Math.floor(index / columns);
        const column = index % columns;
        result.push(makeRect(
            area.x + column * (cellWidth + INNER_GAP),
            area.y + row * (cellHeight + INNER_GAP),
            cellWidth,
            cellHeight
        ));
    }
    return result;
}

function halvesLayout(area, count) {
    if (count <= 2) {
        return gridLayout(area, count);
    }
    if (count > 4) {
        return gridLayout(area, count);
    }
    const columnWidth = (area.width - INNER_GAP) / 2;
    const result = [makeRect(area.x, area.y, columnWidth, area.height)];
    return result.concat(splitRows(
        area.x + columnWidth + INNER_GAP,
        area.y,
        columnWidth,
        area.height,
        count - 1
    ));
}

function primaryLayout(area, count) {
    if (count === 1) {
        return gridLayout(area, count);
    }
    if (count > 4) {
        return gridLayout(area, count);
    }
    const primaryWidth = Math.round((area.width - INNER_GAP) * 2 / 3);
    const secondaryWidth = area.width - INNER_GAP - primaryWidth;
    const result = [makeRect(area.x, area.y, primaryWidth, area.height)];
    return result.concat(splitRows(
        area.x + primaryWidth + INNER_GAP,
        area.y,
        secondaryWidth,
        area.height,
        count - 1
    ));
}

function columnsLayout(area, count) {
    if (count > 3) {
        return gridLayout(area, count);
    }
    const width = (area.width - (INNER_GAP * (count - 1))) / count;
    const result = [];
    for (let index = 0; index < count; index++) {
        result.push(makeRect(area.x + index * (width + INNER_GAP), area.y, width, area.height));
    }
    return result;
}

function geometriesFor(layout, area, count) {
    if (layout === "halves") {
        return halvesLayout(area, count);
    }
    if (layout === "columns") {
        return columnsLayout(area, count);
    }
    if (layout === "grid") {
        return gridLayout(area, count);
    }
    return primaryLayout(area, count);
}

function captureSnapshot(context, windows) {
    const maximizeArea = workspace.clientArea(KWin.MaximizeArea, context.output, context.desktop);
    return {
        key: contextKey(context),
        context,
        entries: windows.map(function(window) {
            return {
                window,
                geometry: copyGeometry(window.frameGeometry),
                maximized: approximatelyEqual(window.frameGeometry, maximizeArea)
            };
        })
    };
}

function liveSnapshotEntries() {
    if (!activeSnapshot) {
        return [];
    }
    const currentWindows = windowsInStackingOrder();
    return activeSnapshot.entries.filter(function(entry) {
        return currentWindows.indexOf(entry.window) !== -1;
    });
}

function restoreSnapshot() {
    if (!activeSnapshot) {
        return false;
    }
    const entries = liveSnapshotEntries();
    for (let i = 0; i < entries.length; i++) {
        const entry = entries[i];
        entry.window.setMaximize(false, false);
        entry.window.frameGeometry = makeRect(
            entry.geometry.x,
            entry.geometry.y,
            entry.geometry.width,
            entry.geometry.height
        );
        if (entry.maximized) {
            entry.window.setMaximize(true, true);
        }
    }
    activeSnapshot = null;
    return true;
}

function applyLayout(layout) {
    const context = currentContext();
    if (!context) {
        return;
    }

    if (activeSnapshot && activeSnapshot.key !== contextKey(context)) {
        restoreSnapshot();
    }

    let entries;
    if (activeSnapshot) {
        entries = liveSnapshotEntries();
    } else {
        const windows = eligibleWindows(context);
        if (windows.length === 0) {
            return;
        }
        activeSnapshot = captureSnapshot(context, windows);
        entries = activeSnapshot.entries;
    }

    const geometries = geometriesFor(layout, usableArea(context), entries.length);
    for (let i = 0; i < entries.length; i++) {
        entries[i].window.setMaximize(false, false);
        entries[i].window.frameGeometry = geometries[i];
    }
    lastLayout = layout;
}

function toggleLastLayout() {
    const context = currentContext();
    if (activeSnapshot && context && activeSnapshot.key === contextKey(context)) {
        restoreSnapshot();
    } else {
        applyLayout(lastLayout);
    }
}

registerShortcut(
    "ProperArrangeWorkspace",
    "Arrange or restore the current workspace",
    "Meta+Z",
    toggleLastLayout
);
registerShortcut(
    "ProperArrangeWorkspacePrimary",
    "Arrange workspace with a two-thirds primary window",
    "",
    function() { applyLayout("primary"); }
);
registerShortcut(
    "ProperArrangeWorkspaceHalves",
    "Arrange workspace in balanced halves",
    "",
    function() { applyLayout("halves"); }
);
registerShortcut(
    "ProperArrangeWorkspaceColumns",
    "Arrange workspace in columns",
    "",
    function() { applyLayout("columns"); }
);
registerShortcut(
    "ProperArrangeWorkspaceGrid",
    "Arrange workspace in a balanced grid",
    "",
    function() { applyLayout("grid"); }
);
registerShortcut(
    "ProperRestoreWorkspace",
    "Restore the captured floating workspace",
    "",
    restoreSnapshot
);
