Name:           proper-look-and-feel
Version:        0.1
Release:        12%{?dist}
Summary:        Proper Linux visual assets
License:        CC-BY-SA-4.0 AND LGPL-3.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later
BuildArch:      noarch
BuildRequires:  libxml2
Provides:       system-backgrounds-kde
Requires:       plasma-workspace >= 6.7

%description
System-wide visual assets for the Proper Linux visual identity. Proper Blue
Hour is the default wallpaper. Proper Horizon and the three PM-selected KDE
wallpapers are installed as a compact, fully attributed Plasma gallery.

%install
install -Dpm 0644 %{_sourcedir}/proper-blue-hour.png %{buildroot}%{_datadir}/wallpapers/ProperBlueHour/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperBlueHour/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperBlueHour/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-horizon-dark.png %{buildroot}%{_datadir}/wallpapers/ProperHorizon/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperHorizon/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperHorizon/metadata.json
install -Dpm 0644 %{_sourcedir}/path.jpg %{buildroot}%{_datadir}/wallpapers/Path/contents/images/2560x1600.jpg
install -Dpm 0644 %{_sourcedir}/Path/metadata.json %{buildroot}%{_datadir}/wallpapers/Path/metadata.json
install -Dpm 0644 %{_sourcedir}/volna.jpg %{buildroot}%{_datadir}/wallpapers/Volna/contents/images/5120x2880.jpg
install -Dpm 0644 %{_sourcedir}/Volna/metadata.json %{buildroot}%{_datadir}/wallpapers/Volna/metadata.json
install -Dpm 0644 %{_sourcedir}/summer-1am.jpg %{buildroot}%{_datadir}/wallpapers/summer_1am/contents/images/2560x1600.jpg
install -Dpm 0644 %{_sourcedir}/summer_1am/metadata.json %{buildroot}%{_datadir}/wallpapers/summer_1am/metadata.json
install -Dpm 0644 %{_sourcedir}/com.properlinux.dark.desktop/metadata.json %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.dark.desktop/metadata.json
install -Dpm 0644 %{_sourcedir}/com.properlinux.dark.desktop/contents/defaults %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.dark.desktop/contents/defaults
install -Dpm 0644 %{_sourcedir}/proper-wallpaper.conf %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
# Fedora 44 PLM reads the distro default from this exact file. Its README
# documents /etc/plasmalogin.conf as the administrator override and
# /usr/lib/plasmalogin/defaults.conf as the shipped default.
install -Dpm 0644 %{_sourcedir}/plasmalogin.conf %{buildroot}%{_datadir}/proper-linux/plasmalogin.conf
install -Dpm 0644 %{_sourcedir}/tokens.yaml %{buildroot}%{_datadir}/proper-linux/tokens.yaml
install -Dpm 0644 %{_sourcedir}/Proper.colors %{buildroot}%{_datadir}/color-schemes/Proper.colors
style_root=%{buildroot}%{_datadir}/plasma/desktoptheme/proper
install -Dpm 0644 %{_sourcedir}/proper/metadata.json "$style_root/metadata.json"
install -Dpm 0644 %{_sourcedir}/proper/colors "$style_root/colors"
install -Dpm 0644 %{_sourcedir}/proper/dialogs/background.svg "$style_root/dialogs/background.svg"
install -Dpm 0644 %{_sourcedir}/proper/widgets/panel-background.svg "$style_root/widgets/panel-background.svg"
install -Dpm 0644 %{_sourcedir}/proper/widgets/plasmoidheading.svg "$style_root/widgets/plasmoidheading.svg"
# Notifications, tooltips, and workspace OSDs use the same approved surface
# recipe. Everything else remains an explicit Breeze fallback.
install -Dpm 0644 %{_sourcedir}/proper/dialogs/background.svg "$style_root/widgets/tooltip.svg"
install -Dpm 0644 %{_sourcedir}/proper/dialogs/background.svg "$style_root/widgets/translucentbackground.svg"
install -Dpm 0644 %{_sourcedir}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}%{_licensedir}/%{name}/CC-BY-SA-4.0.txt
install -Dpm 0644 %{_sourcedir}/LICENSES/LGPL-3.0-only.txt %{buildroot}%{_licensedir}/%{name}/LGPL-3.0-only.txt
install -Dpm 0644 %{_sourcedir}/LICENSES/GPL-2.0-or-later.txt %{buildroot}%{_licensedir}/%{name}/GPL-2.0-or-later.txt
install -Dpm 0644 %{_sourcedir}/LICENSES/GPL-3.0-or-later.txt %{buildroot}%{_licensedir}/%{name}/GPL-3.0-or-later.txt

