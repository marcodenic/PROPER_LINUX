Name:           proper-look-and-feel
Version:        0.1
Release:        3%{?dist}
Summary:        Proper Linux visual assets
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later
BuildArch:      noarch
Requires:       plasma-workspace

%description
System-wide visual assets for the Proper Linux visual identity. Proper Blue
Hour is the default wallpaper, while Proper Horizon remains available as an
alternate. Both are installed in standard Plasma locations.

%install
install -Dpm 0644 %{_sourcedir}/proper-blue-hour.png %{buildroot}%{_datadir}/wallpapers/ProperBlueHour/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperBlueHour/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperBlueHour/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-horizon-dark.png %{buildroot}%{_datadir}/wallpapers/ProperHorizon/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperHorizon/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperHorizon/metadata.json
install -Dpm 0644 %{_sourcedir}/com.properlinux.dark.desktop/metadata.json %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.dark.desktop/metadata.json
install -Dpm 0644 %{_sourcedir}/com.properlinux.dark.desktop/contents/defaults %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.dark.desktop/contents/defaults
install -Dpm 0644 %{_sourcedir}/proper-wallpaper.conf %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
# Fedora 44 PLM reads the distro default from this exact file. Its README
# documents /etc/plasmalogin.conf as the administrator override and
# /usr/lib/plasmalogin/defaults.conf as the shipped default.
install -Dpm 0644 %{_sourcedir}/plasmalogin.conf %{buildroot}%{_datadir}/proper-linux/plasmalogin.conf
install -Dpm 0644 %{_sourcedir}/tokens.yaml %{buildroot}%{_datadir}/proper-linux/tokens.yaml
install -Dpm 0644 %{_sourcedir}/Proper.colors %{buildroot}%{_datadir}/color-schemes/Proper.colors

%files
%{_datadir}/wallpapers/ProperBlueHour/
%{_datadir}/wallpapers/ProperHorizon/
%{_datadir}/plasma/look-and-feel/com.properlinux.dark.desktop/
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
%{_datadir}/proper-linux/plasmalogin.conf
%{_datadir}/proper-linux/tokens.yaml
%{_datadir}/color-schemes/Proper.colors

%posttrans
# Fedora's kde-settings-plasmalogin owns defaults.conf. Apply the Proper
# distro default after the transaction without claiming that upstream file.
install -m 0644 %{_datadir}/proper-linux/plasmalogin.conf %{_prefix}/lib/plasmalogin/defaults.conf || :

%changelog
* Sun Aug 30 2026 Proper Linux <proper@example.invalid> - 0.1-3
- Add Proper Dark defaults and Blue Hour as the default visual identity
