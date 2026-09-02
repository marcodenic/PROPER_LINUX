// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Controls as Controls
import QtQuick.Layouts

import org.kde.kirigami as Kirigami

FocusScope {
    id: compact

    required property var controller
    property real pressedY: 0
    property bool dragged: false

    implicitWidth: 112
    implicitHeight: 8
    Layout.fillWidth: true
    Layout.fillHeight: true
    activeFocusOnTab: true
    Accessible.role: Accessible.Button
    Accessible.name: "Open status shade"
    Accessible.description: "System health, network activity, and coding-agent limits"
    Accessible.onPressAction: controller.expanded = !controller.expanded

    Rectangle {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        width: 64
        height: 3
        radius: 1.5
        color: Kirigami.Theme.textColor
        opacity: pointer.containsMouse || compact.controller.expanded ? 0.76 : 0.34

        Behavior on opacity { NumberAnimation { duration: 120 } }
    }

    MouseArea {
        id: pointer
        anchors.fill: parent
        hoverEnabled: true
        cursorShape: Qt.PointingHandCursor
        preventStealing: true

        onPressed: function(mouse) {
            compact.pressedY = mouse.y;
            compact.dragged = false;
        }
        onPositionChanged: function(mouse) {
            if (pressed && mouse.y - compact.pressedY >= 4) {
                compact.dragged = true;
                compact.controller.expanded = true;
            }
        }
        onClicked: {
            if (!compact.dragged) {
                compact.controller.expanded = !compact.controller.expanded;
            }
        }
    }

    Keys.onSpacePressed: controller.expanded = !controller.expanded
    Keys.onReturnPressed: controller.expanded = !controller.expanded

    Controls.ToolTip {
        visible: pointer.containsMouse && !controller.expanded
        delay: Kirigami.Units.toolTipDelay
        text: "Open status shade · Meta+S"
    }
}
