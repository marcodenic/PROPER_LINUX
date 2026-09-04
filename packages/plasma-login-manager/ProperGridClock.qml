/*
    SPDX-FileCopyrightText: 2026 Proper Linux contributors
    SPDX-License-Identifier: LGPL-2.0-or-later
*/

pragma ComponentBehavior: Bound

import QtQuick

Item {
    id: root

    property date currentDate: new Date()
    property string timeFormat: "hh:mm"
    property real cellSize: 10
    property real cellGap: Math.max(2, cellSize * 0.3)
    property real glyphGap: cellSize
    property color cellColor: properTokens.text
    property color shadowColor: properTokens.alpha(properTokens.base, 0.45)

    ProperTokens {
        id: properTokens
    }

    readonly property int rowCount: 7
    readonly property int digitColumnCount: 5
    readonly property int colonColumnCount: 1
    readonly property string displayTime: Qt.formatTime(currentDate, timeFormat)
    readonly property real digitWidth: digitColumnCount * cellSize + (digitColumnCount - 1) * cellGap
    readonly property real colonWidth: colonColumnCount * cellSize

    implicitWidth: digitWidth * 4 + colonWidth + glyphGap * 4
    implicitHeight: rowCount * cellSize + (rowCount - 1) * cellGap

    Accessible.name: displayTime
    Accessible.role: Accessible.StaticText
    LayoutMirroring.enabled: false
    LayoutMirroring.childrenInherit: true

    function glyphColumns(character) {
        return character === ":" ? colonColumnCount : digitColumnCount
    }

    function glyphPattern(character) {
        const patterns = {
            "0": "01110" +
                 "10001" +
                 "10001" +
                 "10001" +
                 "10001" +
                 "10001" +
                 "01110",
            "1": "00100" +
                 "01100" +
                 "00100" +
                 "00100" +
                 "00100" +
                 "00100" +
                 "01110",
            "2": "01110" +
                 "10001" +
                 "00001" +
                 "00010" +
                 "00100" +
                 "01000" +
                 "11111",
            "3": "11110" +
                 "00001" +
                 "00001" +
                 "01110" +
                 "00001" +
                 "00001" +
                 "11110",
            "4": "00010" +
                 "00110" +
                 "01010" +
                 "10010" +
                 "11111" +
                 "00010" +
                 "00010",
            "5": "11111" +
                 "10000" +
                 "10000" +
                 "11110" +
                 "00001" +
                 "00001" +
                 "11110",
            "6": "01110" +
                 "10000" +
                 "10000" +
                 "11110" +
                 "10001" +
                 "10001" +
                 "01110",
            "7": "11111" +
                 "00001" +
                 "00010" +
                 "00100" +
                 "01000" +
                 "01000" +
                 "01000",
            "8": "01110" +
                 "10001" +
                 "10001" +
                 "01110" +
                 "10001" +
                 "10001" +
                 "01110",
            "9": "01110" +
                 "10001" +
                 "10001" +
                 "01111" +
                 "00001" +
                 "00001" +
                 "01110",
            ":": "0" +
                 "0" +
                 "1" +
                 "0" +
                 "1" +
                 "0" +
                 "0"
        }
        return patterns[character] || ""
    }

    function glyphX(glyphIndex) {
        let position = 0
        for (let index = 0; index < glyphIndex; ++index) {
            const character = displayTime.charAt(index)
            position += (character === ":" ? colonWidth : digitWidth) + glyphGap
        }
        return position
    }

    Repeater {
        model: root.displayTime.length

        delegate: Item {
            id: glyph

            required property int index
            readonly property string character: root.displayTime.charAt(index)
            readonly property int columnCount: root.glyphColumns(character)
            readonly property string pattern: root.glyphPattern(character)

            x: root.glyphX(index)
            width: columnCount * root.cellSize + (columnCount - 1) * root.cellGap
            height: root.implicitHeight

            Repeater {
                model: glyph.columnCount * root.rowCount

                delegate: Item {
                    required property int index

                    x: (index % glyph.columnCount) * (root.cellSize + root.cellGap)
                    y: Math.floor(index / glyph.columnCount) * (root.cellSize + root.cellGap)
                    width: root.cellSize
                    height: root.cellSize
                    visible: glyph.pattern.charAt(index) === "1"

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
}
