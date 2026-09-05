Name:           proper-defaults
Version:        0.1
Release:        37%{?dist}
Summary:        Proper Linux new-user KDE defaults
License:        GPL-3.0-or-later
BuildArch:      noarch
Requires:       chromium
Requires:       proper-look-and-feel >= 0.1-42
Requires:       proper-launchers >= 0.1-17
Requires:       proper-terminal >= 1.3.1-7
Requires:       proper-apps >= 0.1-12
Requires:       proper-appearance >= 0.1-10
Requires:       proper-agent-status >= 0.2-1
Requires:       python3
Requires:       /usr/bin/kscreen-doctor
Requires:       /usr/bin/qdbus-qt6
Requires:       /usr/bin/kreadconfig6
Requires:       /usr/bin/kwriteconfig6

%description
KDE configuration defaults. KDE reads the XDG copies as layered system
defaults, while Plasma's Global Theme creates the initial panel. User settings
remain higher-priority and are never replaced by package updates.

%changelog
* Sat Sep 05 2026 Proper Linux <proper@example.invalid> - 0.1-37
- Remove the inset window frame and contrasting Breeze outline by default

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-36
- Seed KWin's QEMU-only login output profile before the greeter starts
- Keep runtime display changes out of the login password field

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-35
- Keep Plasma Login Manager's supported Wayland session launcher intact
- Leave QEMU display adjustment to the review harness and first-run session

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-34
- Prepare live-user defaults before Plasma starts through the livesys hook
- Replace the repeated installer-icon cleanup with an XDG autostart override

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-33
- Replace duplicated skel and panel files with XDG and Global Theme defaults
- Run the legacy tooltip repair once through KDE's kconf_update mechanism
- Keep hardware-aware natural scrolling as the only per-user default helper

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-32
- Require the global status-shade and agent-meter package revision

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-31
- Make balanced halves the default reversible workspace arrangement on Meta+W
- Use native KWin tiles so dragging a shared edge resizes both neighbouring windows

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-30
- Store digital-clock appearance defaults in Plasma's real nested KConfig group
- Repair only the exact malformed numeric-date fallback from earlier Proper profiles

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-29
- Seed the Proper Breeze layer with the approved plain folder for Files
- Leave existing users' later icon-theme choices untouched

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-28
- Seed the maximum KWin blur recipe explicitly for new profiles
- Let the shelf use its Proper translucent and dense adaptive material states

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-27
- Let the optional agent meter seed its own native right-aligned Plasma panel
- Keep QEMU first-run and login review sessions at Full HD and 100 percent scale

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-26
- Seed the optional agent-usage card at the bottom-right for new Plasma accounts
- Preserve later widget moves, resizing, and removal as ordinary user choices

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-25
- Restore delayed status-area tooltips and task-window previews
- Repair only the former Proper Delay=0 default without overriding later choices
- Keep closed task launchers quiet while running applications expose previews

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-24
- Enable natural scrolling once for each new Plasma account without overriding later choices
- Disable password-wallet prompts only in the passwordless, ephemeral live account
- Move workspace arrangement to Meta+M so Meta+Z remains free for undo conventions

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
install -Dpm 0644 %{_sourcedir}/plasmarc %{buildroot}%{_sysconfdir}/xdg/plasmarc
install -Dpm 0644 %{_sourcedir}/dolphinrc %{buildroot}%{_sysconfdir}/xdg/dolphinrc
install -Dpm 0644 %{_sourcedir}/plasmashellrc %{buildroot}%{_sysconfdir}/xdg/plasmashellrc
install -Dpm 0644 %{_sourcedir}/ksplashrc %{buildroot}%{_sysconfdir}/xdg/ksplashrc
install -Dpm 0644 %{_sourcedir}/breezerc %{buildroot}%{_sysconfdir}/xdg/breezerc
install -Dpm 0644 %{_sourcedir}/kwinrc %{buildroot}%{_sysconfdir}/xdg/kwinrc
install -Dpm 0644 %{_sourcedir}/proper-workspace-arranger/metadata.json %{buildroot}%{_datadir}/kwin/scripts/proper-workspace-arranger/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-workspace-arranger/contents/code/main.js %{buildroot}%{_datadir}/kwin/scripts/proper-workspace-arranger/contents/code/main.js
install -Dpm 0755 %{_sourcedir}/proper-natural-scroll-default %{buildroot}%{_bindir}/proper-natural-scroll-default
install -Dpm 0644 %{_sourcedir}/proper-natural-scroll-default.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/proper-natural-scroll-default.desktop
install -Dpm 0644 %{_sourcedir}/proper-defaults.upd %{buildroot}%{_datadir}/kconf_update/proper-defaults.upd
install -Dpm 0755 %{_sourcedir}/proper-tooltip-default-repair %{buildroot}%{_datadir}/kconf_update/proper-tooltip-default-repair
install -Dpm 0755 %{_sourcedir}/proper-qemu-review-display %{buildroot}%{_bindir}/proper-qemu-review-display
install -Dpm 0644 %{_sourcedir}/proper-qemu-review-display.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/proper-qemu-review-display.desktop
install -Dpm 0644 %{_sourcedir}/20-proper-review-display.conf %{buildroot}%{_unitdir}/plasmalogin.service.d/20-proper-review-display.conf
install -Dpm 0644 %{_sourcedir}/kwalletrc-live %{buildroot}%{_datadir}/proper-linux/live/kwalletrc
install -Dpm 0644 %{_sourcedir}/liveinst-setup.desktop %{buildroot}%{_datadir}/proper-linux/live/liveinst-setup.desktop
install -Dpm 0644 %{_sourcedir}/proper-live-wallpaper.desktop %{buildroot}%{_datadir}/proper-linux/live/proper-live-wallpaper.desktop

