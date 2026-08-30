# Proper Linux architecture

## Architectural objective

Produce a conventional, mutable Fedora KDE live image whose Proper Linux experience is defined by versioned packages and image configuration—not by manually changing a reference user's home directory.

The architecture should make visible product work easy to iterate while delegating operating-system plumbing to Fedora and KDE.

## Base system

### Distribution

- Fedora KDE Plasma Desktop
- Mutable/package-based edition
- x86-64 first
- Wayland and systemd as supplied by Fedora
- Fedora repositories and update mechanism retained

Version 0.1 targets Fedora Linux 44 because it is the current stable Fedora release at project inception. Each Proper Linux release must pin a Fedora major version; moving to a later Fedora is an explicit release task, not an unreviewed rolling change.

### Why not Fedora Atomic

Atomic Fedora provides excellent image-level updates and rollback, but it changes how technically capable users install system packages and modify the host. Proper Linux version 0.1 intends to preserve familiar `dnf` and mutable-system behaviour. Atomic delivery can be reconsidered only after the desktop product exists.

### Why not Arch/Omarchy as the base

Proper Linux borrows Omarchy's curation and useful shortcut ideas, not its package lifecycle or Hyprland operating model. Fedora KDE already supplies the conventional desktop, graphical installer, Wayland stack, and mutable package system required by the product.

## Image construction

Fedora's current package-based live media is built with KIWI. Proper Linux should:

1. pin the upstream Fedora KDE live-image description for the selected Fedora release;
2. carry the smallest possible Proper-specific overlay;
3. build the live ISO on BOX using KIWI directly or through a privileged build container;
4. keep the complete build definition in Git;
5. produce a checksum beside every local ISO artifact; and
6. install and boot the result under QEMU/KVM.

Do not begin new work around legacy `livecd-creator` or an Arch `archiso` profile. Keep a fallback branch or documented experiment only if KIWI proves blocked on the actual BOX host.

KIWI needs image-building privileges, loop devices, and filesystem tooling. Containerising the build is useful for repeatable dependencies, but it does not remove those host requirements.

## Development feedback loops

Visible work uses three increasingly expensive loops: direct iteration in a
dedicated development VM account, RPM installation into that VM, and complete
ISO composition. The ISO loop is reserved for image integration, arrival and
checkpoint validation rather than routine styling changes.

The complete promotion and verification procedure is in
`docs/UI_ITERATION.md`. Regardless of which loop is used, committed packages
and image configuration remain the source of truth.

## Planned repository layout

```text
PROPER_LINUX/
├── AGENTS.md
├── README.md
├── docs/
├── image/
│   ├── descriptions/       # Proper KIWI overlay / pinned Fedora base
│   ├── config/             # Image-time configuration
│   └── repositories/       # Local package repository metadata
├── packages/
│   ├── proper-release/
│   ├── proper-look-and-feel/
│   ├── proper-defaults/
│   ├── proper-launchers/
│   ├── proper-terminal/
│   └── proper-apps/
├── apps/
│   ├── catalog.yaml
│   ├── schemas/
│   └── sources/
├── artwork/
│   ├── identity/
│   ├── wallpapers/
│   └── previews/
├── scripts/
│   ├── bootstrap-box
│   ├── build-iso
│   ├── run-vm
│   └── capture-checkpoint
└── tests/
    ├── image/
    ├── vm/
    └── smoke/
```

Create directories only when their phase starts; this tree is a boundary map, not a requirement for empty scaffolding.

## Package boundaries

### `proper-release`

Owns product identity and release metadata:

- `/etc/os-release` integration
- product name/version data
- release-specific repository configuration
- generic system-logo providers required for rebranding
- legal attribution and release metadata

It must comply with Fedora's remix and trademark rules. Proper Linux should describe itself as independent and derived from Fedora, never as an official Fedora edition.

### `proper-look-and-feel`

Owns system-wide visual assets:

- Plasma Global Theme
- colour schemes
- Plasma style overrides where needed
- wallpaper package
- lock-screen defaults
- splash assets
- cursor/icon selection configuration
- Plasma Login Manager supported branding/defaults

Prefer configuration and original assets over patching upstream QML.

### `proper-defaults`

Owns behavioural defaults:

- initial Plasma panel layout
- taskbar configuration
- KWin/window-management defaults
- keyboard shortcuts
- file-manager defaults
- default applications
- first-login migrations when genuinely necessary

Defaults apply to new profiles. Updates must not continually reset user choices. Use KDE configuration defaults, Plasma layout scripting, and narrowly scoped migrations instead of copying a whole prepared home directory.

### `proper-launchers`

Owns integration rather than upstream launcher source where possible:

- Vicinae package/repository or pinned build
- Proper taskbar launcher action
- `Meta+Space` and fallback shortcut bindings
- initial Vicinae favourites, theme, and script commands

If either upstream component requires a patch, carry it separately with an upstream reference and exit plan.

### `proper-terminal`

Owns:

- Ghostty package/source selection
- default Ghostty configuration
- shell presentation that does not replace the user's shell unnecessarily
- ordinary taskbar launcher
- Dolphin “Open terminal here” integration
- `btop`

### `proper-apps`

Owns the curated application-directory UI and provider adapters. The catalogue data lives separately under `apps/` so products can be added or corrected without redesigning the interface.

## Desktop stack

### Plasma and KWin

