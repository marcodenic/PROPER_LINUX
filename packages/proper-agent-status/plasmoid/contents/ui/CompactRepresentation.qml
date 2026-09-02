// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Controls as Controls
import QtQuick.Layouts

import org.kde.kirigami as Kirigami

FocusScope {
    id: compact

    required property var controller
    readonly property int providerCount: controller.installedProviders.length
    readonly property int compactWidth: providerCount > 1 ? 232 : 124

    function providerSummary(provider) {
        const usageWindow = controller.primaryWindow(provider);
        if (!usageWindow) {
            return provider.label + " usage unavailable";
        }
        return provider.label + " · "
            + controller.percentText(usageWindow.remaining_percent) + " remaining";
    }

    implicitWidth: controller.loaded && controller.anyInstalled ? compactWidth : 1
    implicitHeight: Kirigami.Units.gridUnit * 2
    Layout.minimumWidth: implicitWidth
    Layout.preferredWidth: implicitWidth
    Layout.fillHeight: true
    opacity: controller.loaded && controller.anyInstalled ? 1 : 0
    activeFocusOnTab: controller.anyInstalled
    Accessible.role: Accessible.Button
    Accessible.name: "Agent usage"
    Accessible.description: controller.installedProviders.map(providerSummary).join(", ")
    Accessible.onPressAction: controller.expanded = !controller.expanded

    RowLayout {
        anchors.centerIn: parent
        spacing: 12

        Repeater {
            model: compact.controller.installedProviders

            delegate: RowLayout {
                id: providerItem
                required property var modelData
                required property int index
                readonly property var usageWindow: compact.controller.primaryWindow(modelData)
                readonly property int litDots: usageWindow
                    ? Math.round(usageWindow.remaining_percent / 10)
                    : 0

                spacing: 9

                Image {
                    Layout.preferredWidth: 18
                    Layout.preferredHeight: 18
                    sourceSize.width: 18
                    sourceSize.height: 18
                    fillMode: Image.PreserveAspectFit
                    source: providerItem.modelData.id === "claude"
                        ? Qt.resolvedUrl("../images/claude-white.svg")
                        : Qt.resolvedUrl("../images/codex-white.svg")
                }

                RowLayout {
                    spacing: 3

                    Repeater {
                        model: 10

                        delegate: Rectangle {
                            required property int index
                            Layout.preferredWidth: 5
                            Layout.preferredHeight: 5
                            radius: 0.8
                            color: Kirigami.Theme.textColor
                            opacity: index < providerItem.litDots ? 0.92 : 0.14

                            Behavior on opacity {
                                NumberAnimation { duration: 180; easing.type: Easing.OutCubic }
                            }
                        }
                    }
                }

                Rectangle {
                    visible: providerItem.index < compact.providerCount - 1
                    Layout.leftMargin: 2
                    Layout.preferredWidth: 1
                    Layout.preferredHeight: 20
                    color: Kirigami.Theme.textColor
                    opacity: 0.12
                }
            }
        }
    }

    Rectangle {
        anchors.fill: parent
        radius: 9
        color: Kirigami.Theme.textColor
        opacity: mouseArea.containsMouse ? 0.08 : 0

        Behavior on opacity { NumberAnimation { duration: 120 } }
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        enabled: compact.controller.anyInstalled
        hoverEnabled: true
        cursorShape: Qt.PointingHandCursor
        onClicked: compact.controller.expanded = !compact.controller.expanded
    }

    Keys.onSpacePressed: controller.expanded = !controller.expanded
    Keys.onReturnPressed: controller.expanded = !controller.expanded

    Controls.ToolTip {
        visible: mouseArea.containsMouse && !controller.expanded
        delay: Kirigami.Units.toolTipDelay
        text: controller.installedProviders.map(compact.providerSummary).join("\n")
    }
}
