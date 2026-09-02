Name:           proper-launchers
Version:        0.1
Release:        15%{?dist}
Summary:        Proper Linux launcher and window workflow defaults
License:        GPL-3.0-or-later
BuildArch:      x86_64
%global debug_package %{nil}
Requires:       coreutils
Requires:       kdialog
Requires:       libnotify
Requires:       plasma-discover
Requires:       plasma-systemsettings
Requires:       plasma-systemmonitor
Requires:       proper-apps >= 0.1-7
Requires:       proper-appearance >= 0.1-3
Requires:       proper-look-and-feel >= 0.1-23
Requires:       qt6-qttools
Requires:       spectacle
Requires:       systemd
Requires:       tesseract
Requires:       tesseract-langpack-eng
Requires:       util-linux-core
Requires:       wl-clipboard
Source0:        https://github.com/vicinaehq/vicinae/archive/01cd7cb4936d9cb14272091623da85e7c880f0dc.tar.gz
# SHA-256: ee4e80d6e69193820b294a43a008794d8761cda9914256c32aed3be091f5c0e3

%description
Proper Linux integration for the pinned Vicinae launcher, KDE shortcuts, and
the searchable shortcut reference. Vicinae is built from the official v0.24.0
commit against Fedora's Qt 6.11 packages, avoiding the private-ABI workaround
used by the prior build.

%prep
%setup -q -n vicinae-01cd7cb4936d9cb14272091623da85e7c880f0dc

%build
cmake --preset linux-release -B build -DCMAKE_INSTALL_PREFIX=%{_prefix} -DUSE_SYSTEM_CMARK_GFM=OFF -DUSE_SYSTEM_KF6=ON -DUSE_SYSTEM_QT_KEYCHAIN=OFF -DUSE_SYSTEM_LAYER_SHELL=ON -DTYPESCRIPT_EXTENSIONS=OFF -DINSTALL_NODE_MODULES=OFF -DVICINAE_NODE_RUNTIME_DOWNLOAD=OFF
cmake --build build --parallel

