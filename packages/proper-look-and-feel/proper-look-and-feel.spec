Name:           proper-look-and-feel
Version:        0.1
Release:        29%{?dist}
Summary:        Proper Linux visual assets
License:        CC-BY-SA-4.0 AND LGPL-3.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later
BuildArch:      noarch
BuildRequires:  libxml2
BuildRequires:  python3
Provides:       system-backgrounds-kde
Requires:       plasma-workspace >= 6.7
Requires:       proper-branding
Requires:       google-noto-sans-fonts
Requires:       rsms-inter-fonts = 4.1-3%{?dist}

%description
System-wide visual assets for the Proper Linux visual identity. Proper Blue
Hour remains the default wallpaper. Eight Proper landscape photographs and two
rally treatments join three PM-selected KDE wallpapers in a compact, fully
attributed Plasma gallery.

%build
python3 %{_sourcedir}/generate-ui-assets.py %{_sourcedir}/tokens.yaml %{_builddir}/proper-ui
python3 %{_sourcedir}/generate-plasma-controls.py %{_sourcedir}/tokens.yaml %{_builddir}/proper-controls

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
install -Dpm 0644 %{_sourcedir}/proper-rally-blue-hour.png %{buildroot}%{_datadir}/wallpapers/ProperRallyBlueHour/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperRallyBlueHour/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperRallyBlueHour/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-rally-night-flight.png %{buildroot}%{_datadir}/wallpapers/ProperRallyNightFlight/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperRallyNightFlight/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperRallyNightFlight/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-floating-falls.png %{buildroot}%{_datadir}/wallpapers/ProperFloatingFalls/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperFloatingFalls/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperFloatingFalls/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-terraced-dawn.png %{buildroot}%{_datadir}/wallpapers/ProperTerracedDawn/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperTerracedDawn/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperTerracedDawn/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-glacial-arch.png %{buildroot}%{_datadir}/wallpapers/ProperGlacialArch/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperGlacialArch/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperGlacialArch/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-highland-blue-hour.png %{buildroot}%{_datadir}/wallpapers/ProperHighlandBlueHour/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperHighlandBlueHour/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperHighlandBlueHour/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-highland-sunrise.png %{buildroot}%{_datadir}/wallpapers/ProperHighlandSunrise/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperHighlandSunrise/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperHighlandSunrise/metadata.json
install -Dpm 0644 %{_sourcedir}/proper-salt-flat-station.png %{buildroot}%{_datadir}/wallpapers/ProperSaltFlatStation/contents/images/1920x1080.png
install -Dpm 0644 %{_sourcedir}/ProperSaltFlatStation/metadata.json %{buildroot}%{_datadir}/wallpapers/ProperSaltFlatStation/metadata.json
install -Dpm 0644 %{_sourcedir}/com.properlinux.dark.desktop/metadata.json %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.dark.desktop/metadata.json
install -Dpm 0644 %{_sourcedir}/com.properlinux.dark.desktop/contents/defaults %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.dark.desktop/contents/defaults
install -Dpm 0644 %{_sourcedir}/com.properlinux.light.desktop/metadata.json %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.light.desktop/metadata.json
install -Dpm 0644 %{_sourcedir}/com.properlinux.light.desktop/contents/defaults %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.light.desktop/contents/defaults
install -Dpm 0644 %{_sourcedir}/com.properlinux.midnight.desktop/metadata.json %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.midnight.desktop/metadata.json
install -Dpm 0644 %{_sourcedir}/com.properlinux.midnight.desktop/contents/defaults %{buildroot}%{_datadir}/plasma/look-and-feel/com.properlinux.midnight.desktop/contents/defaults
for theme in com.properlinux.dark.desktop com.properlinux.light.desktop com.properlinux.midnight.desktop; do
  install -Dpm 0644 %{_sourcedir}/Splash.qml \
    "%{buildroot}%{_datadir}/plasma/look-and-feel/$theme/contents/splash/Splash.qml"