%check
! grep -q '^\[Colors:' %{buildroot}%{_sysconfdir}/xdg/kdeglobals
grep -qx 'ColorScheme=Proper' %{buildroot}%{_sysconfdir}/xdg/kdeglobals
grep -qx 'ShellPackage=com.properlinux.desktop' %{buildroot}%{_sysconfdir}/xdg/plasmashellrc
grep -qx 'Id=proper-tooltip-delay-v2' %{buildroot}%{_datadir}/kconf_update/proper-defaults.upd
grep -qx 'Hidden=true' %{buildroot}%{_datadir}/proper-linux/live/liveinst-setup.desktop
grep -Fqx 'ExecStartPre=-/usr/bin/proper-qemu-review-display --prepare-login' %{buildroot}%{_unitdir}/plasmalogin.service.d/20-proper-review-display.conf
test ! -e %{buildroot}%{_sysconfdir}/skel/.config/kdeglobals
test ! -e %{buildroot}%{_sysconfdir}/skel/.config/plasma-org.kde.plasma.desktop-appletsrc

%files
%config(noreplace) %{_sysconfdir}/xdg/kdeglobals
%config(noreplace) %{_sysconfdir}/gtk-3.0/settings.ini
%config(noreplace) %{_sysconfdir}/gtk-4.0/settings.ini
%config(noreplace) %{_sysconfdir}/xdg/mimeapps.list
%config(noreplace) %{_sysconfdir}/xdg/plasmarc
%config(noreplace) %{_sysconfdir}/xdg/dolphinrc
%config(noreplace) %{_sysconfdir}/xdg/plasmashellrc
%config(noreplace) %{_sysconfdir}/xdg/ksplashrc
%config(noreplace) %{_sysconfdir}/xdg/kwinrc
%config(noreplace) %{_sysconfdir}/xdg/breezerc
%{_datadir}/kwin/scripts/proper-workspace-arranger/
%{_bindir}/proper-natural-scroll-default
%{_sysconfdir}/xdg/autostart/proper-natural-scroll-default.desktop
%{_datadir}/kconf_update/proper-defaults.upd
%{_datadir}/kconf_update/proper-tooltip-default-repair
%{_bindir}/proper-qemu-review-display
%{_sysconfdir}/xdg/autostart/proper-qemu-review-display.desktop
%{_unitdir}/plasmalogin.service.d/20-proper-review-display.conf
%{_datadir}/proper-linux/live/kwalletrc
%{_datadir}/proper-linux/live/liveinst-setup.desktop
%{_datadir}/proper-linux/live/proper-live-wallpaper.desktop
