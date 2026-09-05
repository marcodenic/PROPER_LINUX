// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Layouts

import org.kde.plasma.core as PlasmaCore
import org.kde.plasma.plasma5support as Plasma5Support
import org.kde.plasma.plasmoid

PlasmoidItem {
    id: root

    readonly property string systemCommand: "/usr/bin/proper-agent-status --system-snapshot"
    readonly property string agentCommand: "/usr/bin/proper-agent-status"
    property var system: ({})
    property var network: ({ connected: false, name: "Checking network…" })
    property var providers: []
    property bool systemLoaded: false
    property bool agentsLoaded: false
    property bool systemRefreshing: false
    property bool agentsRefreshing: false
    property int systemRevision: 0

    function refreshSystem() {
        if (systemRefreshing) {
            return;
        }
        systemRefreshing = true;
        systemSource.disconnectSource(systemCommand);
        systemSource.connectSource(systemCommand);
    }

    function refreshAgents() {
        if (agentsRefreshing) {
            return;
        }
        agentsRefreshing = true;
        agentSource.disconnectSource(agentCommand);
        agentSource.connectSource(agentCommand);
    }

    function primaryWindow(provider) {
        if (!provider || !provider.windows || provider.windows.length === 0) {
            return null;
        }
        let shortest = provider.windows[0];
        for (let index = 1; index < provider.windows.length; ++index) {
            if ((provider.windows[index].duration_minutes || Number.MAX_VALUE)
                    < (shortest.duration_minutes || Number.MAX_VALUE)) {
                shortest = provider.windows[index];
            }
        }
        return shortest;
    }

    function provider(identifier) {
        for (let index = 0; index < providers.length; ++index) {
            if (providers[index].id === identifier) {
                return providers[index];
            }
        }
        return ({ id: identifier, label: identifier === "claude" ? "Claude" : "Codex", installed: false, windows: [] });
    }

    preferredRepresentation: compactRepresentation
    Plasmoid.backgroundHints: PlasmaCore.Types.NoBackground
    Plasmoid.status: PlasmaCore.Types.ActiveStatus
    Plasmoid.icon: "dashboard-show"
    Plasmoid.title: "Command Centre"
    toolTipMainText: "Command Centre"
    toolTipSubText: "System and agent status · Meta+S"
    toolTipItem: ProperToolTip {
        sourceArea: QtObject {
            readonly property string mainText: root.toolTipMainText
            readonly property string subText: root.toolTipSubText
            readonly property string icon: "dashboard-show"
            readonly property int textFormat: Text.PlainText
        }
    }

    compactRepresentation: CompactRepresentation {
        controller: root
    }

    fullRepresentation: FullRepresentation {
        controller: root
    }

    Plasma5Support.DataSource {
        id: systemSource
        engine: "executable"

        onNewData: function(sourceName, data) {
            disconnectSource(sourceName);
            root.systemRefreshing = false;
            try {
                const parsed = JSON.parse(data["stdout"] || "{}");
                if (parsed.schema_version === 1 && parsed.system && parsed.network) {
                    root.system = parsed.system;
                    root.network = parsed.network;
                    root.systemLoaded = true;
                    root.systemRevision += 1;
                }
            } catch (error) {
                root.systemLoaded = true;
            }
        }
    }

    Plasma5Support.DataSource {
        id: agentSource
        engine: "executable"

        onNewData: function(sourceName, data) {
            disconnectSource(sourceName);
            root.agentsRefreshing = false;
            try {
                const parsed = JSON.parse(data["stdout"] || "{}");
                if (parsed.schema_version === 1 && Array.isArray(parsed.providers)) {
                    root.providers = parsed.providers;
                    root.agentsLoaded = true;
                }
            } catch (error) {
                root.agentsLoaded = true;
            }
        }
    }

    Timer {
        interval: 1000
        repeat: true
        running: root.expanded
        triggeredOnStart: true
        onTriggered: root.refreshSystem()
    }

    Timer {
        interval: 300000
        repeat: true
        running: true
        onTriggered: root.refreshAgents()
    }

    onExpandedChanged: {
        if (root.expanded) {
            refreshSystem();
            refreshAgents();
        }
    }

    Component.onCompleted: refreshAgents()
}
