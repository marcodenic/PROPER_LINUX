// SPDX-FileCopyrightText: 2026 Proper Linux contributors
// SPDX-License-Identifier: GPL-2.0-or-later

// Move clocks that still use Plasma's stock numeric date to Proper's approved
// month-and-day form. Leave an existing custom format alone: it is a user
// choice, not an old Proper default.
panels().forEach(panel => panel.widgets("org.kde.plasma.digitalclock").forEach(clock => {
    clock.currentConfigGroup = ["Appearance"]
    const format = clock.readConfig("dateFormat", "shortDate")
    const customFormat = clock.readConfig("customDateFormat", "")
    if (format === "shortDate" && customFormat === "") {
        clock.writeConfig("dateFormat", "custom")
        clock.writeConfig("customDateFormat", "MMMM d")
    }
}))
