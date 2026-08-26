Name:           proper-look-and-feel
Version:        0.1
Release:        1%{?dist}
Summary:        Proper Linux visual assets
License:        CC-BY-SA-4.0
BuildArch:      noarch
Requires:       plasma-workspace

%description
System-wide visual assets for the Proper Linux visual identity. The wallpaper
is deliberately installed in a standard Plasma location so desktop, lock
screen, and Plasma Login Manager can use the same asset.

%install
install -Dpm 0644 %{_sourcedir}/proper-horizon-dark.png %{buildroot}%{_datadir}/wallpapers/ProperHorizon/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperHorizon/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperHorizon/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-wallpaper.conf %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
# Fedora 44 PLM reads the distro default from this exact file. Its README
# documents /etc/plasmalogin.conf as the administrator override and
# /usr/lib/plasmalogin/defaults.conf as the shipped default.
install -Dpm 0644 %{_sourcedir}/plasmalogin.conf %{buildroot}%{_datadir}/proper-linux/plasmalogin.conf
install -Dpm 0644 %{_sourcedir}/tokens.yaml %{buildroot}%{_datadir}/proper-linux/tokens.yaml
install -Dpm 0644 %{_sourcedir}/Proper.colors %{buildroot}%{_datadir}/color-schemes/Proper.colors

%files
%{_datadir}/wallpapers/ProperHorizon/
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
%{_datadir}/proper-linux/plasmalogin.conf
%{_datadir}/proper-linux/tokens.yaml
%{_datadir}/color-schemes/Proper.colors

%posttrans
# Fedora's kde-settings-plasmalogin owns defaults.conf. Apply the Proper
# distro default after the transaction without claiming that upstream file.
install -m 0644 %{_datadir}/proper-linux/plasmalogin.conf %{_prefix}/lib/plasmalogin/defaults.conf || :
