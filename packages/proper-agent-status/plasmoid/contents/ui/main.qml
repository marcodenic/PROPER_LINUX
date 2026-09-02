// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick
import QtQuick.Layouts

import org.kde.plasma.core as PlasmaCore
import org.kde.plasma.plasma5support as Plasma5Support
import org.kde.plasma.plasmoid

PlasmoidItem {
    id: root

    readonly property string snapshotCommand: "/usr/bin/proper-agent-status"
    readonly property string connectClaudeCommand: "/usr/bin/proper-agent-status --install-claude-hook"
    property var providers: []
    property bool loaded: false
    property bool refreshing: false
    readonly property var installedProviders: providers.filter(provider => provider.installed)
    readonly property bool anyInstalled: installedProviders.length > 0

    function refresh() {
        if (refreshing) {
            return;
        }
        refreshing = true;
        snapshotSource.disconnectSource(snapshotCommand);
        snapshotSource.connectSource(snapshotCommand);
    }

    function connectClaude() {
        claudeActionSource.disconnectSource(connectClaudeCommand);
        claudeActionSource.connectSource(connectClaudeCommand);
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

    function percentText(value) {
        if (value === undefined || value === null) {
            return "—";
        }
        return Math.round(value) + "%";
    }

    function resetText(epoch) {
        if (!epoch) {
            return "Reset time unavailable";
        }
        const seconds = Math.max(0, epoch - Math.floor(Date.now() / 1000));
        if (seconds < 90) {
            return "Resets in a minute";
        }
        const minutes = Math.floor(seconds / 60);
        if (minutes < 60) {
            return "Resets in " + minutes + "m";
        }
        const hours = Math.floor(minutes / 60);
        if (hours < 24) {
            return "Resets in " + hours + "h";
        }
        const days = Math.floor(hours / 24);
        const remainder = hours % 24;
        return "Resets in " + days + "d" + (remainder > 0 ? " " + remainder + "h" : "");
    }

    function accentFor(identifier) {
        return identifier === "claude" ? "#d9a178" : "#8eb8ff";
    }

    preferredRepresentation: compactRepresentation
    Plasmoid.backgroundHints: PlasmaCore.Types.NoBackground
    Plasmoid.status: anyInstalled ? PlasmaCore.Types.ActiveStatus : PlasmaCore.Types.PassiveStatus
    Plasmoid.icon: "proper-agent"
    Plasmoid.title: "Agent Usage"
    toolTipMainText: "Agent usage"
    toolTipSubText: anyInstalled ? "Current plan limits" : "Shown when a supported agent is installed"

    compactRepresentation: CompactRepresentation {
        controller: root
    }

    fullRepresentation: FullRepresentation {
        controller: root
    }

    Plasma5Support.DataSource {
        id: snapshotSource
        engine: "executable"

        onNewData: function(sourceName, data) {
            disconnectSource(sourceName);
            root.refreshing = false;
            try {
                const parsed = JSON.parse(data["stdout"] || "{}");
                if (parsed.schema_version === 1 && Array.isArray(parsed.providers)) {
                    root.providers = parsed.providers;
                    root.loaded = true;
                }
            } catch (error) {
                root.loaded = true;
            }
        }
    }

    Plasma5Support.DataSource {
        id: claudeActionSource
        engine: "executable"

        onNewData: function(sourceName, data) {
            disconnectSource(sourceName);
            refreshAfterAction.restart();
        }
    }

    Timer {
        interval: 300000
        repeat: true
        running: true
        onTriggered: root.refresh()
    }

    Timer {
        id: refreshAfterAction
        interval: 800
        onTriggered: root.refresh()
    }

    Component.onCompleted: refresh()
}
