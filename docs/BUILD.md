# Building and updating Proper Linux

For the short agent-assisted installation path, start with the [README](../README.md).
This reference covers build inputs, prerequisites and source-based updates.

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
[`packages/proper-look-and-feel/`](../packages/proper-look-and-feel/), beside the RPM
that installs them. They are ordinary PNG/JPEG files, not assets held only in a
local build directory. The [artwork ledger](../packages/proper-look-and-feel/ARTWORK.md)
lists their names, provenance, licences and SHA-256 checksums.

For example:

- [Highland Sunrise](../packages/proper-look-and-feel/proper-highland-sunrise.png), shown in the README.
- [Highland Blue Hour](../packages/proper-look-and-feel/proper-highland-blue-hour.png).
- [Rally: Night Flight](../packages/proper-look-and-feel/proper-rally-night-flight.png).
- [Salt-Flat Station](../packages/proper-look-and-feel/proper-salt-flat-station.png).

This repository contains Proper's source, packaged artwork, defaults, patches,
image description and build instructions. A checkout is **not an offline build
kit**: the scripts download Fedora packages, pinned source RPMs, container images
and upstream sources. Those services must remain reachable, and the recorded
versions must still be available. No prepared Proper home directory, private
wallpaper folder, existing VM disk or prebuilt Proper RPM repository is required.

## Build environment and commands

You can start from Windows, macOS or Linux. The commands below run in an
x86-64 Linux build environment; Fedora 44 is the current development environment.
Your agent can arrange a suitable Linux VM or an accessible remote Linux
builder when your computer cannot run the build directly. On ARM machines,
such as Apple silicon Macs, use an x86-64 builder or compatible emulation;
an ARM Linux VM alone does not meet the current build requirements.
The installation image currently targets x86-64 PCs.
The RPM build uses Podman and host RPM tools. ISO composition additionally needs
privileged KIWI access, either on the host or through the supplied Podman builder.
A restricted container without the required privileges is not sufficient.
Graphical review needs QEMU/KVM, UEFI firmware and a graphical display; a
VM-based builder needs nested virtualization for that review, or a separate
review machine with KVM access. Verify these capabilities before building.

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

## Agent: handle setup and recoverable failures

The user is asking to try Proper, not to maintain a build environment. Install
missing prerequisites in the chosen builder, diagnose failures from the logs,
and retry routine repairs without asking the user to interpret tool errors.
Obtain any required system permissions normally. Do not weaken checks to make
a build appear successful.

- For a temporary download failure, retry before changing an input.
- For a missing source archive or RPM, look for the exact pinned input on its
  official upstream archive or build service and retain checksum verification.
- For a removed Fedora build-container manifest, follow
  [the builder update procedure](../image/BUILDERS.md). Use an official x86-64
  container from the same Fedora release, verify it, and record its exact
  digest. This is a local build repair; it does not authorize upgrading Proper
  to another Fedora release or replacing its patched KDE versions.
- Keep repairs in the checkout and save a patch alongside the build log and
  original Git revision. Retry the build and all affected checks. Report the
  resulting image as built from that revision **plus the recorded patch**.
  A modified checkout is not the unchanged signed release.
- If recovery needs a different Fedora release, substantial source changes,
  unavailable hardware or access the agent lacks, explain the specific blocker
  and the simplest next step in plain language. Never skip failed validation,
  substitute unverified downloads, or claim an untested USB is ready.

For Windows or macOS, preparing the Linux builder is part of the agent's work.
It must establish that the VM or remote builder is actually usable, including
the required privileges and architecture, rather than merely telling the user
to run Linux commands on their host.

## Prepare the installation USB

When building in a VM or remotely, copy the ISO and its checksum to the computer
with the USB drive attached, and verify the transferred ISO. USB writing can
happen on Windows, macOS or Linux using a disk-image writer appropriate to that
platform. Write the image to the whole USB drive rather than copying the ISO
file onto its filesystem.

Identify the drive by model, capacity, serial number where available and device
path. Obtain explicit confirmation of the exact target and its erasure before
writing. Verify the written image against the ISO and safely eject the drive.
The resulting USB can then boot a compatible x86-64 PC into the live installer.
