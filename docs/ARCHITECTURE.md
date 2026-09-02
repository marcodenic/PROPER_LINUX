# Proper Linux architecture and delivery

## Objective

Proper Linux is a conventional, mutable Fedora KDE live image. The experience
is built from versioned RPMs, assets, catalogue data, and image configuration;
it is never defined by copying a prepared user's home directory.

Fedora 44 supplies the x86-64 kernel, drivers, Wayland, systemd, Plasma, KWin,
networking, security, installer, package system, and updater. The Fedora KDE
KIWI definition is pinned to an immutable upstream revision, then overlaid with
the smallest practical set of Proper packages and image changes.

This boundary exists so Proper can own taste and integration while Fedora and
KDE continue to deliver their mature infrastructure and security updates.

## Ownership rules

- Prefer configuration, themes, supported extension points, and small
  integration packages over forks.
- Keep each visible choice in one owning package and derive shared visual
  assets from `packages/proper-look-and-feel/tokens.yaml`.
- Seed new-user defaults through system configuration and `/etc/skel`; use a
  narrow migration only when an existing Proper default genuinely needs repair.
- Never overwrite a later user choice simply because a package was updated.
- Keep upstream applications and applets independently updateable unless a
  documented product requirement cannot be met through a supported surface.
- Pin external build inputs. Keep their source, checksum, licence, patch, and
  update method beside the relevant spec or lock file instead of in a separate
  prose log.

## Repository map

| Area | Responsibility |
| --- | --- |
| `image/` | Pinned Fedora KIWI input, Proper image overlay, live-session integration, and VM firmware used for controlled review |
| `packages/proper-release/` | Product identity, release metadata, repository configuration, and Fedora derivative boundary |
| `packages/proper-branding/` | Boot, installer, system-logo, and platform artwork |
| `packages/proper-look-and-feel/` | Design tokens, global themes, Plasma Style, wallpapers, lock screen, colours, and generated shared UI assets |
| `packages/proper-appearance/` | Preview-first style, text-size, and wallpaper control plus the bounded login-wallpaper helper |
| `packages/proper-defaults/` | Panel, KWin, shortcuts, Files, natural scrolling, default applications, and narrowly scoped migrations |
| `packages/proper-launchers/` | Pinned Vicinae build, reliable opener, desktop actions, arrangement, OCR, and shortcut reference |
| `packages/proper-terminal/` | Pinned Ghostty build, terminal defaults, `btop`, and Files integration |
| `packages/proper-apps/` | Curated catalogue UI, provider execution, state reconciliation, web apps, and agent selection |
| `packages/proper-welcome/` | Passive Start Here hub and live install entry point |
| `packages/plasma-login-manager/` | Fedora source-package pin and the narrow Proper login composition patch |
| `packages/plasma-desktop/` | Fedora source-package pin and the narrow task-launch indicator patch |
| `apps/` | Catalogue schema and data plus the application-icon provenance ledger |
| `artwork/` | Shipped identity, wallpaper, and preview assets |
| `scripts/` | Build, validation, VM, and source-pinning tools |

Package specs, lock files, catalogue data, and artwork ledgers are the
authoritative record for exact versions and provenance.

## Desktop implementation

### Plasma and KWin

Proper uses Plasma's global themes, Plasma Style, panel configuration,
ShellPackage support, KWin shortcuts, and scripts. The floating shelf, common
shell controls, notifications, tray, OSDs, overview, network, Bluetooth, audio,
power, and authentication keep their upstream behaviour. Missing Proper theme
assets fall back to Breeze.

Windows remain in KWin's normal floating model. Snapping and native tiling are
configured defaults; Arrange Workspace is a reversible KWin script that affects
only eligible windows on the current workspace and display.

### Deliberate source-package exceptions

Two small patches exist because the required presentation is not exposed by a
supported theme hook:

- Plasma Login Manager 6.7.4 embeds its greeter composition in the executable.
  Proper rebuilds Fedora's exact source RPM with one entry-point QML patch while
  retaining upstream authentication, session, accessibility, power, service,
  and package behaviour.