done
install -Dpm 0644 %{_sourcedir}/proper-wallpaper.conf %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
# Fedora 44 PLM reads the distro default from this exact file. Its README
# documents /etc/plasmalogin.conf as the administrator override and
# /usr/lib/plasmalogin/defaults.conf as the shipped default.
install -Dpm 0644 %{_sourcedir}/plasmalogin.conf %{buildroot}%{_datadir}/proper-linux/plasmalogin.conf
install -Dpm 0644 %{_sourcedir}/tokens.yaml %{buildroot}%{_datadir}/proper-linux/tokens.yaml
install -d %{buildroot}%{_datadir}/proper-linux/ui
install -pm 0644 %{_builddir}/proper-ui/* %{buildroot}%{_datadir}/proper-linux/ui/
install -Dpm 0644 %{_sourcedir}/proper/colors %{buildroot}%{_datadir}/color-schemes/Proper.colors
install -Dpm 0644 %{_sourcedir}/ProperLight.colors %{buildroot}%{_datadir}/color-schemes/ProperLight.colors
install -Dpm 0644 %{_sourcedir}/ProperMidnight.colors %{buildroot}%{_datadir}/color-schemes/ProperMidnight.colors
style_root=%{buildroot}%{_datadir}/plasma/desktoptheme/proper
install -Dpm 0644 %{_sourcedir}/proper/metadata.json "$style_root/metadata.json"
install -Dpm 0644 %{_sourcedir}/proper/colors "$style_root/colors"
install -Dpm 0644 %{_sourcedir}/proper/dialogs/background.svg "$style_root/dialogs/background.svg"
install -Dpm 0644 %{_sourcedir}/proper/widgets/panel-background.svg "$style_root/widgets/panel-background.svg"
install -Dpm 0644 %{_sourcedir}/proper/widgets/plasmoidheading.svg "$style_root/widgets/plasmoidheading.svg"
install -Dpm 0644 %{_sourcedir}/proper/widgets/tasks.svg "$style_root/widgets/tasks.svg"
# Keep all five system applets on their upstream QML and RPM update path.
# These generated files use Plasma's supported Style element contract only.
for asset in button line lineedit listitem slider switch tabbar viewitem; do
  install -Dpm 0644 "%{_builddir}/proper-controls/$asset.svg" "$style_root/widgets/$asset.svg"
done
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
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/updates/01-refine-proper-panel.js "$shell_root/contents/updates/01-refine-proper-panel.js"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/updates/02-expand-proper-panel.js "$shell_root/contents/updates/02-expand-proper-panel.js"

%check
# Proper's rounded shell surfaces use a mask-composed centre and nine neutral
# slices to stop Plasma from exposing rectangular contrast or fallback-shadow
# layers. Keep the check here for builds outside the repository wrapper.
for asset in \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/translucentbackground.svg; do
  xmllint --noout "$asset"
  for element in \
    center top bottom left right \
    topleft topright bottomleft bottomright \
    mask-center mask-top mask-bottom mask-left mask-right \
    mask-topleft mask-topright mask-bottomleft mask-bottomright; do
    test "$(xmllint --xpath "count(//*[@id = '$element'])" "$asset")" = 1
  done
  shadow_selector="//*[starts-with(@id, 'shadow-') and not(starts-with(@id, 'shadow-hint-'))]"
  test "$(xmllint --xpath "count($shadow_selector)" "$asset")" = 9
  test "$(xmllint --xpath "count(${shadow_selector}[@fill-opacity and number(@fill-opacity) <= 0.001])" "$asset")" = 9
  test "$(xmllint --xpath "count(//*[@id = 'hint-compose-over-border'])" "$asset")" = 1
done
panel_radius=$(sed -n "s/^radius: {panel: \([0-9][0-9]*\),.*/\1/p" \
  %{buildroot}%{_datadir}/proper-linux/tokens.yaml)
