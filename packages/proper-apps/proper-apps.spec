Name: proper-apps
Version: 0.1
Release: 15%{?dist}
Summary: Proper Linux curated application catalogue
License: GPL-3.0-or-later
BuildRequires: qt6-qtbase-devel
BuildRequires: kf6-kwindowsystem-devel
Requires: flatpak
Requires: kdialog
Requires: polkit
Requires: proper-terminal >= 1.3.1-7
Requires: proper-look-and-feel >= 0.1-62
%description
Small catalogue front end delegating installs to Fedora, Flatpak, and official vendor paths.
%prep
cp %{_sourcedir}/main.cpp %{_sourcedir}/proper-apps.pro .
cp %{_sourcedir}/../proper-look-and-feel/proper-action-button.h %{_sourcedir}/../proper-look-and-feel/proper-material-window.h .

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
* Sat Sep 05 2026 Proper Linux <proper@example.invalid> - 0.1-15
- Introduce native frosted navigation with solid content and a solid fallback

* Sat Sep 05 2026 Proper Linux <proper@example.invalid> - 0.1-14
- Refine app layout, native keyboard actions and everyday navigation

* Sat Sep 05 2026 Proper Linux <proper@example.invalid> - 0.1-13
- Present three optional favourites above the full searchable catalogue

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-12
- Use the active semantic selection palette for generated fallback artwork

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-11
- Preflight offline and critically low-space installs with actionable messages
- Identify network, disk, missing-package, and stale-provider failures in plain language
- Explain the live session's temporary, capacity-limited application storage

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-10
- Show authentication, download, install, and configuration phases explicitly
- Reconcile catalogue state after every provider result, including partial success
- Distinguish authorization cancellation, missing results, and configuration errors

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-9
- Require the Inter-based shared first-party UI token assets

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-8
- Use the shared token-generated Proper widget style and first-party icon
- Keep Recommended decisive while retaining the broad categorised catalogue

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
