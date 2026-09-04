// SPDX-FileCopyrightText: 2026 Proper Linux contributors
// SPDX-License-Identifier: GPL-2.0-or-later

// Plasma records this update by filename. Change only the exact former Proper
// Status Shade panel signature: auto-hide consumes the first edge click while
// revealing its panel, whereas the promised interaction is one click. Keeping
// the old panel full-width would leave a blank strip, so use a deterministic
// centred handle. A panel the user changed is left alone.
panels().forEach(panel => {
    const shades = panel.widgets("com.properlinux.statusshade")
    const isLegacyProperShade = panel.location === "top"
        && panel.alignment === "center"
        && panel.height === 8
        && panel.lengthMode === "fill"
        && panel.hiding === "autohide"
        && panel.floating === false
        && shades.length === 1

    if (isLegacyProperShade) {
        panel.lengthMode = "custom"
        panel.length = 112
        panel.minimumLength = 112
        panel.maximumLength = 112
        panel.hiding = "none"
    }
})