# Plasma exposes the lock screen through its supported ShellPackage extension
# point. The package metadata names Fedora's active desktop shell as its
# fallback, so Proper owns only lockscreen QML and upstream fixes keep landing.
shell_root=%{buildroot}%{_datadir}/plasma/shells/com.properlinux.desktop
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/metadata.json "$shell_root/metadata.json"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/LockScreen.qml "$shell_root/contents/lockscreen/LockScreen.qml"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/LockScreenUi.qml "$shell_root/contents/lockscreen/LockScreenUi.qml"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/PasswordSync.qml "$shell_root/contents/lockscreen/PasswordSync.qml"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/qmldir "$shell_root/contents/lockscreen/qmldir"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/updates/00-ensure-proper-panel.js "$shell_root/contents/updates/00-ensure-proper-panel.js"

%check
# Proper's rounded shell surfaces must not regain unmasked rectangular shadow
# slices when this spec is built outside the repository's normal wrapper.
for asset in \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/translucentbackground.svg; do
  xmllint --noout "$asset"
  test "$(xmllint --xpath "count(//*[starts-with(@id, 'shadow-')])" "$asset")" = 0
done

%files
%{_datadir}/wallpapers/ProperBlueHour/
%{_datadir}/wallpapers/ProperHorizon/
%{_datadir}/wallpapers/Path/
%{_datadir}/wallpapers/Volna/
%{_datadir}/wallpapers/summer_1am/
%{_datadir}/plasma/look-and-feel/com.properlinux.dark.desktop/
%{_datadir}/plasma/desktoptheme/proper/
%{_datadir}/plasma/shells/com.properlinux.desktop/
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
%{_datadir}/proper-linux/plasmalogin.conf
%{_datadir}/proper-linux/tokens.yaml
%{_datadir}/color-schemes/Proper.colors
%license %{_licensedir}/%{name}/CC-BY-SA-4.0.txt
%license %{_licensedir}/%{name}/LGPL-3.0-only.txt
%license %{_licensedir}/%{name}/GPL-2.0-or-later.txt
%license %{_licensedir}/%{name}/GPL-3.0-or-later.txt

%posttrans
# Fedora's kde-settings-plasmalogin owns defaults.conf. Apply the Proper
# distro default after the transaction without claiming that upstream file.
install -m 0644 %{_datadir}/proper-linux/plasmalogin.conf %{_prefix}/lib/plasmalogin/defaults.conf || :

%changelog
* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-12
- Remove square shadow frames from the panel and shared shell surfaces
- Retain depth through translucency, blur, and restrained rounded edges
- Bump the Plasma Style version so upgraded systems invalidate cached SVGs

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-11
- Add the approved narrow Proper Plasma Style for shell surfaces
- Use charcoal popup, panel, heading, tooltip, and OSD assets with Breeze fallback

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-10
- Match the panel's Ghostty launcher to the application's Wayland identity

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-9
- Make the one-time panel seed match Proper's curated translucent panel

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-8
- Seed the upstream Plasma panel once for the Proper ShellPackage layout store

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-7
- Ship full licence texts for the curated artwork and lock-screen QML

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-6
- Provide Fedora's system-backgrounds-kde capability from Proper artwork

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-5
- Package the five approved wallpapers as the native Plasma gallery
- Preserve upstream Path, Volna, and summer_1am attribution and licences

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-4
- Add the approved minimal lock screen through Plasma's ShellPackage API

* Sun Aug 30 2026 Proper Linux <proper@example.invalid> - 0.1-3
- Add Proper Dark defaults and Blue Hour as the default visual identity
