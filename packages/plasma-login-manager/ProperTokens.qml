// Generated from tokens.yaml; do not edit.
// SPDX-License-Identifier: GPL-2.0-or-later
import QtQuick

QtObject {
    readonly property color base: "#11151d"
    readonly property color surface: "#181d25"
    readonly property color surface_alt: "#232933"
    readonly property color view: "#151a22"
    readonly property color view_alt: "#1d232c"
    readonly property color text: "#f1f4f8"
    readonly property color muted: "#a8b2c2"
    readonly property color accent: "#91b4ff"
    readonly property color selection: "#4f6f99"
    readonly property color on_accent: "#11151d"
    readonly property color positive: "#57be82"
    readonly property color warning: "#dea55c"
    readonly property color urgent: "#e86978"
    readonly property color visited: "#b489d3"
    readonly property color border: "#a8b2c2"
    readonly property int controlRadius: 9
    readonly property int spacingUnit: 4
    readonly property int spacingItem: 8
    readonly property int spacingSection: 16
    readonly property int animationFast: 120
    readonly property int animationNormal: 180
    readonly property string uiFont: "Inter"
    readonly property color arrivalBase: "#050608"
    readonly property color arrivalWordmark: "#f7f8fa"

    function alpha(colour, value) {
        return Qt.rgba(colour.r, colour.g, colour.b, value)
    }
}
