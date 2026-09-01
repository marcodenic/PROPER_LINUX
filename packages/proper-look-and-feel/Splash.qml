/*
    SPDX-FileCopyrightText: 2026 Proper Linux contributors
    SPDX-License-Identifier: GPL-2.0-or-later
*/

import QtQuick

Rectangle {
    id: root

    color: "#050608"
    property int stage: 0

    Image {
        id: logo
        anchors.centerIn: parent
        width: 96
        height: 96
        asynchronous: true
        fillMode: Image.PreserveAspectFit
        opacity: root.stage >= 2 ? 1 : 0
        source: "file:///usr/share/icons/hicolor/scalable/apps/proper-logo-icon.svg"

        Behavior on opacity {
            NumberAnimation { duration: 220 }
        }
    }
}
