Name:           proper-agent-status
Version:        0.1
Release:        2%{?dist}
Summary:        Proper Linux coding-agent usage widget
License:        GPL-3.0-or-later
BuildArch:      noarch
BuildRequires:  python3
Requires:       python3
Requires:       plasma-workspace >= 6.7
Requires:       plasma5support >= 6.7
Requires:       proper-branding >= 0.1-3

%description
A small Plasma panel widget and credential-free normalizer for supported
coding-agent usage limits. Codex is read through its local app-server and
Claude is read through its supported status-line feed.

%check
python3 -m unittest discover -s %{_sourcedir}/tests -v

%install
install -Dpm 0755 %{_sourcedir}/proper-agent-status %{buildroot}%{_bindir}/proper-agent-status
install -Dpm 0644 %{_sourcedir}/plasmoid/metadata.json %{buildroot}%{_datadir}/plasma/plasmoids/com.properlinux.agentstatus/metadata.json
install -Dpm 0644 %{_sourcedir}/plasmoid/contents/ui/main.qml %{buildroot}%{_datadir}/plasma/plasmoids/com.properlinux.agentstatus/contents/ui/main.qml
install -Dpm 0644 %{_sourcedir}/plasmoid/contents/ui/CompactRepresentation.qml %{buildroot}%{_datadir}/plasma/plasmoids/com.properlinux.agentstatus/contents/ui/CompactRepresentation.qml
install -Dpm 0644 %{_sourcedir}/plasmoid/contents/ui/FullRepresentation.qml %{buildroot}%{_datadir}/plasma/plasmoids/com.properlinux.agentstatus/contents/ui/FullRepresentation.qml
install -Dpm 0644 %{_sourcedir}/plasmoid/contents/images/codex-white.svg %{buildroot}%{_datadir}/plasma/plasmoids/com.properlinux.agentstatus/contents/images/codex-white.svg
install -Dpm 0644 %{_sourcedir}/plasmoid/contents/images/claude-white.svg %{buildroot}%{_datadir}/plasma/plasmoids/com.properlinux.agentstatus/contents/images/claude-white.svg
install -Dpm 0644 %{_sourcedir}/proper-agent-panel.service %{buildroot}%{_userunitdir}/proper-agent-panel.service
install -Dpm 0644 %{_sourcedir}/proper-agent-panel.timer %{buildroot}%{_userunitdir}/proper-agent-panel.timer
mkdir -p %{buildroot}%{_userunitdir}/timers.target.wants
ln -s ../proper-agent-panel.timer %{buildroot}%{_userunitdir}/timers.target.wants/proper-agent-panel.timer

%files
%{_bindir}/proper-agent-status
%{_datadir}/plasma/plasmoids/com.properlinux.agentstatus/
%{_userunitdir}/proper-agent-panel.service
%{_userunitdir}/proper-agent-panel.timer
%{_userunitdir}/timers.target.wants/proper-agent-panel.timer

%changelog
* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Present usage in a native right-aligned Plasma panel matching the main shelf
- Match the shelf height, edge inset, material, and floating attachment behaviour
- Seed the panel once only after a supported agent is installed
- Reduce the compact view to monochrome provider marks and Proper square-dot meters

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-1
- Add a compact bottom-right agent-usage card and pointer-opened detail panel
- Read Codex through its supported local app-server JSON-RPC interface
- Capture only Claude rate-limit percentages and reset times from its status line
