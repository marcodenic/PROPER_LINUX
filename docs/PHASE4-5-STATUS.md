# Phase 4/5 implementation status — 2026-08-26

## Current integration artifact

The current source state has been promoted through a full ISO rebuild.

- Branch: `codex/complete-phase-4-and-5`
- ISO: `/home/code/.codex/worktrees/7b43/proper-linux-build/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.iso`
- ISO SHA-256: `0760160f9b94a84e62ec957a30464d2ff0fed132ebf6ff4af32f61b22ea96daa`
- Package manifest: `/home/code/.codex/worktrees/7b43/proper-linux-build/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.packages`
- Manifest checks: `proper-apps-0.1-2.fc44.x86_64`, `proper-terminal-1.2.3-5.fc44.x86_64`, and no LibreOffice package.

The focused Proper Apps RPM build passed with qmake6, make, rpmbuild, and RPM
metadata/file-list inspection. It is an intermediate build, not the release
ISO artifact:

- RPM: `/home/code/.codex/worktrees/7b43/proper-linux-build/rpms/proper-apps-recovery-fix-1787715600/proper-apps-0.1-2.fc44.x86_64.rpm`
- RPM SHA-256: `d7f437ffa429f849f4002dfa78f5e3c188d541082499676a0d2ce92df89d88d8`

## VM-control evidence

`scripts/run-vm` supports a localhost-only VNC backend and selectable tablet or
relative pointer mode. `scripts/vm-input.py` sends bounded QMP keyboard and
absolute-pointer events. The harness has been syntax-checked and disposable
UEFI/KVM guest lifecycle tested.

Fresh integrated-ISO boot evidence:

- Desktop: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/checkpoint4-1787714419/desktop.png`
- Desktop SHA-256: `e596905dde724e8c711bd50dbbde1bc6c0693e867047d2d65b753fbb9b88afaa`
- Fresh post-promotion desktop: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/recovery-1787716000/hmp.png`

Fresh graphical input evidence using relative VNC mode:

- Terminal opened by taskbar click: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/relative-1787714591/terminal-click.png`
- Unique marker typed into the visible terminal: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/relative-1787714591/marker.png`
- Marker screenshot SHA-256: `fcf87b314c71c4fbc694d3e84a66adfd60542be82b67f9df13c1b18b5cb1b56a`

The fresh post-promotion capture proves the new ISO boots to the branded
desktop. The earlier captures prove a working graphical control path for the
demonstrated actions.
They do not prove the complete Phase 4 journey; relative coordinates must not
be treated as absolute coordinates between sessions.

## Source changes included in the ISO

Proper Apps launch is separate from installation progress; successful
operations refresh installed detection; and recovery uses provider-specific
Flatpak or Fedora removal commands, with an explanatory vendor fallback.
`scripts/validate-catalogue` passes.

## Acceptance matrix

| Criterion | Evidence state |
|---|---|
| ISO boots to Proper desktop | Passed; fresh screenshot above |
| Pointer control and visible typing | Passed for the demonstrated relative-VNC path |
| Retained dropdown Ghostty session | Open; not freshly reverified on this ISO |
| Dropdown hide/reopen and Meta+J | Open |
| btop renders | Open for current release-ISO journey |
| Dolphin “Open terminal here” | Open |
| Vicinae actions use Ghostty | Open |
| Fresh-user defaults and upgrade persistence | Open for current release-ISO evidence |
| Catalogue home/category/search/detail | Open for current release-ISO evidence |
| Install progress and installed state | Open for current release-ISO evidence |
| Launch and provider-specific recovery | Open for current release-ISO evidence |
| Intentional failure and advanced source details | Open |
| Fedora, Flatpak, vendor, and agent paths | Open |
| PM checkpoint 4 | Not approved |

No completion claim is based solely on source inspection, package metadata,
QMP command success, or historical screenshots.

## Remaining work

Continue with fresh disposable guests booted from the ISO above. Capture the
remaining acceptance journeys, update this matrix with paths and checksums,
and stop at PM checkpoint 4. Do not begin Phase 6.
