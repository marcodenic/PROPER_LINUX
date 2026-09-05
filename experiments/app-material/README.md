# Native application material study

A disposable Qt Widgets / KWindowEffects feasibility study for the approved
frosted-navigation, solid-content direction. It is not Dolphin, a replacement
file manager, an installed application, or a release default. The model is
read-only and provides directory navigation solely to assess real text/icons.

Build with Qt 6.11.2 and KF6 WindowSystem 6.29 (Fedora 44):

```sh
mkdir -p /tmp/proper-material-build
cd /tmp/proper-material-build
qmake6 /path/to/PROPER_LINUX/experiments/app-material/material.pro
make
./proper-material-study
```

The native top-level window has an alpha buffer before it is shown. Only its
220-pixel navigation region requests KWin blur. An 80% tint comes from the
active Qt palette; the content widget paints an opaque palette background.
Text and icons stay fully opaque. The checkbox compares native frost with a
solid navigation fallback. This is a manual comparison, not automatic
compositor capability detection. No settings or user files are written.

Review over wallpaper and another app, toggle solid, resize, and compare light
and dark palettes. Dolphin integration is still unproven: Aurorae controls the
window decoration, not Dolphin's client painting. Do not deploy global opacity
rules or force blur over opaque widgets. An eventual implementation must use a
maintainable upstream/Qt extension and handle compositor-disabled operation,
scaling, palette changes, menus, selections and native file operations.

Sources checked 5 September 2026:
- https://doc.qt.io/qt-6.11/qwidget.html#creating-translucent-windows
- https://api.kde.org/kwindoweffects.html
- https://raw.githubusercontent.com/KDE/kwindowsystem/v6.29.0/src/kwindoweffects.h
- https://raw.githubusercontent.com/KDE/dolphin/v26.08.0/src/dolphinmainwindow.cpp
