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

### Phase 0 baseline pin

- **Checked:** 2026-08-24
- **Source:** https://forge.fedoraproject.org/releng/kiwi-descriptions.git
- **Fedora 44 commit:** dfc49a5a10f69941179fdadd96aa6a5984f7c677
- **Profile:** KDE-Desktop-Live with KIWI iso output
- **Licence:** GPL-3.0-or-later
- **Update method:** resolve the f44 branch only through scripts/pin-fedora-base, review the resulting immutable revision, and commit the lock update before rebuilding.

Fedora's old fedora-kiwi-descriptions path currently redirects to the canonical releng/kiwi-descriptions Forge repository. The build lock uses the canonical path.

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

### Current product and hardware comparison

- Manual/product model: <https://omarchy.org/manual/>
- Theme system: <https://omarchy.org/manual/making-your-own-theme/>
- Mac support: <https://github.com/basecamp/omarchy/blob/quattro/manual/44-mac-support.md>

Omarchy currently describes itself as an omakase Arch distribution built on
Hyprland and Quickshell. Its theme palette generates coordinated configuration
for its shell, terminals, `btop`, editors and selected graphical applications.
This is a strong reference for Proper's design-token and live-iteration model.

Omarchy now documents built-in Intel Mac support, including a patched kernel
and supporting configuration for T2 machines. Its official documentation says
M-series Apple Silicon Macs are not directly supported. Community ports exist,
but they are not evidence of upstream Omarchy support.

## Apple hardware

### Apple Silicon

- Fedora Asahi Remix and device support: <https://asahilinux.org/fedora/>
- Detailed feature support: <https://asahilinux.org/docs/platform/feature-support/overview/>
- Fedora Asahi SIG: <https://fedoraproject.org/wiki/SIGs/Asahi>

Apple M-series systems are ARM64 machines and do not boot the Proper Linux
version 0.1 x86-64 ISO. Fedora Asahi Remix 44 currently supports the M1 and M2
families through Apple-specific boot integration, a 16K-page kernel, Mesa and
hardware-enablement packages. This is the technically credible base for a
future Proper Apple Silicon edition, but it would be a separate image profile,
package-validation target and release commitment.

M3 and M4 work remains visible in Asahi's support tables but is not part of the
current Fedora Asahi M1/M2 support claim. Do not infer support from the presence
of an upstream device entry.

### Intel Macs

- T2 Linux project: <https://t2linux.org/>
- T2 Fedora installation notes: <https://wiki.t2linux.org/distributions/fedora/installation/>

Standard Fedora x86-64 media can boot some Intel Macs, especially pre-T2
models, but working installation and complete laptop support are model-specific.
Broadcom wireless, audio, cameras, suspend, Touch Bar, keyboard and trackpad
support have all required special handling on different generations. T2 models
generally require the external T2 Linux kernel and integration packages for a
complete experience. Proper Linux 0.1 should treat Intel Mac operation as
unvalidated incidental compatibility rather than a product promise.

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
- Fedora 44 PLM observation on BOX (2026-08-25): `/usr/lib/plasmalogin/defaults.conf` is the distro default actually read by the greeter; a `plasmalogin.conf.d` fragment was present but had no effect. The Proper package now owns a source copy and applies it in `%posttrans` without conflicting with Fedora's package ownership.
- Legal redistribution paths for proprietary catalogue applications
- Best maintained GitHub Desktop Linux port and how clearly to label it
- Current official installation methods for Codex, Claude Code, OpenCode, VS Code Insiders, Chrome, and Docker on Fedora
- Final font, icon, and artwork licences

## Phase 4 source audit — 2026-08-25

- Ghostty upstream: <https://github.com/ghostty-org/ghostty>; official source release: <https://release.files.ghostty.org/1.2.3/ghostty-1.2.3.tar.gz>.
- Upstream packaging guidance says to use the project source tarball rather than GitHub's generated archive. Ghostty is MIT licensed. Fedora 44's configured repositories were queried on the BOX and did not return a `ghostty` package, so `proper-terminal` builds the pinned source with the official Zig 0.14.1 binary release plus Fedora's `gtk4-devel`, `libadwaita-devel`, and related build dependencies. Zig is build-only, verified with the official minisign signature; SHA-256 is `24aeeec8af16c381934a6cd7d95c807a8cb2cf7df9fa40d359aa884195c4716c`. The resulting Ghostty RPM payload includes the executable, desktop metadata, shell integration, themes, terminfo, D-Bus service and KIO service menu.
- Proper terminal runtime configuration is versioned in `packages/proper-terminal/ghostty.conf`; update checks must record the release URL, checksum, licence and build dependency changes before promotion.
- Build result: official Ghostty 1.2.3 source checksum `559770fe9773161e93e3dd9177d916e27037d7f548edcf6186eabc571c0e520b`; the pinned `proper-terminal` RPM checksum is `4a2d48289bc9b4a095ca1aaeeba1c3b14e3d561311c102fa6fdf744e38d7fe75`. Update by auditing the official release tarball, its minisign signature, the declared Zig requirement and the generated runtime payload before rebuilding.

## Phase 5 provider audit — 2026-08-25

- `apps/catalogue-v1.json` is schema version 1 and records provider, status, licence, architecture, install and launch metadata.
- Fedora RPM, Flathub, and official vendor paths are represented. Proprietary binaries are not redistributed. GitHub Desktop is labelled community-maintained. Codex deliberately opens the official installation/authentication flow without storing credentials.
