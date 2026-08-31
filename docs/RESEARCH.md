# Proper Linux research and upstream references

Last reviewed: 2026-08-31.

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
- Fedora 44 PLM observation on BOX (2026-08-25): `/usr/lib/plasmalogin/defaults.conf` is the distro default actually read by the greeter. The Proper package owns a source copy and applies it in `%posttrans` without conflicting with Fedora's package ownership. A later 6.7.4 source audit confirmed that `/etc/plasmalogin.conf.d` is also loaded; a fragment affects a newly started greeter, not an already-running wallpaper process.
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

## Vicinae source-build audit — 2026-08-26

- The official Vicinae v0.24.0 source archive is pinned to commit `01cd7cb4936d9cb14272091623da85e7c880f0dc`, SHA-256 `ee4e80d6e69193820b294a43a008794d8761cda9914256c32aed3be091f5c0e3`, and GPL-3.0-or-later. It is built against Fedora 44 Qt 6.11.1; no private-Qt symbol relabeling or prebuilt executable is used.
- The build's upstream CMake dependencies were recorded from the successful build: Glaze v7.2.0, commit `b518eec7a22e56ffa238b072c07f47efa7cea97f`, MIT; and QtKeychain v0.14.0, commit `e63da2868465db18eb35a312b2635c26fdc46923`, BSD-3-Clause. Sources are <https://github.com/stephenberry/glaze> and <https://github.com/frankosterfeld/qtkeychain>. They are build-only FetchContent dependencies; updates require re-auditing their exact commits, licences and checksums.
- The resulting `proper-launchers-0.1-3.fc44.x86_64.rpm` is SHA-256 `2eba5e5c71222a462beebe2b3928c772f2fe70b82840874d6cdd485587495d6d`. The exact fresh ISO is SHA-256 `31d8dab4c7d7b1001526268b2b2dd29ff67decfb252b0941101b79a94167c50d`.

## Plasma Login Manager layout audit — 2026-08-31

- Fedora 44 currently ships `plasma-login-manager` 6.7.4. Its wallpaper is a
  supported plugin/configuration surface, and its settings loader cascades
  `/etc/plasmalogin.conf`, `/etc/plasmalogin.conf.d`, the distro defaults file,
  and the distro defaults directory.
- The greeter composition is not an external theme package in this release.
  `Main.qml`, `Login.qml`, `SessionButton.qml`, and `GreeterState.qml` are built
  into `/usr/libexec/plasma-login-greeter` as the
  `org.kde.plasma.login` QML module; the executable loads its main file from a
  `qrc:` URL.
- Therefore wallpaper synchronisation needs no fork, but an approved custom
  login composition cannot be installed as an SDDM-style theme. The smallest
  maintainable implementation is a narrow, versioned downstream QML patch to
  Fedora's PLM source package, re-audited on every Plasma update. Do not replace
  arbitrary files in `/usr` or carry an unversioned greeter binary.
- The pinned Fedora source RPM is
  `plasma-login-manager-6.7.4-1.fc44.src.rpm`, SHA-256
  `d8139ab3fdac94c5361cb0823e229d421d9385efb3dd26e54fd11442eed7ffa6`.
  Its upstream `plasma-login-manager-6.7.4.tar.xz` source is SHA-256
  `8ba5f9a5b31b2cb09d6846c590d09891dadb9a5625426b8552577299093b67fd`.
- The patched package built successfully in the pinned Fedora 44 build
  container. Its `ProperMain.qml` was compiled into the greeter's QML module,
  and the validated
  `plasma-login-manager-6.7.4-1.proper2.fc44.x86_64.rpm` is SHA-256
  `50f91f9acbaa18462fa6938c1446f283edd570ad8604bdf69169c8a0983deab8`.
  Running that package's greeter in offscreen `--test` mode for eight seconds
  produced no QML or runtime errors and remained alive until the test timeout.
- The matching `kcm-plasmalogin-6.7.4-1.proper2.fc44.x86_64.rpm` is SHA-256
  `11478102ebb730821912504d7fc39f99e537b2cdeeb9b7f7656def63b31fc8c8`.
  Both exact packages were installed in the Fedora 44 review VM. Normal login,
  first-character preservation, lock and unlock, pointer opening and closing
  of the icon menu, and its Switch User action all passed against the installed
  system.

