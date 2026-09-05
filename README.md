# Proper Linux

> Normal Linux. Properly finished.

![Proper Linux desktop with Highland Sunrise wallpaper and a translucent terminal](artwork/previews/proper-linux-desktop.png)

*Development desktop with the included Highland Sunrise wallpaper.*

Proper Linux is a lean, opinionated Fedora KDE desktop. It keeps Fedora's
normal mutable system and concentrates on the part people actually live in:
the desktop, its defaults, and the small interactions that make a computer
feel calm and deliberate.

The point is not to hide Linux or replace working infrastructure. The point is
to remove clutter, duplication, setup ceremony, and needless choices while
leaving the underlying system fully available.

## What makes it Proper

- A coherent dark desktop with curated wallpapers, clear typography,
  natural scrolling, selective translucency, and sensible settings from the
  first login.
- A quiet floating shelf with useful task states and familiar system controls,
  without redundant bars, launchers, hover noise, or decorative clutter.
- Vicinae as one polished place to browse apps, search, run actions, and reach
  common desktop tools with either pointer or keyboard.
- Normal floating windows, excellent snapping, a reversible arrangement tool,
  and concise shortcuts that accelerate rather than define the workflow.
- A simplified Dolphin experience, Ghostty 1.3.1 and `btop`, Chromium as the
  promoted browser, and a small set of genuinely useful defaults.
- Proper Apps: a broad optional catalogue that asks which product the user
  wants instead of making package formats the main decision.
- Proper Appearance with desktop-style previews, text sizing and a compact
  wallpaper gallery; Start Here with everyday settings and an offline help guide.
- Easy access to coding agents as ordinary user applications.
- A build-enforced sub-3 GiB image with no bundled office suite, duplicate
  application stacks, games, or promotional welcome software simply because an
  upstream edition included them.

Proper Linux is still Fedora underneath: kernel, drivers, networking,
security, installer, updates, DNF, Flatpak, System Settings, and the normal
ability to change any default remain intact.

## Status

Proper Linux is in development. Version 0.1 will be an agent-assisted
source-build preview, not a hosted ISO release.

## How distribution works

Proper Linux is source-distributed from this Git repository. Preview releases
are signed Git tags, and a separate Proper package or ISO server is not
required:

1. GitHub supplies Proper's signed release source, patches, assets, and build
   rules.
2. A user or their agent verifies and checks out the selected release tag.
3. Fedora supplies the base packages and pinned source RPMs.
4. Upstream projects supply the checksum-verified external sources recorded by
   the relevant Proper package.
5. `scripts/build-rpms` creates a local RPM-MD repository outside the checkout.
6. `scripts/build-iso` embeds that local repository into the generated ISO.

After installation, Fedora continues to provide ordinary system and security
updates through DNF, PackageKit, and Discover. Flatpak and vendor-managed
software retain their normal update services. Proper-specific updates are new
signed source releases; they are never pulled automatically from the moving
development branch.

For an announced Proper update, the user or their agent verifies and checks out
the named release tag, reads its release notes, and then runs:

```bash
scripts/update-installed --dry-run
scripts/update-installed
```

The release instructions identify the tag and signing key; `git verify-tag`
must succeed before either command is run. The updater then verifies that the
installed Fedora/Plasma source versions still match Proper's pinned patches,
builds a local RPM-MD repository, and installs the resulting Proper RPMs
through DNF. It stops on an incompatible Plasma update instead of silently
reinstalling stale code. Updating an installed system does not rebuild or
reinstall the ISO, and it never replaces Fedora's normal update path.

## Wallpapers and build inputs

All **13 shipped wallpapers** are checked into
[`packages/proper-look-and-feel/`](packages/proper-look-and-feel/), beside the RPM
that installs them. They are ordinary PNG/JPEG files, not assets held only in a
local build directory. The [artwork ledger](packages/proper-look-and-feel/ARTWORK.md)
lists their names, provenance, licences and SHA-256 checksums.

For example:

