// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Controls as Controls
import QtQuick.Layouts
import QtQuick.Window

import org.kde.ksvg as KSvg

FocusScope {
    id: shade

    required property var controller
    property var downloadHistory: []
    property var uploadHistory: []
    readonly property color foreground: "#f1f4f8"
    readonly property color secondary: "#a8b2c2"
    readonly property color tertiary: "#687386"
    readonly property color downloadColor: "#79eadb"
    readonly property color uploadColor: "#91b4ff"
    readonly property color urgent: "#ff7184"
    readonly property bool narrow: width < 900

    implicitWidth: Math.max(720, Screen.width - 24)
    implicitHeight: narrow ? 376 : 286
    Layout.minimumWidth: Math.min(implicitWidth, 720)
    Layout.minimumHeight: implicitHeight
    activeFocusOnTab: true

    function capacity(bytes, total) {
        if (!Number.isFinite(bytes) || !Number.isFinite(total) || total <= 0) {
            return "—";
        }
        const unit = total >= 900000000000 ? "TB" : "GB";
        const divisor = unit === "TB" ? 1000000000000 : 1000000000;
        const usedValue = bytes / divisor;
        const totalValue = total / divisor;
        const usedDigits = usedValue >= 100 ? 0 : 1;
        const totalDigits = totalValue >= 100 ? 0 : (totalValue >= 10 ? 0 : 1);
        return usedValue.toFixed(usedDigits) + " / " + totalValue.toFixed(totalDigits) + " " + unit;
    }

    function rate(bytes) {
        if (!Number.isFinite(bytes)) {
            return "—";
        }
        if (bytes >= 1000000) {
            return (bytes / 1000000).toFixed(1) + " MB/s";
        }
        return Math.round(bytes / 1000) + " KB/s";
    }

    function pushSample(history, value) {
        const next = history.slice(Math.max(0, history.length - 58));
        next.push(Math.max(0, Number(value) || 0));
        while (next.length < 60) {
            next.unshift(0);
        }
        return next;
    }

    function agentSummary(provider) {
        if (!provider.installed) {
            return "Not installed";
        }
        const usageWindow = controller.primaryWindow(provider);
        if (usageWindow) {
            return Math.round(usageWindow.remaining_percent) + "% remaining";
        }
        return "Usage unavailable";
    }

    function primaryAgent() {
        const codex = controller.provider("codex");
        const claude = controller.provider("claude");
        if (controller.primaryWindow(codex)) {
            return codex;
        }
        if (controller.primaryWindow(claude)) {
            return claude;
        }
        if (codex.installed) {
            return codex;
        }
        if (claude.installed) {
            return claude;
        }
        return codex;
    }

    function primaryAgentValue() {
        const usageWindow = controller.primaryWindow(primaryAgent());
        return usageWindow ? Math.round(usageWindow.remaining_percent) + "%" : "—";
    }

    function primaryAgentName() {
        const provider = primaryAgent();
        return provider.installed ? provider.label : "";
    }

    function secondaryAgentState() {
        const primary = primaryAgent();
        const secondary = controller.provider(primary.id === "codex" ? "claude" : "codex");
        if (!primary.installed && !secondary.installed) {
            return "Codex and Claude not installed";
        }
        return secondary.label + " · " + agentSummary(secondary);
    }

    function temperature() {
        const value = controller.system.temperature_c;
        if (value === null || value === undefined || !Number.isFinite(Number(value))) {
            return "";
        }
        return Math.round(Number(value)) + "°C";
    }

    function temperatureColor() {
        return Number(controller.system.temperature_c) >= 85 ? urgent : secondary;
    }

    Connections {
        target: shade.controller

        function onSystemRevisionChanged() {
            shade.downloadHistory = shade.pushSample(shade.downloadHistory, shade.controller.network.download_bytes_per_second);
            shade.uploadHistory = shade.pushSample(shade.uploadHistory, shade.controller.network.upload_bytes_per_second);
        }
    }

    Keys.onEscapePressed: controller.expanded = false
    Component.onCompleted: forceActiveFocus()
    onVisibleChanged: {
        if (visible) {
            forceActiveFocus();
        }
    }

    KSvg.FrameSvgItem {
        id: surface
        anchors.fill: parent
        imagePath: "solid/widgets/panel-background"
    }

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight: 43

            RowLayout {
                anchors.fill: parent
                anchors.leftMargin: 20
                anchors.rightMargin: 12
                spacing: 8

                Text {
                    text: "C O M M A N D   C E N T R E   ·   M O N I T O R"
                    color: shade.foreground
                    opacity: 0.86
                    font.family: "JetBrains Mono"
                    font.pixelSize: 9
                    font.weight: Font.Medium
                    font.letterSpacing: 0.8
                }

                Item { Layout.fillWidth: true }

                Controls.ToolButton {
                    implicitWidth: 30
                    implicitHeight: 30
                    enabled: !shade.controller.systemRefreshing && !shade.controller.agentsRefreshing
                    display: Controls.AbstractButton.IconOnly
                    icon.name: "view-refresh-symbolic"
                    onClicked: {
                        shade.controller.refreshSystem();
                        shade.controller.refreshAgents();
                    }
                    Controls.ToolTip.text: "Refresh status"
                    Controls.ToolTip.visible: hovered
                }

                Controls.ToolButton {
                    implicitWidth: 30
                    implicitHeight: 30
                    display: Controls.AbstractButton.IconOnly
                    icon.name: "window-close-symbolic"
                    onClicked: shade.controller.expanded = false
                    Controls.ToolTip.text: "Close status shade"
                    Controls.ToolTip.visible: hovered
                }
            }

            Rectangle {
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                height: 1
                color: "#1ca6afbd"
            }
        }

        GridLayout {
            id: telemetryDeck
            Layout.fillWidth: true
            Layout.preferredHeight: shade.narrow ? 144 : 78
            columns: shade.narrow ? 2 : 4
            columnSpacing: 0
            rowSpacing: 0

            Repeater {
                model: [
                    {
                        label: "CPU",
                        value: shade.controller.systemLoaded
                            ? Math.round(Number(shade.controller.system.cpu_percent) || 0) + "%" : "—",
                        annotation: shade.temperature(),
                        annotationColor: shade.temperatureColor(),
                        detail: ""
                    },
                    {
                        label: "MEMORY",
                        value: shade.capacity(Number(shade.controller.system.memory_used_bytes), Number(shade.controller.system.memory_total_bytes)),
                        annotation: "",
                        annotationColor: shade.secondary,
                        detail: ""
                    },
                    {
                        label: "STORAGE",
                        value: shade.capacity(Number(shade.controller.system.storage_used_bytes), Number(shade.controller.system.storage_total_bytes)),
                        annotation: "",
                        annotationColor: shade.secondary,
                        detail: ""
                    },
                    {
                        label: "AGENT USAGE",
                        value: shade.primaryAgentValue(),
                        annotation: shade.primaryAgentName(),
                        annotationColor: shade.secondary,
                        detail: shade.secondaryAgentState()
                    }
                ]

                delegate: Item {
                    id: telemetryCell
                    required property var modelData
                    required property int index
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    Layout.preferredWidth: 1
                    Layout.preferredHeight: 72

                    ColumnLayout {
                        anchors.fill: parent
                        anchors.leftMargin: shade.narrow ? 16 : 20
                        anchors.rightMargin: shade.narrow ? 16 : 20
                        anchors.topMargin: 12
                        anchors.bottomMargin: 10
                        spacing: 0

                        Text {
                            text: telemetryCell.modelData.label
                            color: shade.secondary
                            font.family: "JetBrains Mono"
                            font.pixelSize: 9
                            font.weight: Font.Medium
                            font.letterSpacing: 1.1
                        }

                        RowLayout {
                            Layout.fillWidth: true
                            Layout.topMargin: 7
                            spacing: 8

                            Text {
                                text: telemetryCell.modelData.value
                                color: shade.foreground
                                font.family: "JetBrains Mono"
                                font.pixelSize: telemetryCell.modelData.label === "AGENT USAGE" ? 20 : 18
                                font.weight: Font.Light
                                elide: Text.ElideRight
                            }

                            Text {
                                Layout.fillWidth: true
                                text: telemetryCell.modelData.annotation
                                visible: text.length > 0
                                color: telemetryCell.modelData.annotationColor
                                font.family: "JetBrains Mono"
                                font.pixelSize: 10
                                elide: Text.ElideRight
                            }
                        }

                        Text {
                            Layout.fillWidth: true
                            Layout.topMargin: 4
                            text: telemetryCell.modelData.detail
                            visible: text.length > 0
                            color: shade.tertiary
                            font.family: "Inter"
                            font.pixelSize: 9
                            elide: Text.ElideRight
                        }
                    }

                    Rectangle {
                        anchors.right: parent.right
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        width: 1
                        visible: shade.narrow ? telemetryCell.index % 2 === 0 : telemetryCell.index < 3
                        color: "#1ca6afbd"
                    }

                    Rectangle {
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.bottom: parent.bottom
                        height: 1
                        visible: shade.narrow && telemetryCell.index < 2
                        color: "#1ca6afbd"
                    }
                }
            }
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 1
            color: "#1ca6afbd"
        }

        ColumnLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.leftMargin: shade.narrow ? 16 : 20
            Layout.rightMargin: shade.narrow ? 16 : 20
            Layout.topMargin: 12
            Layout.bottomMargin: 18
            spacing: 0

            RowLayout {
                Layout.fillWidth: true
                spacing: 20

                Text {
                    text: "B A N D W I D T H   M O N I T O R   ·   6 0   S E C O N D S"
                    color: shade.secondary
                    font.family: "JetBrains Mono"
                    font.pixelSize: 9
                    font.weight: Font.Medium
                    font.letterSpacing: 0.8
                }

                Item { Layout.fillWidth: true }

                Text {
                    text: "↓ " + shade.rate(Number(shade.controller.network.download_bytes_per_second))
                    color: shade.downloadColor
                    font.family: "JetBrains Mono"
                    font.pixelSize: 12
                }

                Text {
                    text: "↑ " + shade.rate(Number(shade.controller.network.upload_bytes_per_second))
                    color: shade.uploadColor
                    font.family: "JetBrains Mono"
                    font.pixelSize: 12
                }
            }

            Text {
                Layout.fillWidth: true
                Layout.topMargin: 4
                text: shade.controller.network.name || "Offline"
                color: shade.foreground
                opacity: 0.82
                font.family: "Inter"
                font.pixelSize: 10
                elide: Text.ElideRight
            }

            ThroughputGraph {
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.minimumHeight: 72
                Layout.topMargin: 4
                downloadHistory: shade.downloadHistory
                uploadHistory: shade.uploadHistory
                downloadColor: shade.downloadColor
                uploadColor: shade.uploadColor
            }

            RowLayout {
                Layout.fillWidth: true
                spacing: 0

                Text {
                    text: "60 seconds ago"
                    color: shade.tertiary
                    font.family: "JetBrains Mono"
                    font.pixelSize: 8
                }

                Item { Layout.fillWidth: true }

                Text {
                    text: "Now"
                    color: shade.tertiary
                    font.family: "JetBrains Mono"
                    font.pixelSize: 8
                }
            }
        }
    }

    Rectangle {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 5
        width: 42
        height: 3
        radius: 1.5
        color: shade.foreground
        opacity: closeArea.containsMouse ? 0.68 : 0.26

        Behavior on opacity { NumberAnimation { duration: 120 } }
    }

    MouseArea {
        id: closeArea
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        width: 92
        height: 18
        hoverEnabled: true
        cursorShape: Qt.PointingHandCursor
        onClicked: shade.controller.expanded = false
    }
}
