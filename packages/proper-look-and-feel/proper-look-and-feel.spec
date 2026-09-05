Name:           proper-look-and-feel
Version:        0.1
Release:        56%{?dist}
Summary:        Proper Linux visual assets
License:        CC-BY-SA-4.0 AND LGPL-3.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later
BuildArch:      noarch
BuildRequires:  libxml2
BuildRequires:  python3
BuildRequires:  python3-pyside6
Provides:       system-backgrounds-kde
Requires:       plasma-workspace >= 6.7
Requires:       proper-branding >= 0.1-4
Requires:       aurorae >= 6.7.4
Requires:       breeze-icon-theme
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
python3 %{_sourcedir}/generate-panel-material.py %{_sourcedir}/tokens.yaml %{_builddir}/proper-panel
python3 %{_sourcedir}/generate-semantic-assets.py %{_sourcedir}/tokens.yaml %{_builddir}/proper-semantic

%install
python3 %{_sourcedir}/generate-window-decoration.py %{_sourcedir}/tokens.yaml %{buildroot}%{_datadir}/aurorae/themes
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
  install -Dpm 0644 %{_builddir}/proper-semantic/ProperTokens.qml \
    "%{buildroot}%{_datadir}/plasma/look-and-feel/$theme/contents/splash/ProperTokens.qml"
  install -Dpm 0644 %{_sourcedir}/proper-desktop-layout.js \
    "%{buildroot}%{_datadir}/plasma/look-and-feel/$theme/contents/layouts/org.kde.plasma.desktop-layout.js"
  # ShellCorona selects a Global Theme layout by the active ShellPackage ID.
  # Proper uses its own supported shell extension for the lock screen, so make
  # that exact lookup available from the same authoritative source.
  install -Dpm 0644 %{_sourcedir}/proper-desktop-layout.js \
    "%{buildroot}%{_datadir}/plasma/look-and-feel/$theme/contents/layouts/com.properlinux.desktop-layout.js"
done
install -Dpm 0644 %{_sourcedir}/proper-wallpaper.conf %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
# Plasma Login Manager loads system drop-ins before administrator overrides
# from /etc/plasmalogin.conf.d. Keep Proper's default separate from the Fedora
# settings package so both RPMs retain clean file ownership.
install -Dpm 0644 %{_sourcedir}/plasmalogin.conf \
  %{buildroot}%{_prefix}/lib/plasmalogin/plasmalogin.conf.d/50-proper.conf
