Name:           proper-launchers
Version:        0.1
Release:        2%{?dist}
Summary:        Proper Linux launcher and window workflow defaults
License:        GPL-3.0-or-later
BuildArch:      x86_64
AutoReq:        no
%global debug_package %{nil}
Source0:        https://github.com/vicinaehq/vicinae/releases/download/v0.24.0/vicinae-linux-x86_64-v0.24.0.tar.gz
# SHA-256: 015a1ef2f8b23ea36a3f831a41de2d138f927cf45c987f62de3ec4add8dbafe7

%description
Proper Linux integration for the pinned Vicinae launcher, KDE shortcuts, and
the searchable shortcut reference. The upstream binary is redistributed
unchanged from its signed project release asset.

%prep
%setup -q -c

%install
install -Dpm 0755 ./bin/vicinae %{buildroot}%{_bindir}/vicinae
install -Dpm 0755 %{_sourcedir}/proper-launcher %{buildroot}%{_bindir}/proper-launcher
install -Dpm 0755 ./libexec/vicinae/* -t %{buildroot}%{_libexecdir}/vicinae
python3 %{_sourcedir}/qt-vicinae-version-patch.py %{buildroot}%{_libexecdir}/vicinae/vicinae-server
install -Dpm 0644 %{_sourcedir}/vicinae.service %{buildroot}%{_userunitdir}/vicinae.service
install -Dpm 0644 ./lib/modules-load.d/vicinae.conf %{buildroot}%{_prefix}/lib/modules-load.d/vicinae.conf
install -Dpm 0644 ./share/applications/vicinae.desktop %{buildroot}%{_datadir}/applications/vicinae.desktop
install -Dpm 0644 ./share/applications/vicinae-url-handler.desktop %{buildroot}%{_datadir}/applications/vicinae-url-handler.desktop
install -Dpm 0644 %{_sourcedir}/proper-vicinae-shortcut.desktop %{buildroot}%{_datadir}/applications/proper-vicinae-shortcut.desktop
cp -a ./share/vicinae %{buildroot}%{_datadir}/
cp -a ./share/icons %{buildroot}%{_datadir}/
install -Dpm 0644 %{_sourcedir}/vicinae.toml %{buildroot}%{_sysconfdir}/skel/.config/vicinae/vicinae.toml
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
%config(noreplace) %{_sysconfdir}/skel/.config/vicinae/vicinae.toml
%config(noreplace) %{_sysconfdir}/skel/.config/kglobalshortcutsrc
%doc %{_datadir}/doc/proper-launchers/proper-shortcuts.md

%post
%systemd_user_post vicinae.service
systemctl --global enable vicinae.service >/dev/null 2>&1 || :

%changelog
* Tue Aug 25 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Refresh package release for Phase 3 runtime verification

* Tue Aug 25 2026 Proper Linux <proper@example.invalid> - 0.1-1
- Add pinned Vicinae 0.24.0 and Proper launcher/window defaults
