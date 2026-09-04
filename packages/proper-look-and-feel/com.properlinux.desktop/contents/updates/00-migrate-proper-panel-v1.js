// SPDX-FileCopyrightText: 2026 Proper Linux contributors
// SPDX-License-Identifier: GPL-2.0-or-later

// Plasma records this update by filename. Only the exact earlier Proper shelf
// signature is changed; a removed, rearranged, or resized panel is a user
// choice and is left alone.
panels().forEach(panel => {
    const tasks = panel.widgets("org.kde.plasma.icontasks")
    const trays = panel.widgets("org.kde.plasma.systemtray")
    const isLegacyProperShelf = panel.maximumLength === 720
        && panel.height === 56
        && panel.lengthMode === "fit"
        && tasks.length === 1
        && trays.length === 1

    if (!isLegacyProperShelf)
        return

    if (panel.minimumLength === 320) {
        panel.minimumLength = 560

        if (panel.widgets("org.kde.plasma.panelspacer").length === 0) {
            const tray = trays[0]
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
    }

    panel.widgets("org.kde.plasma.digitalclock").forEach(clock => {
        clock.currentConfigGroup = ["Configuration"]
        const legacyFormat = clock.readConfig("Appearance.dateFormat", "")
        const legacyCustom = clock.readConfig("Appearance.customDateFormat", "")

        clock.currentConfigGroup = ["Configuration", "Appearance"]
        const currentFormat = clock.readConfig("dateFormat", "")
        if (currentFormat === "" && legacyFormat === "custom" && legacyCustom === "MMMM d") {
            clock.writeConfig("showSeconds", false)
            clock.writeConfig("showDate", true)
            clock.writeConfig("dateFormat", "custom")
            clock.writeConfig("customDateFormat", "MMMM d")
        }
    })
})
