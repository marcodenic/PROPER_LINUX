// SPDX-FileCopyrightText: 2026 Proper Linux contributors
// SPDX-License-Identifier: GPL-2.0-or-later

// Expand only the exact legacy Proper shelf. A user-selected minimum or a
// structurally different panel is their choice and remains untouched.
panels().forEach(panel => {
    const isLegacyProperShelf = panel.minimumLength === 320
        && panel.maximumLength === 720
        && panel.height === 56
        && panel.lengthMode === "fit"
        && panel.widgets("org.kde.plasma.icontasks").length === 1
        && panel.widgets("org.kde.plasma.systemtray").length === 1

    if (!isLegacyProperShelf)
        return

    panel.minimumLength = 560

    if (panel.widgets("org.kde.plasma.panelspacer").length === 0) {
        const tray = panel.widgets("org.kde.plasma.systemtray")[0]
        // Supplying the tray's position inserts the spacer immediately before
        // it instead of appending it after the clock.
        const spacer = panel.addWidget(
            "org.kde.plasma.panelspacer",
            tray.geometry.x,
            tray.geometry.y,
            86,
            1
        )
        spacer.currentConfigGroup = ["General"]
        spacer.writeConfig("expanding", false)
        spacer.writeConfig("length", 86)
    }
})
