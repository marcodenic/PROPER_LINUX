# Proper Linux

> Normal Linux. Properly finished.

Proper Linux is Fedora KDE with the rough edges worked on: frosted window
materials, a calmer taskbar, cleaner settings, thoughtful typography and
wallpapers, and less clutter between you and what you came to do.

From login to everyday work, the aim is a desktop that feels considered.
Windows move and resize normally, shortcuts are optional, and Fedora stays
fully available underneath.

![Proper Linux desktop with Highland Sunrise wallpaper and a translucent terminal](artwork/previews/proper-linux-desktop.png)

## Try it

Proper is currently a **development preview**, built from source rather than
downloaded as a prebuilt ISO. Give the prompt below to a coding agent with
terminal access on Windows, macOS or Linux. Your agent handles setup, building,
and preparing the USB; you don't need to know how to build a Linux distribution.
You’ll need internet access and a USB
drive you are happy to erase. Proper currently targets x86-64 PCs.

```text
Help me build Proper Linux and prepare an installation USB:
https://github.com/marcodenic/PROPER_LINUX

Clone the repository, read AGENTS.md, docs/PRODUCT.md and
docs/ARCHITECTURE.md, and record the revision being built.
Check my platform and use docs/BUILD.md to arrange a suitable x86-64
Linux build environment, locally, in a VM or on an accessible remote
machine. I do not need to already be running Linux. Run scripts/check-box
inside that environment, read its report and resolve the prerequisites.
Handle routine setup and build troubleshooting yourself. If a download is
unavailable, follow the recovery instructions in docs/BUILD.md, record any
local fixes and retry. Don't make me diagnose build tools or broken links.

Build with scripts/build-iso using the pinned inputs and full default
package set. Keep outputs outside the checkout. Check the resulting
ISO and checksum, and validate installation and boot using the
repository's disposable VM review instructions.

If built remotely or in a VM, copy the ISO and checksum back to my
computer and verify the transfer. Identify my USB drive by model,
capacity, serial number and device
path. Explain that writing the image erases it, and get my explicit
confirmation of that exact drive before writing anything. Never
select the system disk. Write the ISO as a bootable disk image,
verify the written bytes against the ISO, and safely eject it.

Tell me how to boot the USB and start the installer. Report the ISO
path, revision, any local fixes, checksum and checks completed. If you cannot
resolve a blocker, explain in plain language what I need to do next; do not
claim the USB is ready. Do not commit or push.
```

## More

[What we’re changing](docs/PRODUCT.md) ·
[Build and update details](docs/BUILD.md) ·
[Architecture](docs/ARCHITECTURE.md) ·
[Included wallpapers and licences](packages/proper-look-and-feel/ARTWORK.md)