install -Dpm 0644 %{_sourcedir}/tokens.yaml %{buildroot}%{_datadir}/proper-linux/tokens.yaml
install -d %{buildroot}%{_datadir}/proper-linux/ui
install -pm 0644 %{_builddir}/proper-ui/* %{buildroot}%{_datadir}/proper-linux/ui/
install -pm 0644 %{_builddir}/proper-semantic/proper-palette.json %{buildroot}%{_datadir}/proper-linux/ui/proper-palette.json
install -Dpm 0644 %{_builddir}/proper-semantic/Proper.colors %{buildroot}%{_datadir}/color-schemes/Proper.colors
install -Dpm 0644 %{_builddir}/proper-semantic/ProperLight.colors %{buildroot}%{_datadir}/color-schemes/ProperLight.colors
install -Dpm 0644 %{_builddir}/proper-semantic/ProperMidnight.colors %{buildroot}%{_datadir}/color-schemes/ProperMidnight.colors
install -Dpm 0644 %{_builddir}/proper-semantic/proper-dark.toml %{buildroot}%{_datadir}/vicinae/themes/proper-dark.toml
install -Dpm 0644 %{_builddir}/proper-semantic/proper-light.toml %{buildroot}%{_datadir}/vicinae/themes/proper-light.toml
# Keep Dolphin's desktop identity for task grouping while presenting Files with
# the PM-selected plain folder. These links retain Breeze's independently
# updated, size-specific upstream artwork rather than copying it into Proper.
icon_root=%{buildroot}%{_datadir}/icons
install -Dpm 0644 %{_sourcedir}/proper.index.theme "$icon_root/proper/index.theme"
install -Dpm 0644 %{_sourcedir}/proper-dark.index.theme "$icon_root/proper-dark/index.theme"
for size in 16 22 24 32 48 64 96; do
  install -d "$icon_root/proper/apps/$size" "$icon_root/proper-dark/apps/$size"
  sed 's/#f8fbff/#18202b/g' %{_sourcedir}/../proper-launchers/proper-vicinae.svg > "$icon_root/proper/apps/$size/proper-vicinae.svg"
  install -m 0644 %{_sourcedir}/../proper-launchers/proper-vicinae.svg "$icon_root/proper-dark/apps/$size/proper-vicinae.svg"
  ln -s "../../../breeze/places/$size/folder-blue.svg" \
    "$icon_root/proper/apps/$size/org.kde.dolphin.svg"
  ln -s "../../../breeze-dark/places/$size/folder-blue.svg" \
    "$icon_root/proper-dark/apps/$size/org.kde.dolphin.svg"
done
# Original small status artwork inherits KDE state handling and palette colours.
for variant in proper proper-dark; do
  install -d "$icon_root/$variant/status/22"
  for asset in %{_sourcedir}/status-icons/*.svg; do
    install -m 0644 "$asset" "$icon_root/$variant/status/22/"
  done
  for name in dashboard-show brightness-high audio-volume-muted audio-volume-low audio-volume-medium audio-volume-high network-wired-activated network-wired-disconnected; do
    ln -s "$name.svg" "$icon_root/$variant/status/22/$name-symbolic.svg"
  done
done
sed -i 's/#232629/#eff0f1/g' "$icon_root/proper-dark/status/22/"*.svg
style_root=%{buildroot}%{_datadir}/plasma/desktoptheme/proper
install -Dpm 0644 %{_sourcedir}/proper/metadata.json "$style_root/metadata.json"
install -Dpm 0644 %{_sourcedir}/proper/plasmarc "$style_root/plasmarc"
install -Dpm 0644 %{_builddir}/proper-semantic/Proper.colors "$style_root/colors"
install -Dpm 0644 %{_builddir}/proper-panel/popup-background.svg "$style_root/dialogs/background.svg"
install -Dpm 0644 %{_builddir}/proper-panel/panel-background.svg "$style_root/widgets/panel-background.svg"
install -Dpm 0644 %{_builddir}/proper-panel/solid-panel-background.svg "$style_root/solid/widgets/panel-background.svg"
install -Dpm 0644 %{_builddir}/proper-panel/solid-popup-background.svg "$style_root/solid/dialogs/background.svg"
install -Dpm 0644 %{_sourcedir}/proper/widgets/plasmoidheading.svg "$style_root/widgets/plasmoidheading.svg"
install -Dpm 0644 %{_sourcedir}/proper/widgets/tasks.svg "$style_root/widgets/tasks.svg"
# Keep all five system applets on their upstream QML and RPM update path.
# These generated files use Plasma's supported Style element contract only.
for asset in button line lineedit listitem slider switch tabbar viewitem; do
  install -Dpm 0644 "%{_builddir}/proper-controls/$asset.svg" "$style_root/widgets/$asset.svg"
done
# Notifications, tooltips, and workspace OSDs use the same approved surface
# recipe. Everything else remains an explicit Breeze fallback.
install -Dpm 0644 %{_builddir}/proper-panel/popup-background.svg "$style_root/widgets/tooltip.svg"
install -Dpm 0644 %{_builddir}/proper-panel/popup-background.svg "$style_root/widgets/translucentbackground.svg"
install -Dpm 0644 %{_builddir}/proper-panel/solid-popup-background.svg "$style_root/solid/widgets/tooltip.svg"
install -Dpm 0644 %{_builddir}/proper-panel/solid-popup-background.svg "$style_root/solid/widgets/translucentbackground.svg"
python3 %{_sourcedir}/generate-light-style.py %{_sourcedir}/tokens.yaml "$style_root" %{_builddir}/proper-semantic/ProperLight.colors %{buildroot}%{_datadir}/plasma/desktoptheme/proper-light
install -Dpm 0644 %{_sourcedir}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}%{_licensedir}/%{name}/CC-BY-SA-4.0.txt
install -Dpm 0644 %{_sourcedir}/LICENSES/LGPL-3.0-only.txt %{buildroot}%{_licensedir}/%{name}/LGPL-3.0-only.txt
install -Dpm 0644 %{_sourcedir}/LICENSES/GPL-2.0-or-later.txt %{buildroot}%{_licensedir}/%{name}/GPL-2.0-or-later.txt
install -Dpm 0644 %{_sourcedir}/LICENSES/GPL-3.0-or-later.txt %{buildroot}%{_licensedir}/%{name}/GPL-3.0-or-later.txt

# Plasma exposes the lock screen through its supported ShellPackage extension
# point. The package metadata names Fedora's active desktop shell as its
# fallback, so Proper owns only lockscreen QML and upstream fixes keep landing.
effect_root=%{buildroot}%{_datadir}/kwin/effects/proper-shelf-reveal
install -Dpm 0644 %{_sourcedir}/proper-shelf-reveal/metadata.json "$effect_root/metadata.json"
install -Dpm 0644 %{_sourcedir}/proper-shelf-reveal/contents/code/main.js "$effect_root/contents/code/main.js"

shell_root=%{buildroot}%{_datadir}/plasma/shells/com.properlinux.desktop
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/metadata.json "$shell_root/metadata.json"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/LockScreen.qml "$shell_root/contents/lockscreen/LockScreen.qml"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/LockScreenUi.qml "$shell_root/contents/lockscreen/LockScreenUi.qml"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/PasswordSync.qml "$shell_root/contents/lockscreen/PasswordSync.qml"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/ProperGridClock.qml "$shell_root/contents/lockscreen/ProperGridClock.qml"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/ProperPasswordCells.qml "$shell_root/contents/lockscreen/ProperPasswordCells.qml"
install -Dpm 0644 %{_builddir}/proper-semantic/ProperTokens.qml "$shell_root/contents/lockscreen/ProperTokens.qml"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/lockscreen/qmldir "$shell_root/contents/lockscreen/qmldir"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/updates/00-migrate-proper-panel-v1.js "$shell_root/contents/updates/00-migrate-proper-panel-v1.js"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/updates/01-migrate-status-shade-edge-v1.js "$shell_root/contents/updates/01-migrate-status-shade-edge-v1.js"
install -Dpm 0644 %{_sourcedir}/com.properlinux.desktop/contents/updates/03-migrate-status-shade-to-shelf-v3.js "$shell_root/contents/updates/03-migrate-status-shade-to-shelf-v3.js"

%check
python3 %{_sourcedir}/tests/test_window_decoration.py %{buildroot}%{_datadir}/aurorae/themes
QT_QPA_PLATFORM=offscreen python3 %{_sourcedir}/tests/test_panel_material.py %{_builddir}/proper-panel
# Proper overrides Files and selected status glyphs, inheriting the upstream
# Breeze themes. Preserve every size-specific source link.
grep -qx 'Inherits=breeze' %{buildroot}%{_datadir}/icons/proper/index.theme
grep -qx 'Inherits=breeze-dark' %{buildroot}%{_datadir}/icons/proper-dark/index.theme
for size in 16 22 24 32 48 64 96; do
  light_icon=%{buildroot}%{_datadir}/icons/proper/apps/$size/org.kde.dolphin.svg
  dark_icon=%{buildroot}%{_datadir}/icons/proper-dark/apps/$size/org.kde.dolphin.svg
  test -L "$light_icon"
  test -L "$dark_icon"
  test "$(readlink "$light_icon")" = "../../../breeze/places/$size/folder-blue.svg"
  test "$(readlink "$dark_icon")" = "../../../breeze-dark/places/$size/folder-blue.svg"
done

# Proper's rounded shell surfaces provide complete masks. Keep the checks here
# for builds outside the repository wrapper. Panels follow Breeze's
# tiled-centre contract with the same material opacity in all nine slices.
for asset in \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/panel-background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/translucentbackground.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/translucentbackground.svg; do
  xmllint --noout "$asset"
  for element in \
    center top bottom left right \
    topleft topright bottomleft bottomright \
    mask-center mask-top mask-bottom mask-left mask-right \
    mask-topleft mask-topright mask-bottomleft mask-bottomright; do
    test "$(xmllint --xpath "count(//*[@id = '$element'])" "$asset")" = 1
  done
done
for asset in \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/panel-background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/translucentbackground.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/translucentbackground.svg; do
  test "$(xmllint --xpath "count(//*[@id = 'hint-compose-over-border'])" "$asset")" = 0
  test "$(xmllint --xpath "count(//*[@id = 'hint-tile-center'])" "$asset")" = 1
  centre_opacity=$(xmllint --xpath "string(//*[@id='center']/@fill-opacity)" "$asset")
  test "$(xmllint --xpath "count(//*[@id='top' or @id='bottom' or @id='left' or @id='right']/*[1][@fill-opacity='$centre_opacity'])" "$asset")" = 4
  test "$(xmllint --xpath "count(//*[@id='topleft' or @id='topright' or @id='bottomleft' or @id='bottomright']/*[1][@opacity='$centre_opacity'])" "$asset")" = 4
  test "$(xmllint --xpath "count(//*[@id='topleft' or @id='topright' or @id='bottomleft' or @id='bottomright']/*[1]/*[local-name()='rect'])" "$asset")" = 0
  rim_color=$(xmllint --xpath "string(//*[@id='top']/*[2]/@fill)" "$asset")
  rim_opacity=$(xmllint --xpath "string(//*[@id='top']/*[2]/@fill-opacity)" "$asset")
  test "$(xmllint --xpath "count(//*[@id='top' or @id='bottom' or @id='left' or @id='right']/*[2][@fill='$rim_color' and @fill-opacity='$rim_opacity'])" "$asset")" = 4
  test "$(xmllint --xpath "count(//*[@id='topleft' or @id='topright' or @id='bottomleft' or @id='bottomright']/*[2][@opacity='$rim_opacity'])" "$asset")" = 4
  test "$(xmllint --xpath "count(//*[@id='topleft' or @id='topright' or @id='bottomleft' or @id='bottomright']/*[2]/*[local-name()='rect' and @fill='$rim_color'])" "$asset")" = 0
  test "$(xmllint --xpath "count(//*[starts-with(@id, 'rim-') and (@stroke='$rim_color' or @fill='$rim_color')])" "$asset")" = 4
  test "$(xmllint --xpath "count(//*[local-name()='linearGradient'])" "$asset")" = 0
  test "$(xmllint --xpath "count(//*[@id='mask-topleft' or @id='mask-topright' or @id='mask-bottomleft' or @id='mask-bottomright']/*[local-name()='rect'])" "$asset")" = 8
done
for asset in \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/panel-background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/translucentbackground.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/translucentbackground.svg; do
  test "$(xmllint --xpath "string(//*[@id='rim-topleft']/@d)" "$asset")" = 'M16 0H15C6.72 0 0 6.72 0 15V16H1V15C1 7.27 7.27 1 15 1H16Z'
  test "$(xmllint --xpath "string(//*[@id='rim-topright']/@d)" "$asset")" = 'M0 0H1C9.28 0 16 6.72 16 15V16H15V15C15 7.27 8.73 1 1 1H0Z'
  test "$(xmllint --xpath "string(//*[@id='rim-bottomleft']/@d)" "$asset")" = 'M16 16H15C6.72 16 0 9.28 0 1V0H1V1C1 8.73 7.27 15 15 15H16Z'
  test "$(xmllint --xpath "string(//*[@id='rim-bottomright']/@d)" "$asset")" = 'M0 16H1C9.28 16 16 9.28 16 1V0H15V1C15 8.73 8.73 15 1 15H0Z'
done
for asset in \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/dialogs/background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/translucentbackground.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/tooltip.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/translucentbackground.svg; do
  shadow_selector="//*[starts-with(@id, 'shadow-') and not(starts-with(@id, 'shadow-hint-')) and (local-name()='rect' or local-name()='path' or local-name()='g')]"
  test "$(xmllint --xpath "count($shadow_selector)" "$asset")" = 9
  test "$(xmllint --xpath "count(${shadow_selector}[@fill-opacity and number(@fill-opacity) <= 0.001])" "$asset")" = 9
done
for asset in \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/panel-background.svg; do
  shadow_selector="//*[starts-with(@id, 'shadow-') and not(starts-with(@id, 'shadow-hint-')) and (local-name()='rect' or local-name()='path' or local-name()='g')]"
  test "$(xmllint --xpath "count($shadow_selector)" "$asset")" = 9
  test "$(xmllint --xpath "count(${shadow_selector}[@fill-opacity and number(@fill-opacity) <= 0.001])" "$asset")" = 9
  test "$(xmllint --xpath "string(//*[@id = 'floating-hint-top-margin']/@height)" "$asset")" = 12
  test "$(xmllint --xpath "string(//*[@id = 'floating-hint-left-margin']/@width)" "$asset")" = 12
done
test "$(xmllint --xpath "string(//*[@id = 'center']/@fill-opacity)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg)" = 0.66
test "$(xmllint --xpath "string(//*[@id = 'center']/@fill-opacity)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/panel-background.svg)" = 1.00
test "$(xmllint --xpath "string(//*[@id = 'center']/@fill-opacity)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/dialogs/background.svg)" = 0.66
test "$(xmllint --xpath "string(//*[@id = 'center']/@fill-opacity)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/dialogs/background.svg)" = 1.00
test "$(xmllint --xpath "string(//*[@id = 'center']/@fill)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/dialogs/background.svg)" = \
  "$(xmllint --xpath "string(//*[@id = 'center']/@fill)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg)"
test "$(xmllint --xpath "string(//*[@id = 'center']/@fill)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/dialogs/background.svg)" = \
  "$(xmllint --xpath "string(//*[@id = 'center']/@fill)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/solid/widgets/panel-background.svg)"
heading_asset=%{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/plasmoidheading.svg
xmllint --noout "$heading_asset"
for prefix in header footer; do
  for side in top bottom left right topleft topright bottomleft bottomright center; do
    test "$(xmllint --xpath "count(//*[@id='$prefix-$side'])" "$heading_asset")" = 1
  done
done
test "$(xmllint --xpath "count(//*[@id='header-top' or @id='header-left' or @id='header-right']/*[2][@fill='#a6afbd' and @fill-opacity='0.18'])" "$heading_asset")" = 3
test "$(xmllint --xpath "count(//*[@id='header-topleft' or @id='header-topright']/*[2][local-name()='path' and @fill='#a6afbd' and @fill-opacity='0.18'])" "$heading_asset")" = 2
test "$(xmllint --xpath "count(//*[@id='header-bottomleft' or @id='header-bottomright']/*[@fill='#a6afbd'])" "$heading_asset")" = 4
test "$(xmllint --xpath "count(//*[@id='footer-bottom' or @id='footer-left' or @id='footer-right']/*[2][@fill='#a6afbd' and @fill-opacity='0.18'])" "$heading_asset")" = 3
test "$(xmllint --xpath "count(//*[@id='footer-bottomleft' or @id='footer-bottomright']/*[2][local-name()='path' and @fill='#a6afbd' and @fill-opacity='0.18'])" "$heading_asset")" = 2
for asset in button lineedit listitem tabbar viewitem; do
  control_asset=%{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/$asset.svg
  test "$(xmllint --xpath "count(//*[contains(@id, 'hint-compose-over-border')])" "$control_asset")" = 0
done
test "$(xmllint --xpath "count(//*[@fill-opacity and number(@fill-opacity) != 0])" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/tasks.svg)" = 0
grep -qx 'enabled=true' %{buildroot}%{_datadir}/plasma/desktoptheme/proper/plasmarc
grep -qx 'contrast=0.72' %{buildroot}%{_datadir}/plasma/desktoptheme/proper/plasmarc
grep -qx 'intensity=0.82' %{buildroot}%{_datadir}/plasma/desktoptheme/proper/plasmarc
grep -qx 'saturation=1.15' %{buildroot}%{_datadir}/plasma/desktoptheme/proper/plasmarc
panel_radius=$(sed -n "s/^radius: {panel: \([0-9][0-9]*\),.*/\1/p" \
  %{buildroot}%{_datadir}/proper-linux/tokens.yaml)
