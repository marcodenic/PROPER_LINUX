Name:           proper-welcome
Version:        0.1
Release:        12%{?dist}
Summary:        Proper Linux live-session welcome
License:        GPL-3.0-or-later
BuildArch:      x86_64
BuildRequires:  qt6-qtbase-devel
Requires:       anaconda-live
Requires:       proper-branding >= 0.1-4
Requires:       proper-look-and-feel >= 0.1-42
Requires:       proper-launchers >= 0.1-17

%description
A focused, pointer-accessible live-session choice between exploring the Proper
desktop and launching Fedora's maintained Anaconda installer, plus a passive
Start Here hub for the installed desktop.

%prep
cp %{_sourcedir}/main.cpp %{_sourcedir}/proper-welcome.pro .

%build
qmake6 CONFIG+=release proper-welcome.pro
make %{?_smp_mflags}

%install
install -Dpm 0755 proper-welcome %{buildroot}%{_bindir}/proper-welcome
install -Dpm 0755 %{_sourcedir}/proper-welcome-launch %{buildroot}%{_bindir}/proper-welcome-launch
install -Dpm 0644 %{_sourcedir}/proper-welcome.desktop %{buildroot}%{_datadir}/proper-linux/live/proper-welcome.desktop
install -Dpm 0644 %{_sourcedir}/proper-install.desktop %{buildroot}%{_datadir}/proper-linux/live/proper-install.desktop
install -Dpm 0644 %{_sourcedir}/proper-start.desktop %{buildroot}%{_datadir}/applications/proper-start.desktop

%files
%{_bindir}/proper-welcome
%{_bindir}/proper-welcome-launch
%{_datadir}/proper-linux/live/proper-welcome.desktop
%{_datadir}/proper-linux/live/proper-install.desktop
%{_datadir}/applications/proper-start.desktop

%changelog
* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-12
- Draw the live welcome atmosphere and wordmark from the shared semantic palette

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-11
- Show Meta+W for workspace arrangement and Meta+O for keyboard Overview

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-10
- Replace the welcome grid with a soft atmospheric blue-black backdrop
- Tighten the opening promise and reduce the introduction to two clear lines
- Promote the install choice before one quiet, unboxed shortcut row
- Remove duplicate live-session, close, and version chrome around the hero

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-9
- Surface the complete sub-3 GB live image as evidence of deliberate curation
- Explain that the lean image omits an office suite, duplicate apps or redundant packages without restricting the catalogue

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-8
- Explain Proper's Fedora foundation, curation, ethos, and workflow on arrival and in Start Here
- Replace rigid button tiles with a padded, scrollable, responsive editorial launchpad
- Add visible keycap hints and a compact Meta+/ shortcut overview pane

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-7
- Add obvious pointer cards for workspace arrangement and Vicinae search

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-6
- Require the Inter-based shared first-party UI token assets

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-5
- Add a passive Start Here hub for apps, appearance, updates, shortcuts, and support
- Consume the shared token-generated Proper widget styles

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-4
- Restore the approved welcome width and protect the headline line box from clipping

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-3
- Remove the visible Fedora footer, support the 640x480 fallback, and select
  the QEMU review mode before the welcome opens

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Inhibit idle locking and display sleep only while the live welcome is open

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-1
- Add the approved full-screen Try Proper or Install Proper arrival choice
- Keep the installer launch delegated to Fedora's maintained liveinst entrypoint
