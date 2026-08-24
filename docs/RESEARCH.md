# Proper Linux research and upstream references

Last reviewed: 2026-08-24.

This is a working technical reference, not a substitute for checking current upstream documentation during implementation. Pin exact revisions when code enters the build.

## Fedora base and image construction

### Fedora KDE Plasma Desktop 44

- Current Fedora KDE download and architecture information: <https://www.fedoraproject.org/kde/download/>
- Fedora 44 release overview: <https://fedoramagazine.org/announcing-fedora-linux-44/>

Fedora KDE 44 is the initial base. It supplies KDE Plasma 6, a live ISO, graphical installation, and x86-64 support.

### Current Fedora image tooling

- Fedora “Building a Fedora” overview: <https://fedoraproject.org/wiki/Building_a_Fedora>
- Fedora's boot ISO modernisation notes: <https://fedoraproject.org/wiki/Changes/ModernizeBootISO>
- KIWI upstream documentation: <https://osinside.github.io/kiwi/>
- Fedora KIWI package overview: <https://packages.fedoraproject.org/pkgs/kiwi/>

Fedora states that KIWI builds most current variants and that package-based live media has moved to KIWI. Proper Linux should pin and extend Fedora's KDE live description rather than start from legacy `livecd-tools` instructions.

## Fedora derivative and branding

- Fedora Remix overview: <https://fedoraproject.org/wiki/Remix>
- Fedora distribution/trademark guidance: <https://fedoraproject.org/wiki/Distribution>
- Fedora Remix mark guidelines: <https://fedoraproject.org/wiki/Legal%3ASecondary_trademark_usage_guidelines>

Proper Linux may use its own name and visual identity, but a public derivative must not appear to be an official Fedora edition. Rebranding work must replace the relevant release/logo assets and retain correct attribution.

## KDE Plasma and login

### Plasma extension points

- Plasma themes and plugins: <https://develop.kde.org/docs/plasma/>
- Plasma style details: <https://develop.kde.org/docs/plasma/theme/theme-details/>
- KRunner development: <https://develop.kde.org/docs/plasma/krunner/>

Plasma Global Themes can collect layouts, colours, styles, decorations, cursors, splash/lock assets, and related defaults. KWin and Plasma scripting provide supported seams for window and panel behaviour.

### Plasma Login Manager

- Fedora 44 Plasma Login Manager change: <https://fedoraproject.org/wiki/Changes/PlasmaLoginManager>
- Upstream Plasma Login Manager: <https://github.com/KDE/plasma-login-manager>
- Fedora package: <https://packages.fedoraproject.org/pkgs/plasma-login-manager/plasma-login-manager/>

Fresh Fedora KDE 44 uses PLM rather than SDDM. PLM runs a Plasma/KWin greeter session and provides a supported path for applying appearance and display settings. Login configuration is machine-global and owned by the greeter account; it cannot simply inherit an arbitrary user's private configuration.

The desktop and login wallpapers are conceptually separate. Proper Linux must ship a consistent system-wide default and provide an explicit sync/action for later user changes if desired.

## Omarchy reference

- Manual: <https://omarchy.org/manual/>
- Navigation: <https://omarchy.org/manual/navigation/>
- Hotkeys: <https://omarchy.org/manual/hotkeys/>
- AI tools: <https://omarchy.org/manual/ai/>
- Terminal: <https://omarchy.org/manual/terminal/>

Omarchy's valuable ideas are decisive curation, cohesive theming, developer-tool selection, shortcut vocabulary, update presentation, and agent access. Proper Linux deliberately rejects its mandatory tiling and keyboard-dominant operating model.

## Launchers

### Vicinae

- Source/features: <https://github.com/vicinaehq/vicinae>
- Documentation: <https://docs.vicinae.com/>
- Linux installation guidance: <https://docs.vicinae.com/install/linux>