Use supported Plasma 6 extension points:

- Global Theme packages
- Plasma panel/layout scripting
- Plasma widgets
- KWin shortcuts and scripts
- KDE defaults and configuration modules

Do not replace Plasma or KWin for version 0.1. A shell replacement would discard exactly the mature mouse and floating-window behaviour Proper Linux wants to preserve.

### Taskbar

Prototype with the native Plasma panel in floating, fit-content form plus supported widgets. Validate whether it can provide:

- central pinned/running applications;
- a Proper/Vicinae launcher;
- an ordinary pinned Ghostty launcher;
- system tray and clock; and
- correct floating/translucent appearance.

Only introduce a custom panel/shell if the prototype fails an explicit acceptance criterion.

### File manager

Dolphin is the version 0.1 baseline because it is current in Fedora 44, native to Qt/KDE, and already integrates KIO remote locations, removable devices, previews, tabs, split views, plugins, trash/undo, and Plasma defaults.

Proper Linux should make it look and behave deliberate through `proper-defaults`:

- simplified toolbar and hidden optional panels;
- friendly “Files” launcher name;
- approved view, spacing, sidebar, preview, and click defaults;
- Ghostty context/action integration; and
- no wholesale copy of a prepared user's Dolphin state.

At PM checkpoint 2, compare the configured result against current Nautilus and COSMIC Files in the same Plasma VM. Replacing Dolphin is allowed only if the candidate passes the file-manager checks in `ACCEPTANCE.md` and does not create obvious toolkit/theme or desktop-integration regressions.

### Login manager

Fresh Fedora KDE 44 uses Plasma Login Manager (PLM). Proper Linux will standardise on PLM rather than reintroducing SDDM.

PLM runs as its own `plasmalogin` system user. Therefore:

- ship the default Proper wallpaper and theme system-wide;
- configure the greeter through PLM's supported settings;
- use PLM's display-settings synchronisation for an installed user;
- investigate carrying the live installer display layout into the target installation; and
- avoid blindly copying arbitrary user home configuration into the greeter account.

Physical monitor rotation cannot always be inferred from hardware data. The acceptance requirement is that a layout selected during install can be applied to the first login, not that the OS guesses how every monitor is mounted.

## Window management

KWin remains in its normal floating mode. Proper Linux configures:

- mouse edge and corner snapping;
- visual tiling feedback;
- `Meta`+arrow quick-tile shortcuts;
- maximise/restore/minimise behaviour; and
- selected non-conflicting Omarchy-inspired bindings.

An automatic tiling KWin script is optional and post-0.1 unless an existing upstream component proves low-risk and excellent with a mouse. It must never replace ordinary floating behaviour.

## Application delivery

### Default applications

Default applications come from Fedora packages or a Proper-managed RPM when tight desktop integration requires it. Large optional applications stay out of the base image.

### Curated catalogue

The catalogue is a product manifest, not a package repository. Each entry records:

- stable application identifier;
- display name and description;
- category;
- icon source and licence;
- install provider;
- provider-specific identifier;
- architecture availability;
- whether the source is official, upstream-maintained, or community-maintained;
- uninstall and launch information; and
- any unavoidable caveat.

Provider preference:

1. well-maintained Flatpak from the application's verified publisher;
2. Fedora RPM;
3. official vendor repository/package;
4. clearly identified community package when no official Linux release exists;
5. AppImage or custom installer only as a last resort.

The normal UI exposes one Install action. Advanced details expose the selected source.

## AI integration

Version 0.1 installs or launches agent clients as ordinary user applications. Vicinae commands may open the selected agent in Ghostty. Proper Apps may manage installation and direct users into official authentication flows.

There is no privileged agent daemon, shared credential store, or automatic root authority in version 0.1.

## Installation and updates

- Retain Fedora's Anaconda-based installation experience as supplied by the KDE live image.
- Apply only necessary Proper product naming, artwork, package selection, and display-layout integration.
- Retain Fedora/DNF/PackageKit/Discover update mechanisms.
- Proper packages update through a small repository only when public distribution begins. Early prototypes may embed locally built RPMs in the image.

## Test architecture

### Build validation

- Validate KIWI configuration.
- Build all Proper RPMs from clean sources.
- Verify the ISO checksum and expected file type.
- Ensure no secrets or private signing material appear in artifacts.

### VM validation

- Boot with UEFI firmware under QEMU/KVM.
- Exercise the live session.
- Install to a blank virtual disk.
- Reboot from the installed disk.
- Capture the five visual checkpoints.
- Run focused smoke checks for launchers, window snapping, Ghostty, software installation, and updates.

This is targeted product verification, not a promise of broad hardware certification.

## Security and trust

- Build inputs and external packages must be pinned and documented.
- Prefer signed upstream repositories and verified Flatpak publishers.
- Never run opaque remote shell installers from Proper Apps.
- Installation actions use existing privilege mechanisms and display the expected authentication prompt.
- AI tools run with normal user permissions unless the user explicitly approves escalation.
- Public ISO releases require checksums and signatures; local prototypes require checksums.

## Release identity and trademark boundary

Proper Linux uses its own name, logos, wallpaper, and release metadata. Fedora's official logo and primary marks must not imply that Proper Linux is an official Fedora product. Before distributing a public ISO, audit and replace packages/assets required by Fedora's remix guidelines and include correct attribution.
