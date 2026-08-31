// SPDX-FileCopyrightText: 2026 Proper Linux contributors
// SPDX-License-Identifier: GPL-2.0-or-later

// A ShellPackage has its own applet layout store even when its visual files
// fall back to org.kde.plasma.desktop. Seed Proper's small panel only when that
// new store contains no panel. Plasma records this update as performed, so a
// panel removed intentionally later stays removed.
if (panels().length === 0) {
    const panel = new Panel("org.kde.panel")
    panel.location = "bottom"
    panel.alignment = "center"
    panel.height = 56
    panel.lengthMode = "fit"
    panel.minimumLength = 320
    panel.maximumLength = 720
    panel.hiding = "normal"
    panel.floating = true

    const tasks = panel.addWidget("org.kde.plasma.icontasks")
    tasks.currentConfigGroup = ["General"]
    tasks.writeConfig("launchers", "applications:vicinae.desktop,applications:org.kde.dolphin.desktop,applications:proper-terminal.desktop")
    tasks.writeConfig("showOnlyCurrentDesktop", false)
    tasks.writeConfig("showOnlyCurrentActivity", false)

    panel.addWidget("org.kde.plasma.systemtray")
    panel.addWidget("org.kde.plasma.showdesktop")
    panel.addWidget("org.kde.plasma.digitalclock")
}
