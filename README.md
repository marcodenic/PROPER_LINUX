# Proper Linux

> Normal Linux. Properly finished.

![Proper Linux desktop](artwork/previews/proper-linux-desktop.png)

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

## Build and run

The image build requires an x86-64 Linux environment with privileged KIWI or
Podman support. Graphical validation additionally requires QEMU/KVM.

```bash
scripts/check-box
scripts/build-iso
scripts/run-vm /absolute/path/to/Proper-Linux.iso
```

`scripts/check-box` writes a host-capability report and does not install or
change anything. An agent should resolve any reported build prerequisites,
read `AGENTS.md`, and then use the commands above without committing generated
artifacts.

Build output is written outside the repository to `../proper-linux-build` by
default. A successful build emits the ISO and its SHA-256 checksum; a release
is not considered usable until the ISO also installs and boots in a fresh VM.

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