popup_radius=$(sed -n "s/^radius: {panel: [0-9][0-9]*, popup: \([0-9][0-9]*\),.*/\1/p" \
  %{buildroot}%{_datadir}/proper-linux/tokens.yaml)
asset_radius=$(xmllint --xpath "string(//*[@id='top']/*[1]/@height)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg)
mask_radius=$(xmllint --xpath "string(//*[@id='mask-top']/@height)" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/panel-background.svg)
test -n "$panel_radius"
test -n "$popup_radius"
test "$panel_radius" = "$asset_radius"
test "$panel_radius" = "$mask_radius"
test "$panel_radius" = "$popup_radius"

# Proper task frames must stay empty because the patched task QML owns each
# exact line or dot. Visible FrameSvg edge art tiles across the button and is
# the source of the repeated-line/repeated-dot regression.
task_asset=%{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/tasks.svg
xmllint --noout "$task_asset"
for state in normal focus hover minimized attention progress; do
  for slice in center top bottom left right topleft topright bottomleft bottomright; do
    test "$(xmllint --xpath "count(//*[@id = '$state-$slice'])" "$task_asset")" = 1
  done
done
visible_task_shapes=$(xmllint --xpath "count(//*[starts-with(@id, 'normal-') or starts-with(@id, 'focus-') or starts-with(@id, 'hover-') or starts-with(@id, 'minimized-') or starts-with(@id, 'attention-') or starts-with(@id, 'progress-')]//*[local-name()='rect' or local-name()='circle' or local-name()='path'][not(@fill-opacity) or number(@fill-opacity) > 0.001])" "$task_asset")
test "$visible_task_shapes" = 0
for direction in top bottom left right; do
  test "$(xmllint --xpath "count(//*[@id = 'group-expander-$direction'])" "$task_asset")" = 1
done

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
lineedit_asset=%{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/lineedit.svg
test "$(xmllint --xpath "string(//*[@id = 'base-hint-left-margin']/@width)" "$lineedit_asset")" = 7
for state in hover focus focusframe; do
  test "$(xmllint --xpath "string(//*[@id = '$state-hint-left-margin']/@width)" "$lineedit_asset")" = 0.001
  test "$(xmllint --xpath "string(//*[@id = '$state-hint-right-margin']/@width)" "$lineedit_asset")" = 0.001
  test "$(xmllint --xpath "string(//*[@id = '$state-hint-top-margin']/@height)" "$lineedit_asset")" = 0.001
  test "$(xmllint --xpath "string(//*[@id = '$state-hint-bottom-margin']/@height)" "$lineedit_asset")" = 0.001
done
switch_asset=%{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/switch.svg
test "$(xmllint --xpath "count(//*[@id = 'inactive-left' or @id = 'inactive-right' or @id = 'active-left' or @id = 'active-right'][local-name()='path'])" "$switch_asset")" = 4
test "$(xmllint --xpath "string(//*[@id = 'hint-bar-size']/@width)" "$switch_asset")" = 38
test "$(xmllint --xpath "string(//*[@id = 'hint-bar-size']/@height)" "$switch_asset")" = 16
test "$(xmllint --xpath "string(//*[@id = 'handle']/@r)" "$switch_asset")" = 8
test "$(xmllint --xpath "count(//*[@id = 'groove-highlight-center'])" \
  %{buildroot}%{_datadir}/plasma/desktoptheme/proper/widgets/slider.svg)" = 1

# The arrival clock and password masks share Proper's exact square-cell visual
# grammar while the real password TextField remains the authentication owner.
shell_root=%{buildroot}%{_datadir}/plasma/shells/com.properlinux.desktop/contents
lock_root=$shell_root/lockscreen
test -f "$lock_root/ProperGridClock.qml"
test -f "$lock_root/ProperPasswordCells.qml"
test -f "$lock_root/ProperTokens.qml"
grep -Fq 'Accessible.role: Accessible.StaticText' "$lock_root/ProperGridClock.qml"
grep -Fq 'readonly property int rowCount: 7' "$lock_root/ProperGridClock.qml"
grep -Fq 'readonly property int digitColumnCount: 5' "$lock_root/ProperGridClock.qml"
grep -Fq 'readonly property string uiFontFamily: properTokens.uiFont' "$lock_root/LockScreenUi.qml"
grep -Fq 'passwordCharacter: "▪"' "$lock_root/LockScreenUi.qml"
grep -Fq 'passwordLength: passwordBox.text.length' "$lock_root/LockScreenUi.qml"
for theme in com.properlinux.dark.desktop com.properlinux.light.desktop com.properlinux.midnight.desktop; do
  theme_root=%{buildroot}%{_datadir}/plasma/look-and-feel/$theme/contents
  test -f "$theme_root/layouts/org.kde.plasma.desktop-layout.js"
  test -f "$theme_root/layouts/com.properlinux.desktop-layout.js"
  cmp "$theme_root/layouts/org.kde.plasma.desktop-layout.js" \
    "$theme_root/layouts/com.properlinux.desktop-layout.js"
  test -f "$theme_root/splash/ProperTokens.qml"
  grep -Fq 'color: properTokens.arrivalBase' "$theme_root/splash/Splash.qml"
done
test -f %{buildroot}%{_datadir}/proper-linux/ui/proper-palette.json
for scheme in Proper ProperLight ProperMidnight; do
  grep -q '^\[Colors:Window\]$' %{buildroot}%{_datadir}/color-schemes/$scheme.colors
done
grep -Fq 'background = "#141a22"' %{buildroot}%{_datadir}/vicinae/themes/proper-dark.toml
grep -Fq 'border = "#232932"' %{buildroot}%{_datadir}/vicinae/themes/proper-dark.toml
grep -A12 '^\[Colors:Header\]$' %{buildroot}%{_datadir}/color-schemes/Proper.colors | \
  grep -Fq 'BackgroundNormal=20,26,34'

%files
%{_datadir}/kwin/effects/proper-shelf-reveal/
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
%{_datadir}/plasma/desktoptheme/proper-light/
%{_datadir}/aurorae/themes/proper-dark/
%{_datadir}/aurorae/themes/proper-light/
%{_datadir}/aurorae/themes/proper-midnight/
%{_datadir}/plasma/shells/com.properlinux.desktop/
%{_datadir}/icons/proper/
%{_datadir}/icons/proper-dark/
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/env/proper-wallpaper.conf
%{_prefix}/lib/plasmalogin/plasmalogin.conf.d/50-proper.conf
%{_datadir}/proper-linux/tokens.yaml
%{_datadir}/proper-linux/ui/
%{_datadir}/color-schemes/Proper.colors
%{_datadir}/color-schemes/ProperLight.colors
%{_datadir}/color-schemes/ProperMidnight.colors
%{_datadir}/vicinae/themes/proper-dark.toml
%{_datadir}/vicinae/themes/proper-light.toml
%license %{_licensedir}/%{name}/CC-BY-SA-4.0.txt
%license %{_licensedir}/%{name}/LGPL-3.0-only.txt
%license %{_licensedir}/%{name}/GPL-2.0-or-later.txt
%license %{_licensedir}/%{name}/GPL-3.0-or-later.txt

%changelog
* Sat Sep 05 2026 Proper Linux <proper@example.invalid> - 0.1-56
- Derive matching light shell material and controls from the shared geometry

* Sat Sep 05 2026 Proper Linux <proper@example.invalid> - 0.1-55
- Keep shelf material consistent in floating and attached states

* Sat Sep 05 2026 Proper Linux contributors - 0.1-54
- Refine shelf spacing, status artwork and shared surface edges
- Match rounded slice bounds and reserve icon-to-indicator clearance
- Reveal the first shelf surface with a focused KWin effect

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-53
- Generate Vicinae light and dark themes from the shared semantic tokens
- Match the dark launcher tint to the translucent Proper shelf material
- Give Breeze window title bars the same dark material tint

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-52
- Give panel applet popups the shelf's exact translucent and solid material
- Keep the Command Centre on Plasma's supported dialog-background path

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-51
- Restore the approved chunky 5-by-7 clock on login and lock surfaces
- Keep its colours and shadows sourced from shared semantic tokens

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-50
- Match the retired single-applet top panel by ownership after Plasma sizing
- Move Command Centre to the shelf without touching user-created top panels

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-49
- Use denser 7-by-11 square-cell clocks on login and lock surfaces
- Move Command Centre into the existing shelf and migrate the former top handle

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-48
- Match popup corner geometry to the rounded Proper shelf material
- Keep Plasma as the single owner of popup tint, blur, contrast, and masking

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-47
- Keep a fixed centred Status Shade handle for reliable one-click activation
- Migrate only the exact former auto-hide default through a Plasma shell update

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-46
- Name the first-profile Global Theme layout for Proper's active ShellPackage
- Keep the upstream-shell compatibility hook sourced from the same layout

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-45
- Install the canonical panel layout as the active ShellPackage first-login hook
- Reuse that same source for user-applied Global Theme layout changes

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-44
- Create the visible shelf before the optional top-edge status surface
- Bind the Status Shade shortcut only after KGlobalAccel is available

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-43
- Create the shelf and Status Shade together through the Global Theme layout
- Prevent first-profile services from pre-empting Plasma's supported defaults

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-42
- Generate KDE schemes, installer CSS, and login/lock tokens from one semantic palette
- Seed the shelf through the supported Global Theme layout and consolidate its migration
- Keep desktop settings layered while preserving later user choices

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-41
- Ship login defaults through PLM's supported system drop-in directory
- Preserve Fedora package ownership and administrator wallpaper overrides

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-39
- Remove shortcut containers from the live welcome and strengthen its hierarchy
- Enlarge the primary choice row while keeping key hints quiet and legible

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-38
- Give dialogs, tooltips, notifications, and OSDs one uniform seam-safe body
- Remove translucent centre-under-border composition from shell and controls
- Add dense popup variants and audit every generated rounded control frame
- Bump the Plasma Style version so upgraded systems invalidate cached SVGs

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-37
- Render one uniform shelf rim around all four sides and corner arcs
- Bleed each corner rim into both adjoining slices to remove subpixel breaks
- Bump the Plasma Style version so upgraded systems invalidate cached SVGs

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-36
- Carry every one-pixel corner rim to the adjoining nine-slice boundary
- Prevent sub-pixel breaks where curved and straight panel edges meet

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-35
- Bleed each rounded panel corner into its adjoining nine-slice edges
- Keep that overlap inside one opacity group so cap joins stay invisible

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-34
- Follow Plasma's native tiled-centre panel contract at one uniform opacity
- Bound rim geometry and neutralize shadow and task textures that exposed joins

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-33
- Present Files with the PM-selected plain blue Breeze folder
- Preserve Dolphin task grouping and inherit every other icon from Breeze

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-32
- Render the lock-screen time as Proper square-cell numerals and colon
- Replace round password dots with exact square-cell masks

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-31
- Recompose the floating shelf as lighter, contrast-managed native acrylic
- Add a directional rim, rounded ambient shadow, and matching dense panel state
- Generate both panel materials from the canonical Proper design tokens

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-30
- Keep focused line edits inside their owning applet rows
- Repair switch track composition and rebalance its handle
- Leave tiled task frames visually empty for exact QML-owned indicators

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
