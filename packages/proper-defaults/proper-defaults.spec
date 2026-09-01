Name:           proper-defaults
Version:        0.1
Release:        23%{?dist}
Summary:        Proper Linux new-user KDE defaults
License:        GPL-3.0-or-later
BuildArch:      noarch
Requires:       chromium
Requires:       proper-look-and-feel >= 0.1-23
Requires:       proper-launchers
Requires:       proper-terminal
Requires:       proper-apps
Requires:       proper-appearance >= 0.1-5

%description
KDE configuration defaults. KDE reads the XDG copies as system defaults and
the small skel copies initialise a live/installer-created account. They do not
overwrite an existing user's configuration.

%changelog
* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-23
- Make the fit-content shelf visibly about 560 pixels wide with an 86-pixel task-to-tray spacer

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-22
- Seed the wider Proper shelf with a fixed task-to-tray gap
- Move reversible workspace arrangement to Meta+Z

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-21
- Seed Inter across Plasma desktop, taskbar, menus, toolbars, titles, and GTK
- Keep JetBrains Mono limited to fixed-width KDE and terminal surfaces

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-20
- Seed the complete Proper application palette so KDE views start dark

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-19
- Select the Proper session splash for new, installed, and live users

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-18
- Select the Proper Horizon colour scheme for new desktop sessions

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-17
- Disable Plasma's hover-triggered informational tooltips by default

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-16
- Use a human-readable month and day in the taskbar without a redundant year

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-15
- Integrate the approved Proper Plasma Style with the workspace arranger

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-14
- Add the reversible, output-aware Proper workspace arranger KWin script

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-13
- Pin Ghostty's own desktop identity so running windows group with its launcher

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-12
- Bind the seeded floating translucent panel view to the Proper ShellPackage

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-11
- Seed the Proper ShellPackage containment config explicitly for persistence

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-10
- Require the polished Proper Appearance gallery revision

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-9
- Require the visual wallpaper gallery for every Proper desktop

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-8
- Promote Chromium through KDE and XDG defaults for new and live users

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-7
- Select the Proper Plasma shell package for the approved lock screen

* Sun Aug 30 2026 Proper Linux <proper@example.invalid> - 0.1-6
- Replace the dropdown prototype with an ordinary pinned Ghostty launcher

* Sun Aug 30 2026 Proper Linux <proper@example.invalid> - 0.1-5
- Default to the Proper Dark look-and-feel and Breeze dark translucent shell

* Tue Aug 25 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Bump defaults package for Phase 3 runtime verification and ISO integration

* Tue Aug 25 2026 Proper Linux <proper@example.invalid> - 0.1-1
- Add KDE and Vicinae defaults for new users

