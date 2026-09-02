// SPDX-License-Identifier: GPL-3.0-or-later
// Proper Linux keeps KWin's ordinary floating model until the user explicitly
// arranges a workspace. Arranged windows are managed by KWin's native tiles so
// dragging a shared edge resizes every window on that edge. The exact original
// floating geometry is retained so the operation remains reversible.

const INNER_GAP = Math.max(0, Number(readConfig("InnerGap", 12)));
const TILE_HORIZONTAL = 1;
const TILE_VERTICAL = 2;

let activeSnapshot = null;
let lastLayout = "halves";

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

function makeRect(x, y, width, height) {
    return {
        x: Math.round(x),
        y: Math.round(y),
        width: Math.max(1, Math.round(width)),
        height: Math.max(1, Math.round(height))
    };
}

function childTiles(tile) {
    return tile && tile.tiles ? Array.from(tile.tiles) : [];
}

function clearTileChildren(tile) {
    let children = childTiles(tile);
    while (children.length > 0) {
        children[children.length - 1].remove();
        children = childTiles(tile);
    }
}

function resizeLinearTiles(container, tiles, direction) {
    const area = copyGeometry(container.relativeGeometry);
    for (let index = 0; index < tiles.length - 1; index++) {
        const geometry = copyGeometry(tiles[index].relativeGeometry);
        if (direction === TILE_HORIZONTAL) {
            const boundary = area.x + area.width * (index + 1) / tiles.length;
            geometry.width = boundary - geometry.x;
        } else {
            const boundary = area.y + area.height * (index + 1) / tiles.length;
            geometry.height = boundary - geometry.y;
        }
        tiles[index].relativeGeometry = geometry;
    }
}

function makeLinearTiles(container, direction, count) {
    if (count < 1) {
        return [];
    }

    clearTileChildren(container);
    container.split(direction);
    let tiles = childTiles(container);

    if (count === 1) {
        tiles[tiles.length - 1].remove();
        return childTiles(container);
    }

    while (tiles.length < count) {
        tiles[tiles.length - 1].split(direction);
        tiles = childTiles(container);
    }
    resizeLinearTiles(container, tiles, direction);
    return tiles;
}

function makeGridTiles(root, count) {
    if (count <= 2) {
        return makeLinearTiles(root, TILE_HORIZONTAL, count);
    }

    const columnCount = Math.ceil(Math.sqrt(count));
    const rowCount = Math.ceil(count / columnCount);
    const rows = makeLinearTiles(root, TILE_VERTICAL, rowCount);
    let result = [];
    for (let row = 0; row < rows.length; row++) {
        result = result.concat(makeLinearTiles(rows[row], TILE_HORIZONTAL, columnCount));
    }
    return result.slice(0, count);
}

function makeStackTiles(root, count, primaryRatio) {
    if (count === 1) {
        return makeLinearTiles(root, TILE_HORIZONTAL, 1);
    }
    if (count > 4) {
        return makeGridTiles(root, count);
    }

    const columns = makeLinearTiles(root, TILE_HORIZONTAL, 2);
    const leftGeometry = copyGeometry(columns[0].relativeGeometry);
    leftGeometry.width = root.relativeGeometry.width * primaryRatio;
    columns[0].relativeGeometry = leftGeometry;

    if (count === 2) {
        return columns;
    }
    return [columns[0]].concat(makeLinearTiles(columns[1], TILE_VERTICAL, count - 1));
}

function nativeTilesFor(layout, root, count) {
    clearTileChildren(root);
    root.padding = INNER_GAP;

    if (layout === "columns" && count <= 3) {
        return makeLinearTiles(root, TILE_HORIZONTAL, count);
    }
    if (layout === "grid") {
        return makeGridTiles(root, count);
    }
    if (layout === "primary") {
        return makeStackTiles(root, count, 2 / 3);
    }
    return makeStackTiles(root, count, 1 / 2);
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

function detachFromTiles(entries) {
    for (let index = 0; index < entries.length; index++) {
        const tile = entries[index].window.tile;
        if (tile) {
            tile.unmanage(entries[index].window);
        }
    }
}

function restoreSnapshot() {
    if (!activeSnapshot) {
        return false;
    }
    const entries = liveSnapshotEntries();
    detachFromTiles(entries);
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

    const root = workspace.rootTile(context.output, context.desktop);
    if (!root) {
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

    if (entries.length === 0) {
        activeSnapshot = null;
        return;
    }

    detachFromTiles(entries);
    const tiles = nativeTilesFor(layout, root, entries.length);
    for (let i = 0; i < entries.length; i++) {
        entries[i].window.setMaximize(false, false);
        tiles[i].manage(entries[i].window);
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
    "Meta+W",
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
