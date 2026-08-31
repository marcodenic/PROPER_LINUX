Name:           proper-launchers
Version:        0.1
Release:        7%{?dist}
Summary:        Proper Linux launcher and window workflow defaults
License:        GPL-3.0-or-later
BuildArch:      x86_64
%global debug_package %{nil}
Requires:       coreutils
Requires:       libnotify
Requires:       systemd
Requires:       util-linux-core
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
install -Dpm 0644 %{_sourcedir}/vicinae.service %{buildroot}%{_userunitdir}/vicinae.service
# Upstream's desktop entry starts the server but does not open its window.
# Replace it after cmake --install so every taskbar/menu activation goes
# through Proper's readiness-aware opener.
install -Dpm 0644 %{_sourcedir}/vicinae.desktop %{buildroot}%{_datadir}/applications/vicinae.desktop
install -Dpm 0644 %{_sourcedir}/proper-vicinae-shortcut.desktop %{buildroot}%{_datadir}/applications/proper-vicinae-shortcut.desktop
install -Dpm 0644 %{_sourcedir}/settings.json %{buildroot}%{_sysconfdir}/skel/.config/vicinae/settings.json
install -Dpm 0644 %{_sourcedir}/kglobalshortcutsrc %{buildroot}%{_sysconfdir}/skel/.config/kglobalshortcutsrc
install -Dpm 0644 %{_sourcedir}/proper-shortcuts.md %{buildroot}%{_datadir}/doc/proper-launchers/proper-shortcuts.md

%files
%{_bindir}/vicinae
%{_bindir}/proper-launcher
%{_libexecdir}/vicinae/
%{_userunitdir}/vicinae.service
%{_prefix}/lib/modules-load.d/vicinae.conf
%{_datadir}/applications/vicinae.desktop
%{_datadir}/applications/vicinae-url-handler.desktop
%{_datadir}/applications/proper-vicinae-shortcut.desktop
%{_datadir}/vicinae/
%{_datadir}/icons/hicolor/512x512/apps/vicinae.png
%config(noreplace) %{_sysconfdir}/skel/.config/vicinae/settings.json
%config(noreplace) %{_sysconfdir}/skel/.config/kglobalshortcutsrc
%doc %{_datadir}/doc/proper-launchers/proper-shortcuts.md

%post
%systemd_user_post vicinae.service
systemctl --global enable vicinae.service >/dev/null 2>&1 || :

%changelog
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