- [Highland Sunrise](packages/proper-look-and-feel/proper-highland-sunrise.png), shown above.
- [Highland Blue Hour](packages/proper-look-and-feel/proper-highland-blue-hour.png).
- [Rally: Night Flight](packages/proper-look-and-feel/proper-rally-night-flight.png).
- [Salt-Flat Station](packages/proper-look-and-feel/proper-salt-flat-station.png).

This repository contains Proper's source, packaged artwork, defaults, patches,
image description and build instructions. A checkout is **not an offline build
kit**: the scripts download Fedora packages, pinned source RPMs, container images
and upstream sources. Those services must remain reachable, and the recorded
versions must still be available. No prepared Proper home directory, private
wallpaper folder, existing VM disk or prebuilt Proper RPM repository is required.

## Build and run

Use an x86-64 Linux host; Fedora 44 is the current development environment.
The RPM build uses Podman and host RPM tools. ISO composition additionally needs
privileged KIWI access, either on the host or through the supplied Podman builder.
A restricted container without the required privileges is not sufficient.
Graphical review needs QEMU/KVM, UEFI firmware and a graphical display.

Clone the repository and enter it:

```bash
git clone https://github.com/marcodenic/PROPER_LINUX.git
cd PROPER_LINUX
scripts/check-box
```

Read the generated host report at `/tmp/proper-linux-build-environment.md`.
It reports capabilities; it neither installs prerequisites nor guarantees that
all build dependencies are present. The scripts also check their required tools.
Host tools include Git, Podman, RPM build/extraction tools, curl, cpio, patch,
Python 3 with PySide6, XML tools, ImageMagick, desktop-file validation, fontconfig,
dracut's `lsinitrd` and xorriso. Package-specific build dependencies are described
in the RPM specs and supplied builder containers.

For a development build, record the exact revision and build:

```bash
git rev-parse HEAD
scripts/build-iso
```

`build-iso` builds the Proper RPMs itself; a separate `build-rpms` run is not
needed first. Keep the default full package set for a fresh build. Output goes
to `../proper-linux-build` by default; set `PROPER_OUTPUT_DIR` to an absolute path
if another location is needed. The script reports the ISO path and emits its
SHA-256 checksum. To review that image:

```bash
scripts/run-vm /absolute/path/to/Proper-Linux.iso
```

Use the default single-display, 1920×1080 graphical VM configuration. Building
successfully is not installation evidence: install to a disposable VM disk,
boot the installed system and check the graphical desktop before describing an
image as installation-tested. Never use a real disk for this review.

For an announced release, verify its named signed tag and check it out before
building, using the signing-key instructions accompanying that release. The
moving `main` branch is development source, not a verified release.

### Instructions to give your coding agent

Copy this brief into your agent from the checkout:

> Build a Proper Linux development ISO from this repository. Read `AGENTS.md`,
> `docs/PRODUCT.md` and `docs/ARCHITECTURE.md` first. Record the Git revision and
> any local changes. Run `scripts/check-box`, read its report and resolve the
> host prerequisites; explain any privileges or external access you cannot
> obtain. Use the repository's pinned inputs and `scripts/build-iso` with the
> full default package set. Do not substitute newer dependencies, invent missing
> assets or depend on another developer's cache. Keep generated outputs outside
> Git. Report the resulting ISO path, checksum and build outcome. If graphical
> validation is available, use only `scripts/run-vm` with its default fullhd
> configuration, install to a disposable VM disk and verify installed boot and
> everyday pointer actions with screenshots and the `scripts/verify-ux` gate.
> Distinguish a successful build from installation and graphical validation;
> report exactly what was and was not checked. Do not commit, push, publish a
> release or write to a physical disk.

## Documentation

- [Product and experience](docs/PRODUCT.md) — what Proper Linux is, what it
  changes, and why those choices matter.
- [Architecture and delivery](docs/ARCHITECTURE.md) — how the product is built,
  packaged, updated, and verified.

## Product rule

Preserve Fedora unless a user can see the problem, feel the problem, or is
unnecessarily forced to understand the problem.

## Naming and licensing

“Proper Linux” remains a working name pending formal trademark review. The
project will remain publicly source-distributed and open source. Component
licences and asset provenance are recorded beside the packages and files they
govern.