- Plasma Desktop 6.7.4 does not expose a task-specific startup-indicator theme
  hook. Proper carries one QML patch for the shelf's restrained launch state
  without changing the system-wide busy indicator.

Each exception is version-pinned, checksum-verified, built as a normal RPM, and
must be rebased and retested when Fedora updates its source. It should be
dropped if upstream provides a suitable supported extension point.

### Applications and providers

`apps/catalogue-v2.json` is a product manifest, not a repository. Each entry
records its identity, presentation, provider, maintenance status, architecture,
licence, install detection, launch, update, removal, caveats, and validation
date. `apps/icon-sources.json` records recognisable artwork provenance and
checksums.

Provider preference is:

1. verified or upstream-maintained Flatpak;
2. Fedora RPM;
3. official vendor repository or package;
4. clearly labelled community package; and
5. a reversible custom integration only when no better path exists.

Proper Apps runs allow-listed commands without a shell, uses the system's
normal privilege prompt, never pipes remote scripts into a privileged shell,
and checks real installed state after a provider exits. Optional software keeps
the update mechanism of its chosen provider.

## Builds, updates, and releases

`scripts/build-iso` checks out the pinned Fedora image definition, builds the
current Proper RPM set, creates a local repository, composes the image through
KIWI, validates its package manifest, and writes a SHA-256 checksum. Generated
ISOs, RPMs, VM disks, caches, logs, and downloaded archives stay outside Git.

The ISO is a tested installation snapshot, not the update mechanism. Installed
systems receive Fedora packages from Fedora and Proper-owned RPMs from the
configured hosted repository through ordinary DNF, PackageKit, and Discover
flows. Optional applications update through their selected provider. A new ISO
is needed for a release snapshot, Fedora rebase, installer or live-image change,
package-set change, or early-boot repair—not for every theme or application
update.

Public artifacts require a source tag, package manifest, release notes,
checksum, signature, and no embedded credentials. Production publishing
credentials must never be exposed to untrusted pull-request code.

## Development and verification

Use the cheapest loop that can answer the question:

1. Prototype a visual or interaction change in a disposable development
   session.
2. Promote the intentional settings or code into the owning RPM and test both
   a new user and a user with custom settings.
3. Rebuild the ISO when image composition, boot, login, live behaviour,
   installer behaviour, or the complete installed journey is in scope.

A package compiling is not proof that the product works. A release candidate
must, from the committed repository:

- produce exactly one x86-64 ISO and checksum with the expected package set;
- boot a graphical UEFI live session in QEMU/KVM;
- install through the included graphical installer to a blank disk;
- boot the installed disk after installation media is removed;
- preserve Fedora networking, updates, System Settings, and package behaviour;
- exercise the shelf, launcher, Files, window arrangement, Ghostty, Proper Apps,
  appearance controls, and user-setting persistence with pointer and keyboard;
- remain legible at 100% and 200% scale, with blur disabled, and on focused
  multi-display and rotated-display checks; and
- contain no secret, token, private key, proprietary credential, or unexpected
  bundled application stack.

Graphical actions must be verified from the resulting screen state rather than
inferred from a successful input command. User-facing visual judgement belongs
to the product manager.

## Security and scope

Proper uses signed Fedora repositories, verified publishers, explicit package
operations, and ordinary privilege boundaries. Agent clients run as the user
and keep their normal provider authentication. The bounded wallpaper helper
accepts only packaged wallpaper identifiers and never an arbitrary path or
command.

Version 0.1 inherits Fedora's general x86-64 support but is validated as a
desktop product rather than a hardware-certification programme. It does not
create a new installer, updater, package manager, compositor, kernel, public
mirror, server edition, gaming edition, or atomic edition.

## Keeping this documentation current

Update `PRODUCT.md` when a user-visible principle, default, or product boundary
changes. Update this file when ownership, packaging, build, update, security, or
verification architecture changes. Record exact versions, checksums, licences,
and implementation notes next to their code and data, where they can be checked
and updated without growing another historical document.