%install
DESTDIR=%{buildroot} cmake --install build
install -Dpm 0755 %{_sourcedir}/proper-launcher %{buildroot}%{_bindir}/proper-launcher
install -Dpm 0755 %{_sourcedir}/proper-arrange-workspace %{buildroot}%{_bindir}/proper-arrange-workspace
install -Dpm 0755 %{_sourcedir}/proper-tool %{buildroot}%{_bindir}/proper-tool
install -Dpm 0644 %{_sourcedir}/vicinae.service %{buildroot}%{_userunitdir}/vicinae.service
# Upstream's desktop entry starts the server but does not open its window.
# Replace it after cmake --install so every taskbar/menu activation goes
# through Proper's readiness-aware opener.
install -Dpm 0644 %{_sourcedir}/vicinae.desktop %{buildroot}%{_datadir}/applications/vicinae.desktop
install -Dpm 0644 %{_sourcedir}/proper-vicinae.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/proper-vicinae.svg
install -Dpm 0644 %{_sourcedir}/proper-vicinae-shortcut.desktop %{buildroot}%{_datadir}/applications/proper-vicinae-shortcut.desktop
install -Dpm 0644 %{_sourcedir}/proper-terminal-shortcut.desktop %{buildroot}%{_datadir}/applications/proper-terminal-shortcut.desktop
install -Dpm 0644 %{_sourcedir}/proper-shortcut-overview.desktop %{buildroot}%{_datadir}/applications/proper-shortcut-overview.desktop
install -Dpm 0644 %{_sourcedir}/proper-arrange-workspace.desktop %{buildroot}%{_datadir}/applications/proper-arrange-workspace.desktop
install -Dpm 0644 %{_sourcedir}/proper-shortcuts.desktop %{buildroot}%{_datadir}/applications/proper-shortcuts.desktop
install -Dpm 0644 %{_sourcedir}/settings.json %{buildroot}%{_sysconfdir}/skel/.config/vicinae/settings.json
install -Dpm 0644 %{_sourcedir}/kglobalshortcutsrc %{buildroot}%{_sysconfdir}/skel/.config/kglobalshortcutsrc
install -Dpm 0644 %{_sourcedir}/proper-shortcuts.md %{buildroot}%{_datadir}/doc/proper-launchers/proper-shortcuts.md
install -Dpm 0644 %{_sourcedir}/proper-shortcuts.html %{buildroot}%{_datadir}/doc/proper-launchers/proper-shortcuts.html
for script in %{_sourcedir}/vicinae-scripts/*.sh; do
    install -Dpm 0755 "$script" %{buildroot}%{_datadir}/vicinae/scripts/proper/"$(basename "$script")"
done

%files
%{_bindir}/vicinae
%{_bindir}/proper-launcher
%{_bindir}/proper-arrange-workspace
%{_bindir}/proper-tool
%{_libexecdir}/vicinae/
%{_userunitdir}/vicinae.service
%{_prefix}/lib/modules-load.d/vicinae.conf
%{_datadir}/applications/vicinae.desktop
%{_datadir}/applications/vicinae-url-handler.desktop
%{_datadir}/applications/proper-vicinae-shortcut.desktop
%{_datadir}/applications/proper-terminal-shortcut.desktop
%{_datadir}/applications/proper-shortcut-overview.desktop
%{_datadir}/applications/proper-arrange-workspace.desktop
%{_datadir}/applications/proper-shortcuts.desktop
%{_datadir}/vicinae/
%{_datadir}/icons/hicolor/512x512/apps/vicinae.png
%{_datadir}/icons/hicolor/scalable/apps/proper-vicinae.svg
%config(noreplace) %{_sysconfdir}/skel/.config/vicinae/settings.json
%config(noreplace) %{_sysconfdir}/skel/.config/kglobalshortcutsrc
%doc %{_datadir}/doc/proper-launchers/proper-shortcuts.md
%doc %{_datadir}/doc/proper-launchers/proper-shortcuts.html

%post
%systemd_user_post vicinae.service
systemctl --global enable vicinae.service >/dev/null 2>&1 || :

%changelog
* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-15
- Make the Meta summon shortcut dismiss Vicinae on a second press
- Register Meta+Return for Ghostty, Meta+/ for the shortcut pane, and single-modifier quadrant tiling
- Rebalance the four-cell launcher mark within its shelf target
- Document Meta+M as the reversible arrangement shortcut

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-14
- Replace the off-centre launcher dot with Proper's centred four-cell mark
- Bind a Meta tap as well as Meta+Space to Vicinae without startup feedback
- Document the reversible workspace-arrangement shortcut

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-13
- Require the Inter-based shared stylesheet used by the shortcut reference

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-12
- Style the shortcut reference from Proper's canonical design tokens
- Add the passive Start Here hub to the launcher favourites

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-11
- Add the generic Coding Agent action to Vicinae
- Route Appearance Settings to Proper's preview-first appearance control

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-10
- Replace the promoted search glyph with Proper's quiet white launcher dot
- Keep the Applications and Search name and tooltip as the pointer affordance

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-9
- Present Vicinae as the semantic Applications and Search pointer affordance
- Replace the upstream brand mark with the coherent Breeze search icon
- Enable and pin Vicinae's pointer-accessible Browse Apps view

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-8
- Add pointer and Vicinae paths for workspace layouts and desktop utilities
- Add a searchable shortcut reference and local region OCR action

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-7
- Promote Chromium in the seeded Vicinae favourites

* Sun Aug 30 2026 Proper Linux <proper@example.invalid> - 0.1-6
- Route the taskbar and application-menu entry through the reliable opener

* Sun Aug 30 2026 Proper Linux <proper@example.invalid> - 0.1-5
- Wait for Vicinae IPC readiness, open idempotently, and report startup failure

* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 0.1-4
- Seed versioned JSON settings with telemetry disabled and real favorites

* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 0.1-3
- Build official Vicinae v0.24.0 source against Fedora Qt 6.11

* Tue Aug 25 2026 Proper Linux <proper@example.invalid> - 0.1-1
- Add pinned Vicinae 0.24.0 and Proper launcher/window defaults
