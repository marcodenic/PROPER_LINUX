// SPDX-License-Identifier: LGPL-2.0-or-later
pragma ComponentBehavior: Bound
import QtQuick
import QtQuick.Layouts
import org.kde.kirigami as Kirigami
import org.kde.plasma.components as PlasmaComponents

Item {
    id: root
    // ToolTipArea makes the item visible when it reparents it into its popup.
    visible: false
    // ToolTipArea reparents this item into the native PopupPlasmaWindow.
    // Its margin is outside the painted card and respects panel orientation.
    Window.onWindowChanged: {
        if (Window.window && typeof Window.window.margin !== "undefined") Window.window.margin = 8;
    }
    required property var sourceArea
    implicitWidth: Math.min(420, content.implicitWidth) + 24
    implicitHeight: content.implicitHeight + 24
    LayoutMirroring.enabled: Qt.application.layoutDirection === Qt.RightToLeft
    LayoutMirroring.childrenInherit: true

    RowLayout {
        id: content
        anchors.fill: parent
        anchors.margins: 12
        spacing: 14
        Rectangle {
            Layout.alignment: Qt.AlignTop
            Layout.preferredWidth: 40
            Layout.preferredHeight: 40
            radius: 12
            color: Qt.alpha(Kirigami.Theme.highlightColor, 0.10)
            visible: symbol.valid
            Kirigami.Icon {
                id: symbol
                anchors.centerIn: parent
                width: 24
                height: 24
                animated: false
                source: root.sourceArea.icon
            }
        }
        ColumnLayout {
            Layout.maximumWidth: 342
            Layout.fillWidth: true
            spacing: 4
            PlasmaComponents.Label {
                Layout.fillWidth: true
                text: root.sourceArea.mainText
                textFormat: Text.PlainText
                font.weight: Font.DemiBold
                wrapMode: Text.Wrap
                visible: text.length > 0
            }
            PlasmaComponents.Label {
                Layout.fillWidth: true
                text: root.sourceArea.subText
                textFormat: root.sourceArea.textFormat
                color: Qt.alpha(Kirigami.Theme.textColor, 0.72)
                wrapMode: Text.Wrap
                maximumLineCount: 8
                elide: Text.ElideRight
                visible: text.length > 0
            }
        }
    }
}
