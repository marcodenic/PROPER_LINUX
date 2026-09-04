// SPDX-FileCopyrightText: 2026 Proper Linux contributors
// SPDX-License-Identifier: GPL-2.0-or-later

// Remove only Proper's two former single-applet top-edge panel signatures. The
// live panel can be thicker than the requested eight pixels because Plasma
// clamps it to the compact applet's minimum size, so applet ownership is the
// stable signature. A panel containing anything else is a user layout and is
// left alone.
let shelf = null
panels().forEach(panel => {
    if (panel.location === "bottom"
        && panel.alignment === "center"
        && panel.widgets("org.kde.plasma.icontasks").length > 0
        && panel.widgets("org.kde.plasma.systemtray").length > 0
        && panel.widgets("org.kde.plasma.digitalclock").length > 0) {
        shelf = panel
    }
})

if (shelf !== null) {
    let shelfShade = shelf.widgets("com.properlinux.statusshade")[0]
    panels().forEach(panel => {
        const shades = panel.widgets("com.properlinux.statusshade")
        const legacyFillPanel = panel.lengthMode === "fill" && panel.hiding === "autohide"
        const legacyHandlePanel = panel.lengthMode === "custom"
            && panel.minimumLength === 112
            && panel.maximumLength === 112
            && panel.hiding === "none"
        const isLegacyProperShade = panel.location === "top"
            && panel.alignment === "center"
            && panel.floating === false
            && panel.widgets().length === 1
            && shades.length === 1
            && (legacyFillPanel || legacyHandlePanel)

        if (isLegacyProperShade) {
            if (!shelfShade) {
                shelfShade = shelf.addWidget("com.properlinux.statusshade")
                shelfShade.globalShortcut = shades[0].globalShortcut || "Meta+S"
            }
            panel.remove()
        }
    })
}
