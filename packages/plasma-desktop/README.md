# Plasma Desktop presentation

The Fedora source RPM and checksum live in `source-rpm.env`. Keep its upstream
patches and rebuild only the matching Fedora release.

`proper-task-loading-indicator.patch` owns the existing bounded shelf marks and
running-window previews. `proper-settings-home.patch` replaces the landing KCM
composition with `ProperSettingsHome.qml` and one native process-launch method.
The six cards navigate to existing KDE modules; Appearance opens Proper's
existing application. Search, sidebar, and all other KCMs stay upstream.
Original Proper QML is GPL-2.0-or-later; upstream licences remain in the patch.

Compatibility: Plasma 6.7.4, Fedora 44, Qt 6.11.2, KCMUtils/Kirigami 6.29.
SimpleKCM sets each padding edge explicitly, so overriding `padding` alone does
not change its margins. Its writable `buttons` property accepts zero for a
navigation-only home page. Do not hide Apply buttons on editable KCMs.

When rebasing, regenerate the patch from the original Fedora source, verify the
readable QML matches its patched file, build the owning RPM, and exercise cards,
search, sidebar and light/dark palettes. During repeated same-upstream-version
VM previews, Qt's old disk QML cache may survive a package replacement; stop the
preview app and remove only its disposable cache before assessing the new UI.

Official guidance: https://develop.kde.org/docs/features/configuration/kcm/
Upstream: https://invent.kde.org/plasma/plasma-desktop/-/tree/v6.7.4/kcms/landingpage