asset_radius=$(xmllint --xpath "string(//*[@id='top']/*[1]/@height)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg)
mask_radius=$(xmllint --xpath "string(//*[@id='mask-top']/@height)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg)
test -n "$panel_radius"
test "$panel_radius" = "$asset_radius"
test "$panel_radius" = "$mask_radius"

# Proper task states must not fall through to Breeze's filled blue frames.
task_asset=%{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/tasks.svg
xmllint --noout "$task_asset"
for state in normal focus hover minimized attention progress; do
  for slice in center top bottom left right topleft topright bottomleft bottomright; do
    test "$(xmllint --xpath "count(//*[@id = '$state-$slice'])" "$task_asset")" = 1
  done
done
test "$(xmllint --xpath "count(//*[@id = 'focus-bottom']//*[contains(@class, 'ColorScheme-ButtonFocus')])" "$task_asset")" = 1
test "$(xmllint --xpath "count(//*[@id = 'normal-bottom']//*[contains(@class, 'ColorScheme-Text')])" "$task_asset")" = 1

# The system surfaces are a Plasma Style, not applet forks. Validate the
# generated supported control payload independently of the upstream QML.
for asset in button line lineedit listitem slider switch tabbar viewitem; do
  control_asset=%{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/$asset.svg
  xmllint --noout "$control_asset"
  test "$(xmllint --xpath "count(//*[@id = 'current-color-scheme'])" "$control_asset")" = 1
done
test "$(xmllint --xpath "count(//*[@id = 'pressed-center'])" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/listitem.svg)" = 1
test "$(xmllint --xpath "count(//*[@id = 'selected-center'])" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/viewitem.svg)" = 1
test "$(xmllint --xpath "count(//*[@id = 'active-center'])" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/switch.svg)" = 1
test "$(xmllint --xpath "count(//*[@id = 'groove-highlight-center'])" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/slider.svg)" = 1

%files
%{_datadir}/wallpapers/ProperBlueHour/
%{_datadir}/wallpapers/ProperHorizon/
%{_datadir}/wallpapers/Path/
%{_datadir}/wallpapers/Volna/
%{_datadir}/wallpapers/summer_1am/
%{_datadir}/wallpapers/ProperRallyBlueHour/
%{_datadir}/wallpapers/ProperRallyNightFlight/
%{_datadir}/wallpapers/ProperFloatingFalls/
%{_datadir}/wallpapers/ProperTerracedDawn/
%{_datadir}/wallpapers/ProperGlacialArch/
%{_datadir}/wallpapers/ProperHighlandBlueHour/
%{_datadir}/wallpapers/ProperHighlandSunrise/
%{_datadir}/wallpapers/ProperSaltFlatStation/
%{_datadir}/plasma/look-and-feel/com.properlinux.dark.desktop/
%{_datadir}/plasma/look-and-feel/com.properlinux.light.desktop/
%{_datadir}/plasma/look-and-feel/com.properlinux.midnight.desktop/
%{_datadir}/plasma/desktoptheme/proper/
%{_datadir}/plasma/shells/com.properlinux.desktop/
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
%{_datadir}/proper-linux/plasmalogin.conf
%{_datadir}/proper-linux/tokens.yaml
%{_datadir}/proper-linux/ui/
%{_datadir}/color-schemes/Proper.colors
%{_datadir}/color-schemes/ProperLight.colors
%{_datadir}/color-schemes/ProperMidnight.colors
%license %{_licensedir}/%{name}/CC-BY-SA-4.0.txt
%license %{_licensedir}/%{name}/LGPL-3.0-only.txt
%license %{_licensedir}/%{name}/GPL-2.0-or-later.txt
%license %{_licensedir}/%{name}/GPL-3.0-or-later.txt

%posttrans
# Fedora's kde-settings-plasmalogin owns defaults.conf. Apply the Proper
# distro default after the transaction without claiming that upstream file.
install -m 0644 %{_datadir}/proper-linux/plasmalogin.conf %{_prefix}/lib/plasmalogin/defaults.conf || :

%changelog
* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-29
- Add the PM-approved photographic Salt-Flat Station wallpaper
- Keep Proper Blue Hour as the default while expanding the gallery to thirteen choices

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-28
- Add the PM-approved photographic Highland Blue Hour and Highland Sunrise wallpapers
- Preserve Proper Blue Hour as the default while expanding the native Plasma gallery to twelve choices

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-27
- Promote all five PM-reviewed wallpaper concepts into the native Plasma gallery
- Keep Proper Blue Hour as the system default while exposing both rally treatments
- Replace the abstract Light background with the approved photographic Alpine Morning

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-26
- Centre the approved fixed-width soft-glass lock password capsule
- Enlarge and centre password dots without adding reveal or submit icons

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-25
- Restore Breeze-compatible switch geometry for Networks and Airplane Mode
- Give task indicators one crisp rounded line or dot and fix combo-box endcaps
- Increase panel and popup translucency while retaining readable owned surfaces

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-24
- Restyle upstream Plasma system applets through supported control assets only
- Keep network, Bluetooth, audio, display, brightness, and power QML untouched

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-23
- Enforce the fit-content shelf's visual floor through its fixed task-to-tray spacer

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-22
- Raise the legacy Proper shelf minimum to 560 pixels without overriding user widths
- Keep a fixed gap between application tasks and the system tray

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-21
- Make Inter 4 the canonical first-party and lock-screen UI family
- Retain Noto Sans as the explicit fallback in generated Qt and web styles

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-20
- Generate shared Qt and web styles directly from the canonical design tokens

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-19
- Implement the approved active-line and running-dot task states without blue fills
- Restore symmetric shelf end spacing and a Proper-branded session splash
- Reveal the lock-screen authentication controls on a background click

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-18
- Package the actual Proper Dark palette as the default application colour scheme
- Remove the obsolete light palette that was incorrectly installed as Proper Dark

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-17
- Add three curated, previewable Proper desktop styles without changing the shell layout
- Align the default, light, and midnight colour schemes to Proper Horizon tokens

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-16
- Reduce the shelf corner radius from 18 pixels to 16 pixels
- Bump the Plasma Style version so upgraded systems invalidate cached SVGs

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-15
- Refine the shelf with softer glass, restrained continuous edges, and more end space
- Migrate the stock clock from numeric dates to a human-readable month and day
- Bump the Plasma Style version so upgraded systems invalidate cached SVGs

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-14
- Mask the translucent contrast and blur layer to every rounded shell surface
- Add package checks that prevent rectangular compositor regions returning

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-13
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
