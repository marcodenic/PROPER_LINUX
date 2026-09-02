/*
    SPDX-FileCopyrightText: 2026 Proper Linux contributors
    SPDX-License-Identifier: GPL-2.0-or-later
*/

pragma ComponentBehavior: Bound

import QtQuick

Item {
    id: root

    property int passwordLength: 0
    property real cellSize: 8
    property real cellGap: 6
    property color cellColor: "#f3f8ff"
    property color shadowColor: Qt.rgba(0, 0.02, 0.06, 0.42)

    readonly property int maximumVisibleCells: Math.max(1, Math.floor((width + cellGap) / (cellSize + cellGap)))
    readonly property int visibleCellCount: Math.min(passwordLength, maximumVisibleCells)

    Accessible.ignored: true

    Row {
        anchors.centerIn: parent
        spacing: root.cellGap

        Repeater {
            model: root.visibleCellCount

            delegate: Item {
                width: root.cellSize
                height: root.cellSize

                Rectangle {
                    y: 1
                    width: parent.width
                    height: parent.height
                    color: root.shadowColor
                    radius: Math.max(0.75, root.cellSize * 0.1)
                }

                Rectangle {
                    width: parent.width
                    height: parent.height
                    color: root.cellColor
                    radius: Math.max(0.75, root.cellSize * 0.1)
                }
            }
        }
    }
}
