// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Layouts

import org.kde.kirigami as Kirigami

FocusScope {
    id: compact

    required property var controller

    implicitWidth: 36
    implicitHeight: 36
    Layout.minimumWidth: 36
    Layout.fillHeight: true
    activeFocusOnTab: true
    Accessible.role: Accessible.Button
    Accessible.name: "Open Command Centre"
    Accessible.description: "System health, network activity, and coding-agent limits"
    Accessible.onPressAction: controller.expanded = !controller.expanded

    Rectangle {
        anchors.centerIn: parent
        width: 32
        height: 32
        radius: 9
        color: Kirigami.Theme.highlightColor
        opacity: pointer.containsMouse || compact.controller.expanded ? 0.18 : 0

        Behavior on opacity { NumberAnimation { duration: 120 } }
    }

    Kirigami.Icon {
        anchors.centerIn: parent
        width: 20
        height: 20
        source: "dashboard-show"
        color: Kirigami.Theme.textColor
        opacity: compact.controller.expanded ? 1 : 0.82
    }

    MouseArea {
        id: pointer
        anchors.fill: parent
        hoverEnabled: true
        cursorShape: Qt.PointingHandCursor
        onClicked: compact.controller.expanded = !compact.controller.expanded
    }

    Keys.onSpacePressed: controller.expanded = !controller.expanded
    Keys.onReturnPressed: controller.expanded = !controller.expanded

}
