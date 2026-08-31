Name: proper-apps
Version: 0.1
Release: 7%{?dist}
Summary: Proper Linux curated application catalogue
License: GPL-3.0-or-later
BuildRequires: qt6-qtbase-devel
Requires: flatpak
Requires: kdialog
Requires: polkit
Requires: proper-terminal >= 1.3.1
%description
Small catalogue front end delegating installs to Fedora, Flatpak, and official vendor paths.
%prep
cp %{_sourcedir}/main.cpp %{_sourcedir}/proper-apps.pro .
%build
qmake6 CONFIG+=release proper-apps.pro
make %{?_smp_mflags}
%install
install -Dpm 0755 proper-apps %{buildroot}%{_bindir}/proper-apps
install -Dpm 0755 %{_sourcedir}/proper-agent %{buildroot}%{_bindir}/proper-agent
install -Dpm 0644 %{_sourcedir}/proper-apps.desktop %{buildroot}%{_datadir}/applications/proper-apps.desktop
install -Dpm 0644 %{_sourcedir}/proper-coding-agent.desktop %{buildroot}%{_datadir}/applications/proper-coding-agent.desktop
install -Dpm 0644 %{_sourcedir}/proper-agent-dolphin.desktop %{buildroot}%{_datadir}/kio/servicemenus/proper-agent-dolphin.desktop
install -Dpm 0644 %{_sourcedir}/../../apps/catalogue-v2.json %{buildroot}%{_datadir}/proper-apps/catalogue-v2.json
install -d %{buildroot}%{_datadir}/proper-apps/icons
install -pm 0644 %{_sourcedir}/icons/* %{buildroot}%{_datadir}/proper-apps/icons/
%files
%{_bindir}/proper-apps
%{_bindir}/proper-agent
%{_datadir}/applications/proper-apps.desktop
%{_datadir}/applications/proper-coding-agent.desktop
%{_datadir}/kio/servicemenus/proper-agent-dolphin.desktop
%{_datadir}/proper-apps/catalogue-v2.json
%{_datadir}/proper-apps/icons/

%changelog
* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-7
- Add one generic Coding Agent action for the launcher, app menu, and Dolphin
- Choose, install, and save Codex, Claude Code, or OpenCode only after success
- Reopen the chooser when a saved agent is missing instead of silently falling back

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-6
- Add the responsive Proper Apps 2 catalogue and user-created web apps.
- Expand the audited optional catalogue and make install/remove metadata explicit.
- Ship pinned upstream application artwork instead of placeholder letter tiles.
* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-5
- Offer optional Fedora container tools and printer compatibility stacks.
* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-4
- Add VLC as a Fedora-backed catalogue application.
* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Refresh installed-state presentation and maintained provider catalogue.
* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 0.1-3
- Capture provider failures and present bounded technical diagnostics.
