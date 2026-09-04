// SPDX-FileCopyrightText: 2026 Proper Linux contributors
// SPDX-License-Identifier: GPL-2.0-or-later

// Plasma runs the active Global Theme's desktop layout only when it creates a
// profile. This is the one authoritative Proper first-profile definition;
// later user edits remain in the user's Plasma configuration.
const panel = new Panel("org.kde.panel")
panel.location = "bottom"
panel.alignment = "center"
panel.height = 56
panel.lengthMode = "fit"
panel.minimumLength = 560
panel.maximumLength = 720
panel.hiding = "none"
panel.floating = true
panel.opacity = "adaptive"

const tasks = panel.addWidget("org.kde.plasma.icontasks")
tasks.currentConfigGroup = ["General"]
tasks.writeConfig("launchers", "applications:vicinae.desktop,applications:org.kde.dolphin.desktop,applications:com.mitchellh.ghostty.desktop")
tasks.writeConfig("showOnlyCurrentDesktop", false)
tasks.writeConfig("showOnlyCurrentActivity", false)
tasks.writeConfig("showToolTips", true)

const spacer = panel.addWidget("org.kde.plasma.panelspacer")
spacer.currentConfigGroup = ["General"]
spacer.writeConfig("expanding", false)
spacer.writeConfig("length", 86)

panel.addWidget("org.kde.plasma.systemtray")
panel.addWidget("org.kde.plasma.showdesktop")

const commandCentre = panel.addWidget("com.properlinux.statusshade")
commandCentre.globalShortcut = "Meta+S"

const clock = panel.addWidget("org.kde.plasma.digitalclock")
clock.currentConfigGroup = ["Appearance"]
clock.writeConfig("showSeconds", false)
clock.writeConfig("showDate", true)
clock.writeConfig("dateFormat", "custom")
clock.writeConfig("customDateFormat", "MMMM d")
