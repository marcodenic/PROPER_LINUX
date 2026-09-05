# Tray tooltip presentation

Source: Fedora plasma-workspace 6.7.4-2.fc44, URL and SHA256 in source-rpm.env.
Upstream: https://invent.kde.org/plasma/plasma-workspace/-/tree/v6.7.4/applets/systemtray
Original ProperToolTip.qml: LGPL-2.0-or-later. Patch preserves upstream headers/licences.

The compiled delegates do not expose a shell-theme hook for tooltip composition. Forward the existing applet/SNI icon and use a bounded 40px icon tile, semibold title and secondary status. Preserve applet-owned custom tooltips and rich-text formatting. Do not parse translated status strings or remove connection details. libplasma remains Fedora's package.

Update: rebase the narrow patch against the matching Fedora source RPM, update checksum/spec release, run dark/light network, audio, SNI and custom-tooltip graphical checks. Drop the exception when upstream exposes the presentation hook. No credential or networking behaviour changes.

Fedora release 2 rebuilds against Qt 6; preserve it rather than using cached release 1. The upstream archive and patches are unchanged between these Fedora source releases.

ToolTipArea explicitly shows a custom mainItem before reparenting it into the
native popup. ProperToolTip therefore starts invisible; otherwise its children
paint inside the panel before the first hover. This lifecycle is verified in
libplasma 6.7.4 tooltiparea.cpp, without patching that library. Package upgrades
must replace the plugin safely; never overwrite a loaded .so in place.