## Plasma ShellPackage layout audit — 2026-08-31

- Plasma's visual fallback lets `com.properlinux.desktop` reuse unowned shell
  QML from `org.kde.plasma.desktop`, but the selected ShellPackage ID also owns
  a separate `plasma-com.properlinux.desktop-appletsrc` layout store.
- Proper now seeds that exact store through `/etc/xdg` and `/etc/skel`, with a
  matching `plasmashellrc` view bound to the Proper shell. A one-time Plasma
  update script repairs only an empty existing store and is then recorded by
  Plasma as performed.
- The installed Fedora 44 review VM exposes one 56-pixel, centred, floating,
  fit-content panel with the Vicinae, Dolphin, and Ghostty launchers plus the
  upstream System Tray, Show Desktop, and Digital Clock widgets. The view uses
  Plasma's translucent panel mode; no widget fork or private Plasma API is
  required.
- Icon Tasks groups a Wayland window by the application's own desktop identity.
  Pinning the wrapper `proper-terminal.desktop` launched Ghostty successfully
  but produced a second running icon. Pinning
  `com.mitchellh.ghostty.desktop` preserves the Proper packaging while grouping
  the running window correctly.

## Phase 9 installed shell-surface audit — 2026-08-31

- The installed review covered the configured panel, Vicinae, tray, calendar,
  notifications, Discover's busy state, volume and mute OSDs, connected
  networking, the audio empty state, clipboard, emoji, Polkit success/failure/
  cancellation, Alt+Tab, Overview, Desktop Grid, 200% scaling, and the
  blur-disabled fallback.
- The Fedora/KDE Breeze-derived surfaces remain coherent with Proper Dark and
  retain their upstream pointer, keyboard, accessibility, security, and update
  ownership. No observed failure justifies importing a third-party Global
  Theme or maintaining a forked applet for version 0.1.
- The exact evidence set and its hardware limits are recorded under
  `docs/evidence/phase9-shell-surfaces`.

## Phase 11 workflow and OCR audit — 2026-08-31

- KWin's supported scripting package format and workspace API provide the
  smallest upstream boundary for reversible window arrangement. Proper installs
  one script under `/usr/share/kwin/scripts`, enables it through packaged KWin
  configuration, and exposes registered actions through KGlobalAccel. Sources:
  <https://develop.kde.org/docs/plasma/kwin/> and
  <https://develop.kde.org/docs/plasma/kwin/api/>.
- Vicinae's documented script-command directories and metadata directives are
  used for the promoted desktop actions. Proper installs 15 small scripts under
  `/usr/share/vicinae/scripts`; each delegates to a whitelisted user-session
  helper rather than duplicating privileged logic. Source:
  <https://docs.vicinae.com/scripts/getting-started>.
- The local OCR path uses Fedora repository packages only:
  `tesseract-5.5.3-1.fc44` (Apache-2.0),
  `tesseract-langpack-eng-4.1.0-12.fc44` (Apache-2.0),
  `leptonica-1.87.0-4.fc44` (Leptonica), and
  `wl-clipboard-2.2.1^git20251124.e808203-2.fc44`
  (GPL-3.0-or-later). Their source RPMs are Fedora's corresponding signed
  source packages and updates follow the normal Fedora repository path; no
  external binary or model is pinned into Proper Linux.
- The exact Phase 11 Proper RPMs are
  `proper-defaults-0.1-14.fc44.noarch` (SHA-256
  `25f455b2c950b77a925e7828022a82111a64c06b7a86a0268cecb4e3821d2431`)
  and `proper-launchers-0.1-8.fc44.x86_64` (SHA-256
  `bb9aedf49fb13d2910b9f24bcd1d8432923df8df600fa980200f3ed55985cc65`).
  Both passed RPM digest and payload inspection. They were installed into the
  Fedora 44 reference VM, where arrange, restore, new-window floating
  behaviour, pointer and Vicinae discovery, the shortcut-reference filter,
  Tesseract extraction, and a Wayland clipboard round trip passed. The
  evidence is recorded under `docs/evidence/phase11-workflows`.
