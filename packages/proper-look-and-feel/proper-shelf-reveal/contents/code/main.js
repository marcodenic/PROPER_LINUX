// SPDX-FileCopyrightText: 2026 Proper Linux contributors
// SPDX-License-Identifier: GPL-2.0-or-later
"use strict";

function revealShelf(window) {
    if (!window.visible || window.properShelfRevealed) {
        return;
    }
    window.properShelfRevealed = true;
    // Keep the surface painting while Plasma settles its initial layout.
    animate({
        window: window,
        type: Effect.Opacity,
        from: 0.001,
        to: 1.0,
        duration: animationTime(700),
        curve: QEasingCurve.InExpo
    });
}

function watchShelf(window) {
    if (!window.dock || window.windowClass.indexOf("plasmashell") < 0) {
        return;
    }
    window.windowHiddenChanged.connect(revealShelf);
    revealShelf(window);
}

effects.windowAdded.connect(watchShelf);
