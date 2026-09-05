# System Settings presentation

Fedora plasma-systemsettings 6.7.4-1.fc44, pinned and checksummed in source-rpm.env.
The upstream LGPL-2.0-only QML is compiled into the executable; there is no
installed theme override for this layout. proper-settings-chrome.patch removes
its short header divider, gives search the full sidebar width, and moves the
native application menu to the footer. It retains navigation and settings code.

Build with PROPER_RPM_RESUME=1 PROPER_RPM_PACKAGES=plasma-systemsettings scripts/build-rpms.
Rebase the presentation patch and validate pointer, keyboard, search, subcategory
Back, and the menu whenever Fedora updates the source. Drop this exception when
upstream exposes equivalent layout configuration. No upstream version is pinned
on installed systems; update-installed refuses a mismatched Fedora version.
