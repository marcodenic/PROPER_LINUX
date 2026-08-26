// Proper Linux retained dropdown terminal. KWin owns visibility; Ghostty owns
// the shell process and contents. The class/app-id is intentionally stable.
function isDropdown(window) {
    return window.resourceClass === "ProperDropdown" ||
        window.resourceName === "ProperDropdown" ||
        window.desktopFileName === "proper-terminal-dropdown" ||
        window.caption === "Proper Terminal";
}

function dropdownWindow() {
    // Plasma 6 exposes managed windows through windowList(); retain the
    // clientList fallback for older KWin builds used by development images.
    const windows = typeof workspace.windowList === "function"
        ? workspace.windowList()
        : workspace.clientList();
    for (let i = 0; i < windows.length; i++) {
        if (isDropdown(windows[i])) {
            return windows[i];
        }
    }
    return null;
}

function toggleDropdown() {
    const window = dropdownWindow();
    if (!window) {
        return;
    }
    window.minimized = !window.minimized;
    if (!window.minimized) {
        workspace.activeWindow = window;
    }
}

registerShortcut("ProperDropdownToggle", "Show or hide Proper Terminal", "Meta+J", toggleDropdown);
