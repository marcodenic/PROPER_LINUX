// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Controls as Controls
import QtQuick.Layouts

import org.kde.kirigami as Kirigami

Item {
    id: details

    required property var controller
    readonly property int panelHeight: content.implicitHeight + 32

    implicitWidth: 340
    implicitHeight: panelHeight
    Layout.minimumWidth: 340
    Layout.minimumHeight: implicitHeight

    Rectangle {
        id: surface
        width: 340
        height: details.panelHeight
        anchors.centerIn: parent
        radius: 16
        color: "#f2171a20"
        border.width: 1
        border.color: "#2effffff"
    }

    ColumnLayout {
        id: content
        parent: surface
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.margins: 16
        spacing: 0

        RowLayout {
            Layout.fillWidth: true
            Layout.bottomMargin: 14
            spacing: 10

            ColumnLayout {
                Layout.fillWidth: true
                spacing: 2

                Text {
                    text: "Agent usage"
                    color: "#f2f4f7"
                    font.family: "Inter"
                    font.pixelSize: 17
                    font.weight: Font.DemiBold
                }

                Text {
                    text: "Current limits · no history stored"
                    color: "#798493"
                    font.family: "Inter"
                    font.pixelSize: 10
                }
            }

            Controls.ToolButton {
                id: refreshButton
                implicitWidth: 32
                implicitHeight: 32
                enabled: !details.controller.refreshing
                display: Controls.AbstractButton.IconOnly
                icon.name: "view-refresh-symbolic"
                onClicked: details.controller.refresh()
                Controls.ToolTip.text: "Refresh"
                Controls.ToolTip.visible: hovered
            }
        }

        Repeater {
            model: details.controller.installedProviders

            delegate: ColumnLayout {
                id: providerSection
                required property var modelData
                Layout.fillWidth: true
                Layout.bottomMargin: 14
                spacing: 8

                RowLayout {
                    Layout.fillWidth: true
                    spacing: 8

                    Rectangle {
                        Layout.preferredWidth: 4
                        Layout.preferredHeight: 18
                        radius: 2
                        color: details.controller.accentFor(providerSection.modelData.id)
                    }

                    Text {
                        text: providerSection.modelData.label
                        color: "#eef1f5"
                        font.family: "Inter"
                        font.pixelSize: 14
                        font.weight: Font.DemiBold
                    }

                    Text {
                        text: providerSection.modelData.plan ? providerSection.modelData.plan.toUpperCase() : ""
                        visible: text.length > 0
                        color: "#697484"
                        font.family: "Inter"
                        font.pixelSize: 8
                        font.weight: Font.DemiBold
                        font.letterSpacing: 0.8
                    }

                    Item { Layout.fillWidth: true }

                    Text {
                        text: providerSection.modelData.status === "ok" ? "LIVE" : ""
                        visible: text.length > 0
                        color: details.controller.accentFor(providerSection.modelData.id)
                        font.family: "Inter"
                        font.pixelSize: 8
                        font.weight: Font.DemiBold
                        font.letterSpacing: 0.9
                    }
                }

                Repeater {
                    model: providerSection.modelData.windows || []

                    delegate: Item {
                        id: windowRow
                        required property var modelData
                        Layout.fillWidth: true
                        Layout.preferredHeight: 42

                        RowLayout {
                            anchors.left: parent.left
                            anchors.right: parent.right
                            anchors.top: parent.top
                            height: 25

                            ColumnLayout {
                                spacing: 0

                                Text {
                                    text: windowRow.modelData.label + " window"
                                    color: "#cbd1da"
                                    font.family: "Inter"
                                    font.pixelSize: 11
                                    font.weight: Font.Medium
                                }

                                Text {
                                    text: details.controller.resetText(windowRow.modelData.resets_at)
                                    color: "#687383"
                                    font.family: "Inter"
                                    font.pixelSize: 9
                                }
                            }

                            Item { Layout.fillWidth: true }

                            Text {
                                text: details.controller.percentText(windowRow.modelData.remaining_percent)
                                color: "#f0f2f6"
                                font.family: "Inter"
                                font.pixelSize: 15
                                font.weight: Font.DemiBold
                            }

                            Text {
                                text: "LEFT"
                                color: "#717c8b"
                                font.family: "Inter"
                                font.pixelSize: 8
                                font.weight: Font.DemiBold
                                font.letterSpacing: 0.7
                            }
                        }

                        Rectangle {
                            anchors.left: parent.left
                            anchors.right: parent.right
                            anchors.bottom: parent.bottom
                            anchors.bottomMargin: 3
                            height: 3
                            radius: 1.5
                            color: "#1cffffff"

                            Rectangle {
                                width: parent.width * windowRow.modelData.remaining_percent / 100
                                height: parent.height
                                radius: 1.5
                                color: details.controller.accentFor(providerSection.modelData.id)
                            }
                        }
                    }
                }

                ColumnLayout {
                    visible: !providerSection.modelData.windows || providerSection.modelData.windows.length === 0
                    Layout.fillWidth: true
                    spacing: 8

                    Text {
                        Layout.fillWidth: true
                        text: providerSection.modelData.message || "Usage is not available yet."
                        color: "#8e98a6"
                        font.family: "Inter"
                        font.pixelSize: 10
                        wrapMode: Text.WordWrap
                    }

                    Controls.Button {
                        visible: providerSection.modelData.action === "connect"
                        text: "Connect Claude"
                        icon.name: "network-connect-symbolic"
                        onClicked: details.controller.connectClaude()
                    }
                }
            }
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 1
            color: "#18ffffff"
        }

        RowLayout {
            Layout.fillWidth: true
            Layout.topMargin: 10
            spacing: 6

            Text {
                text: "Only percentages and reset times are read"
                color: "#626d7c"
                font.family: "Inter"
                font.pixelSize: 9
            }

            Item { Layout.fillWidth: true }

            Rectangle {
                Layout.preferredWidth: 5
                Layout.preferredHeight: 5
                radius: 2.5
                color: details.controller.refreshing ? "#d9a178" : "#718096"
            }
        }
    }
}
