# Phase 4/5 implementation status — 2026-08-26

## Fresh ISO verification attempt

## Continuation evidence — 2026-08-26

The VM-control investigation continued through localhost VNC/RFB, QMP input,
QEMU HMP input, noVNC/websockify, and the host GTK window. Framebuffer capture
is reliable, but pointer delivery is not yet acceptance-grade: QEMU's Wayland
GTK surface ignores host XTest events, the in-app browser cannot reach the
host's loopback namespace, and direct QMP/RFB pointer events produced no
verified guest state change. The exact disposable VMs and proxy processes were
stopped after each test. These paths are diagnostic evidence only; no graphical
journey is marked passed from them.

The VM harness now has a selectable localhost-only VNC backend in
`scripts/run-vm` and a bounded QMP helper in `scripts/vm-input.py`. Harness
commits are `791a2d8` and `b80d154`.

Proper Apps source was corrected so launch uses a detached process rather than
the install progress path, successful operations refresh installed detection,
and Fedora/Flatpak recovery uses provider-specific removal commands. Catalogue
validation passes with `scripts/validate-catalogue`. The focused RPM rebuild
passed in the Fedora 44 builder:

- RPM: `/home/code/Documents/GitHub/proper-linux-build/rpms/proper-apps-focus-1787713228/proper-apps-0.1-2.fc44.x86_64.rpm`
- SHA-256: `4991821f73ebf8a48ce8bb484ca119c12ef91369b3812df856fe25adcf9280b8`
- Source commit: `2c965d8`
- Build result: `qmake6`, `make -j32`, RPM packaging, and `rpm -qpi`/`rpm -qlp` all passed

This RPM is not ISO-integrated and has not yet been visually verified in a
guest. Phase 4 and PM checkpoint 4 remain open.

The supplied completed ISO was verified before testing:

- ISO: `/home/code/Documents/GitHub/proper-linux-build/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.iso`
- SHA-256: `27573b85e899cc83ef7a9457e2a07fcbdcd5fb7d3d91e1dcbba40ea542bc57af`
- manifest spot checks: `proper-terminal 1.2.3-5`, `proper-apps 0.1-2`, LibreOffice absent

A new disposable qcow2 disk was booted with one UEFI QEMU/KVM process at
1920×1080. The live guest reached the branded Proper Linux desktop and the
floating bottom taskbar. The raw and converted display captures are retained
under `/home/code/Documents/GitHub/proper-linux-build/vm/phase45-final.CNgqkx/`:
`live.ppm`/`live.png` capture the boot menu and `boot.ppm`/`boot.png` capture
the live desktop.

The host-side QEMU display capture works, but the available QMP pointer and
keyboard injection did not produce reliable visible interaction in this
guest. Consequently the graphical installer and the requested in-guest
journeys were not completed in this attempt. No success is inferred from
socket commands, package metadata, or source inspection. Phase 4/5 therefore
remains open and no checkpoint approval is claimed.

Checkpoint 3 is approved and remains the regression baseline.

| Area | Source implemented | RPM verified | Fresh-user verified | ISO verified | PM approved |
|---|---:|---:|---:|---:|---:|
| Ghostty/proper-terminal | Yes | Yes (`proper-terminal-1.2.3-1.fc44.x86_64.rpm`) | Yes in development VM | Partial: normal window verified; dropdown toggle regression remains | Not yet |
| Proper Apps catalogue | Yes (latest source includes installed-state detection) | Prior RPM verified; latest source rebuild pending | Yes in development VM (prior source) | Prior UI verified; latest source not integrated | Not yet |

The official Ghostty 1.2.3 source checksum observed during the container build
was `559770fe9773161e93e3dd9177d916e27037d7f548edcf6186eabc571c0e520b`.
The package build uses the official Zig 0.14.1 binary release, verified with
its official minisign signature, because the approved build objective pins
Ghostty 1.2.3 to that compiler. Zig checksum:
`24aeeec8af16c381934a6cd7d95c807a8cb2cf7df9fa40d359aa884195c4716c`.
The resulting proper-terminal RPM checksum from the last fully integrated
image batch is `81c4e4f501ecae02cf6cf78b1fbb8a8d42b7722bf6124038de20eaf9eec2d84c`.
The latest source-only repack used for offline KWin metadata validation is
`a83adff5d4cb4373b04771cc4097b161bbc15b796bfde8042c22529b228f8f78` and is
not an ISO-integrated release artifact.

The development VM installed both RPMs from the deterministic
auxiliary virtio disk. Observed proof includes a normal Ghostty window with
`pwd` output, btop running after terminal sizing, and the graphical Proper Apps
catalogue. The final ISO was then booted in a fresh VM and independently showed
the Proper desktop, Ghostty and Proper Apps catalogue.

Final ISO SHA-256: `533b1be0a9a4fc0b4f19dbf01c3eb6866d70d7a0380a44924decf91345f76848`.
Final Proper Apps RPM SHA-256: `c8dd42933c09a8a566291c130f3ed3e989defd6b195c14a3bb0a2b257821146f`.

Fresh-ISO evidence is under `/home/code/Documents/GitHub/proper-linux-build/vm/final-correct/`:
`final-desktop.png`, `ghostty.png`, `proper-apps-render.png`,
`final-dropdown.png`, `final-marker.png`, and `final-hidden.png`.
The normal Ghostty and Proper Apps journeys pass. The dropdown opens and the
session remains visible, but the current KWin shortcut invocation does not
hide/reopen that same window; this is the genuine remaining checkpoint defect.

The corrected KWin package metadata has since been validated offline with
`kpackagetool6 --type KWin/Script`; it discovers `proper-dropdown`. Fresh
graphical re-verification is pending because the current BOX session exposes
neither `/dev/kvm` nor a usable rootless container namespace.

Phase 4 and checkpoint 4 are not marked complete until the dropdown-session
defect and the remaining launcher/Dolphin/provider journeys are observed and
captured.
