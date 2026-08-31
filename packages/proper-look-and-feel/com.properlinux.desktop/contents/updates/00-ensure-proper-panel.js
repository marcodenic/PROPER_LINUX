// SPDX-FileCopyrightText: 2026 Proper Linux contributors
// SPDX-License-Identifier: GPL-2.0-or-later

// A ShellPackage has its own applet layout store even when its visual files
// fall back to org.kde.plasma.desktop. Seed the upstream Fedora/KDE panel only
// when that new store contains no panel. Plasma records this update as
// performed, so a panel removed intentionally later stays removed.
if (panels().length === 0) {
    loadTemplate("org.kde.plasma.desktop.defaultPanel")
}