Vicinae is the closest current open-source Raycast-style product for Linux. It uses C++/Qt/QML, supports applications, files, clipboard, actions, scripts, and extensions, and is licensed GPL-3.0. It remains keyboard-oriented by philosophy, so Proper Linux must audit all promoted actions for pointer use and provide a visible taskbar entry point.

The launcher should be packaged as a pinned Proper RPM rather than Flatpak because it requires broad desktop integration. Keep styling/configuration separate from upstream source where possible.

### Rejected: AppGrid

- Product site: <https://appgrid.xarbit.dev/>

AppGrid was evaluated and rejected by the product manager on visual grounds. It must not be added as a fallback launcher unless the PM explicitly reopens the decision.

## File managers

### Dolphin

- KDE product page and screenshots: <https://apps.kde.org/dolphin/>
- Fedora 44 package: <https://packages.fedoraproject.org/pkgs/dolphin/dolphin/fedora-44-updates.html>

Dolphin is current, lightweight, native to KDE, and supports tabs, split view, custom actions, plugins, remote/cloud locations, previews, and an embedded terminal. Its weakness for Proper Linux is stock visual density, which can be addressed through defaults before considering a replacement.

### GNOME Files / Nautilus

- Product page and screenshots: <https://apps.gnome.org/Nautilus/>
- Fedora 44 package: <https://packages.fedoraproject.org/pkgs/nautilus/nautilus/fedora-44.html>

Nautilus provides an exceptionally clean interface and covers ordinary local, network, removable-media, search, grid/list, script, and plugin flows. It is designed around GNOME/libadwaita, has fewer power features than Dolphin, and would introduce a visibly different toolkit and settings model on a Plasma desktop.

### COSMIC Files

- Source: <https://github.com/pop-os/cosmic-files>
- Fedora 44 package: <https://packages.fedoraproject.org/pkgs/cosmic-files/cosmic-files/fedora-44.html>

COSMIC Files is a modern GPL-3.0 Rust/libcosmic file manager and is packaged in Fedora 44. It is the most interesting visual alternative, but it is designed for the COSMIC desktop and requires its own theme/icon dependencies. Its Plasma behaviour and feature completeness must be judged in the actual VM.

### Rejected for the default: Spacedrive

- Source/status: <https://github.com/spacedriveapp/spacedrive>

Spacedrive has a visually ambitious cross-device concept, but its current Linux release is explicitly alpha. It is not suitable as the default file manager for version 0.1.

## Terminal

- Ghostty: <https://ghostty.org/>
- Source: <https://github.com/ghostty-org/ghostty>

Ghostty is the preferred terminal. Implementation must confirm the current Fedora packaging/source, licence, Wayland behaviour, configuration path, and best KWin technique for a retained dropdown window.

## Applications and Flatpak

- Flatpak documentation: <https://docs.flatpak.org/>
- Flathub: <https://flathub.org/>
- Fedora Flatpak documentation: <https://docs.fedoraproject.org/en-US/flatpak/>

Flatpak is one provider for Proper Apps, not the product's sole application strategy. Verify publisher identity and architecture availability per catalogue entry.

## Name search

A preliminary exact-name web and GitHub search on 2026-08-24 found no prominent distribution named “Proper Linux.” This result is not a trademark clearance, company-name search, domain check, or legal opinion. Complete a formal review before public branding investment or release.

## Research still required during implementation

- Exact Fedora KDE 44 KIWI profile/revision and local build invocation
- Package and redistribution status for Vicinae and Ghostty on Fedora 44
- Like-for-like Dolphin, Nautilus, and COSMIC Files evaluation under Proper Plasma defaults
- PLM installer-to-first-login display-layout transfer
- Legal redistribution paths for proprietary catalogue applications
- Best maintained GitHub Desktop Linux port and how clearly to label it
- Current official installation methods for Codex, Claude Code, OpenCode, VS Code Insiders, Chrome, and Docker on Fedora
- Final font, icon, and artwork licences