%install
install -Dpm 0644 %{_sourcedir}/kdeglobals %{buildroot}%{_sysconfdir}/xdg/kdeglobals
install -Dpm 0644 %{_sourcedir}/gtk-settings.ini %{buildroot}%{_sysconfdir}/gtk-3.0/settings.ini
install -Dpm 0644 %{_sourcedir}/gtk-settings.ini %{buildroot}%{_sysconfdir}/gtk-4.0/settings.ini
install -Dpm 0644 %{_sourcedir}/mimeapps.list %{buildroot}%{_sysconfdir}/xdg/mimeapps.list
install -Dpm 0644 %{_sourcedir}/plasma-org.kde.plasma.desktop-appletsrc %{buildroot}%{_sysconfdir}/xdg/plasma-org.kde.plasma.desktop-appletsrc
install -Dpm 0644 %{_sourcedir}/plasma-org.kde.plasma.desktop-appletsrc %{buildroot}%{_sysconfdir}/xdg/plasma-com.properlinux.desktop-appletsrc
install -Dpm 0644 %{_sourcedir}/plasmarc %{buildroot}%{_sysconfdir}/xdg/plasmarc
install -Dpm 0644 %{_sourcedir}/kdeglobals %{buildroot}%{_sysconfdir}/skel/.config/kdeglobals
install -Dpm 0644 %{_sourcedir}/gtk-settings.ini %{buildroot}%{_sysconfdir}/skel/.config/gtk-3.0/settings.ini
install -Dpm 0644 %{_sourcedir}/gtk-settings.ini %{buildroot}%{_sysconfdir}/skel/.config/gtk-4.0/settings.ini
install -Dpm 0644 %{_sourcedir}/mimeapps.list %{buildroot}%{_sysconfdir}/skel/.config/mimeapps.list
install -Dpm 0644 %{_sourcedir}/plasma-org.kde.plasma.desktop-appletsrc %{buildroot}%{_sysconfdir}/skel/.config/plasma-org.kde.plasma.desktop-appletsrc
install -Dpm 0644 %{_sourcedir}/plasma-org.kde.plasma.desktop-appletsrc %{buildroot}%{_sysconfdir}/skel/.config/plasma-com.properlinux.desktop-appletsrc
install -Dpm 0644 %{_sourcedir}/plasmarc %{buildroot}%{_sysconfdir}/skel/.config/plasmarc
install -Dpm 0644 %{_sourcedir}/dolphinrc %{buildroot}%{_sysconfdir}/xdg/dolphinrc
install -Dpm 0644 %{_sourcedir}/plasmashellrc %{buildroot}%{_sysconfdir}/xdg/plasmashellrc
install -Dpm 0644 %{_sourcedir}/plasmashellrc %{buildroot}%{_sysconfdir}/skel/.config/plasmashellrc
install -Dpm 0644 %{_sourcedir}/ksplashrc %{buildroot}%{_sysconfdir}/xdg/ksplashrc
install -Dpm 0644 %{_sourcedir}/ksplashrc %{buildroot}%{_sysconfdir}/skel/.config/ksplashrc
install -Dpm 0644 %{_sourcedir}/kwinrc %{buildroot}%{_sysconfdir}/xdg/kwinrc
install -Dpm 0644 %{_sourcedir}/proper-workspace-arranger/metadata.json %{buildroot}%{_datadir}/kwin/scripts/proper-workspace-arranger/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-workspace-arranger/contents/code/main.js %{buildroot}%{_datadir}/kwin/scripts/proper-workspace-arranger/contents/code/main.js
install -Dpm 0644 %{_sourcedir}/dolphinrc %{buildroot}%{_sysconfdir}/skel/.config/dolphinrc
install -Dpm 0755 %{_sourcedir}/proper-live-defaults %{buildroot}%{_bindir}/proper-live-defaults
install -Dpm 0644 %{_sourcedir}/proper-live-defaults.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/proper-live-defaults.desktop

%files
%config(noreplace) %{_sysconfdir}/xdg/kdeglobals
%config(noreplace) %{_sysconfdir}/gtk-3.0/settings.ini
%config(noreplace) %{_sysconfdir}/gtk-4.0/settings.ini
%config(noreplace) %{_sysconfdir}/xdg/mimeapps.list
%config(noreplace) %{_sysconfdir}/xdg/plasma-org.kde.plasma.desktop-appletsrc
%config(noreplace) %{_sysconfdir}/xdg/plasma-com.properlinux.desktop-appletsrc
%config(noreplace) %{_sysconfdir}/xdg/plasmarc
%config(noreplace) %{_sysconfdir}/skel/.config/kdeglobals
%config(noreplace) %{_sysconfdir}/skel/.config/gtk-3.0/settings.ini
%config(noreplace) %{_sysconfdir}/skel/.config/gtk-4.0/settings.ini
%config(noreplace) %{_sysconfdir}/skel/.config/mimeapps.list
%config(noreplace) %{_sysconfdir}/skel/.config/plasma-org.kde.plasma.desktop-appletsrc
%config(noreplace) %{_sysconfdir}/skel/.config/plasma-com.properlinux.desktop-appletsrc
%config(noreplace) %{_sysconfdir}/skel/.config/plasmarc
%config(noreplace) %{_sysconfdir}/xdg/dolphinrc
%config(noreplace) %{_sysconfdir}/xdg/plasmashellrc
%config(noreplace) %{_sysconfdir}/xdg/ksplashrc
%config(noreplace) %{_sysconfdir}/xdg/kwinrc
%{_datadir}/kwin/scripts/proper-workspace-arranger/
%config(noreplace) %{_sysconfdir}/skel/.config/plasmashellrc
%config(noreplace) %{_sysconfdir}/skel/.config/ksplashrc
%config(noreplace) %{_sysconfdir}/skel/.config/dolphinrc
%{_bindir}/proper-live-defaults
%{_sysconfdir}/xdg/autostart/proper-live-defaults.desktop
