# Proper status artwork

Original vector paths drawn for Proper Linux, 5 September 2026, GPL-3.0-or-later.
No external artwork is copied. The owning look-and-feel RPM installs the small
22-unit glyph set in Proper and Proper Dark, with palette-aware SVG classes and
Breeze fallback for all unmodified states. Symbolic aliases share the same art.

KDE's Plasma 6 theme reference directs tray icons to the icon theme, not the
legacy Plasma Style icons directory:
https://develop.kde.org/docs/plasma/theme/theme-elements/

Reviewed against Fedora 44 plasma-workspace 6.7.4-2, plasma-desktop 6.7.4-1,
and the installed Breeze icon names. Qt text properties target Qt 6.11.2:
https://doc.qt.io/qt-6.11/qml-qtquick-text.html

Updates: maintain paths and aliases here; bump the owning RPM and theme metadata.
New state variants must retain distinct meanings; unreviewed warning, charging,
wireless-signal and third-party icons continue to use upstream artwork.
