# Phase 4/5 implementation status — 2026-08-26

## Current integration artifact

The current source state has been promoted through a full ISO rebuild.

- Branch: `codex/complete-phase-4-and-5`
- ISO: `/home/code/.codex/worktrees/7b43/proper-linux-build-icons/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.iso`
- ISO SHA-256: `6470b8410607790e73e558e703572b2ab71f200459dd2ee94470e2719fcf2aaf`
- Package manifest: `/home/code/.codex/worktrees/7b43/proper-linux-build-icons/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.packages`
- Manifest checks: `proper-apps-0.1-2.fc44.x86_64`, `proper-terminal-1.2.3-5.fc44.x86_64`, and no LibreOffice package.

The focused Proper Apps RPM build passed with qmake6, make, rpmbuild, and RPM
metadata/file-list inspection. It is an intermediate build, not the release
ISO artifact:

- RPM: `/home/code/.codex/worktrees/7b43/proper-linux-build-icons/rpms/proper-apps/RPMS/x86_64/proper-apps-0.1-2.fc44.x86_64.rpm`
- RPM SHA-256: `c1dd255a4ac9156745a39f3c166661add88bbf72e139df6307b6d3dc4e36fbbf`

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

Fresh graphical input evidence using the tablet VNC path on the promoted ISO:

- Terminal opened by absolute tablet click: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/tablet-1787716500/click.png`
- Marker/session evidence: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/tablet-1787716500/reopened.png`
- Hide/reopen evidence: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/tablet-1787716500/hidden.png` and `reopened.png`
- Rendered btop: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/tablet-1787716500/btop-final.png`
- Marker/session screenshot SHA-256: `d993623a9af04dca9a309f1fae806fa5547b3c81e1e032dad2f542bb687fad95`
- The VM harness accepts `PROPER_VM_MEMORY` in megabytes; the Flatpak
  acceptance guest used `PROPER_VM_MEMORY=16384` so the live writable layer had
  enough space for the official GNOME runtime.

Additional fresh Phase 4/5 journey evidence from the same promoted ISO guest:

- Latest exact-ISO Fedora install progress: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/fedora-latest-1787732000/install-working-final.png` (SHA-256 `69ed7d62e18186fb7d117b7a398c1a7012c27e1ec306de015b30c7c8d6228a92`)
- Fresh exact-ISO btop state/launch/recovery cycle: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/fedora-postfix-1787735000/btop-active.png` shows `State: Installed` (SHA-256 `8e741b7f4c46971daeec8ab3c3ad0ab961297713b98ea7013d088b1bafa973ce`); `btop-launch.png` shows Ghostty launch (SHA-256 `348de918773d84473bc02c0ca9b1f260fc65cd9a933195e35c0d649404d0a9e4`); `recovery-working.png` shows recovery in progress (SHA-256 `ec9b510a49ec6404d8342ef756a7754bf6fa7fc335563dbcff23a8342c469d1f`); `recovery-complete.png` shows the returned Available state (SHA-256 `7630f243aff259fe4618d8d170b6e7f62d821e9a1b4da523aac7e9753bbd1bf9`).
- Latest exact-ISO Fedora verification terminal: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/fedora-latest-1787732000/rpm-latest-result.png`; visible `rpm -q btop` output confirms `btop-1.4.7-1.fc44.x86_64`.
- Fresh exact-ISO Flatpak success/recovery guest: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/flatpak-16g-1787750000/`. `flatpak-final.png` shows `State: Installed` with enabled Launch and Uninstall / recover actions (SHA-256 `6f6027b43947d6c9070f228d607c1e13b20582e92945f97ab7e779f295370df6`); `direct-launch.png` visibly shows the launched GNOME Calculator (SHA-256 `7b4f88757c25417c222e617e12b2b9f44dc172a469870d79857d4819f1b0e2f9`); `recovery-working.png` shows the returned `State: Available` (SHA-256 `77462cd4f657e3ff0089e5fb68a986621c11e1587d8dff669f9488683bfc9d8b`).
- Fresh exact-ISO vendor path in the same disposable guest: `vendor-result.png` shows Google Chrome `State: Installed` (SHA-256 `adda47c8ef18f38460b45672135515b2bb65988e360d2a2a5745283fef766d4d`); `vendor-launch.png` shows Chrome's first-run terms window (SHA-256 `9392853cb95b4788cd86e880c3d051c20ece2aec5c3864b29b0a7fcece13d040`).
- Fresh boot of the icon-enabled exact ISO: `/home/code/.codex/worktrees/7b43/proper-linux-build-icons/vm/icons-1787760000/icons-home.png` visibly renders recognizable theme icons for all seven catalogue rows (SHA-256 `a71760c55c57faf7048222368cfa073e4372d2019cc4cfc144fc8a8f82c7fdf2`).
- Fresh icon-enabled ISO Vicinae journey: `vicinae-search-icons.png` shows the searchable Proper Apps and Dropdown Terminal actions (SHA-256 `ba204dac3d164b50172f7342182eff3c9e9e0ea8d586ada72cead96fe00d2246`); selecting Dropdown Terminal opens the retained Proper Ghostty session in `vicinae-dropdown-action.png` (SHA-256 `ce5715eaab458eab9169ccc604b200c54f5503d7a24910469c153b568a95a45e`).
- A fresh guest config marker was created before attempting `pkexec dnf reinstall -y proper-terminal`; the screenshot records that the package is not available from the live guest's enabled repositories, so this is not counted as reinstall-persistence evidence (`persistence-reinstall.png`, SHA-256 `61f6b9e0b6d28c745b0a8bc002071bc4770a158c7894dce17650f1ff6e5abd63`).
- Codex agent path remains incomplete: the install attempt exhausted live writable space and the retry hit a partial npm directory (`codex-npm-retry.png`, SHA-256 `617f117264b1c8d4367bad64cc3eed641321a54a4d70e291a01992010d0954eb`); `codex-launch3.png` records the resulting Ghostty executable-not-found state (SHA-256 `5c0d18a77f23058072b519621b78f26ea3553de3778146dfec6c3bb253eb3cff`).
- After freeing the disposable guest’s vendor/runtime payloads, the official npm install completed and `/usr/local/bin/codex` was verified; `codex-direct-final.png` shows the Codex welcome/authentication screen inside Ghostty (SHA-256 `69d3584a8c277fab3ff921d637a6afa3568e4ba0c79e6f6612210f3b2fe3a619`). The Ghostty launch log is captured in `codex-app-final.png` (SHA-256 `874e0bb47eacf67fb9c9aa62e2efbe603ad1b99158a5dffa7047d264d8d367a1`).
- Fresh exact-ISO Flatpak provider attempt: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/flatpak-success-1787747000/gnome-working.png` shows the two-step transaction; `gnome-result.png` shows the understandable provider failure state. Terminal verification shows Flathub is present as a user remote. A confirmed Flatpak success remains open, so this attempt is not treated as success evidence.

- True QMP `Meta+J` hide/reopen: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/meta-1787717000/meta-hidden.png` and `meta-reopened.png` (SHA-256 `fdffb3a2aa441f63c36d5a09c6f238273a43da2a7bbd57fe8353683360b3a844`, `d5dfd94bea6375e2d8f032a769b47e6bb9d2bc843b3b72d3b122f2b682ffb405`)
- Dolphin “Open Terminal Here”: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/meta-1787717000/dolphin-terminal.png` (SHA-256 `202c7faffcd424ff14eba6f7001ca5ff6f6f46e16fc849b8e6f28ca22f5ef1b7`)
- Vicinae search for Proper Apps: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/meta-1787717000/vicinae-search.png` (SHA-256 `4d892fab6af22ff81af3ef7acc0a0324dbc79b8eee1753e7c716ab3bf6dd28c6`)
- Proper Apps home/detail: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/meta-1787717000/proper-apps.png` (SHA-256 `e0776bbb5a713ac500d2c975b84c5afe8371bd4cfd4bf21e7f95f084c883a5d7`)
- Proper Apps search and installed-state detail for btop: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/meta-1787717000/apps-search.png` (SHA-256 `b138ab8feab787a0872654e5e53e29bc062e305f62c763fee864cdf6f3160ec3`)

Final Proper Apps UI verification from a fresh boot of the exact ISO above:

- Empty search state with disabled actions and collapsed Advanced disclosure:
  `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/final-ui-1787718300/empty-final.png`
  (SHA-256 `de189c13706ba912d29186a6c402eab55daf013043c5086e8779a9707d5400fb`)
- Expanded Advanced disclosure showing provider, status, licence, and
  architecture details: `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/final-ui-1787718300/advanced-final4.png`
  (SHA-256 `21808bf93b45cf2679baa94e107ff85be30b56e76fdc82b8c46eaeda75a1ee41`)

Final category-control verification from a fresh boot of the updated ISO:

- Category dropdown visibly open with all five categories:
  `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/category-1787721000/category-open4.png`
  (SHA-256 `499593a4c2be38f160fd90ca07a728f360566b6d61a4cbc0a1b0d18c09eed128`)
- Development category selected with filtered results:
  `/home/code/.codex/worktrees/7b43/proper-linux-build/vm/category-1787721000/category-development.png`
  (SHA-256 `7088d06a5770fe5016cc8ff80bd96e885047cadcb2409f6796598858ace18883`)

The fresh post-promotion capture proves the new ISO boots to the branded
desktop. The earlier captures prove a working graphical control path for the
demonstrated actions.
They do not prove the complete Phase 4 journey; relative coordinates must not
be treated as absolute coordinates between sessions.

## Source changes included in the ISO

Proper Apps launch is separate from installation progress; successful
operations refresh installed detection; recovery uses provider-specific
Flatpak or Fedora removal commands, with an explanatory vendor fallback; and
recovery is enabled only after installed detection succeeds.
Catalogue rows use stable Fedora theme icons selected by product identity so
the catalogue remains recognizable without bundling proprietary artwork.
`scripts/validate-catalogue` passes.

## Acceptance matrix

| Criterion | Evidence state |
|---|---|
| ISO boots to Proper desktop | Passed; fresh screenshot above |
| Pointer control and visible typing | Passed; fresh tablet-VNC evidence above |
| Retained dropdown Ghostty session | Passed; fresh hide/reopen evidence above |
| Dropdown hide/reopen and Meta+J | Passed; fresh tablet and QMP evidence above |
| btop renders | Passed; fresh maximized screenshot above |
| Dolphin “Open terminal here” | Passed; fresh screenshot above |
| Vicinae actions use Ghostty | Passed; fresh Vicinae search exposes Proper Apps and Dropdown Terminal, which opens Ghostty |
| Fresh-user defaults and upgrade persistence | Open for current release-ISO evidence |
| Catalogue home/category/search/detail | Passed for home/detail/search/category; empty state and recognizable product icons passed in fresh exact-ISO captures |
| Install progress and installed state | Passed; exact-ISO progress and installed-state screenshots above |
| Launch and provider-specific recovery | Passed for Fedora btop and Flatpak GNOME Calculator; exact-ISO launch and recovery screenshots above |
| Intentional failure and advanced source details | Advanced source details and intentional empty state passed; fresh Flatpak provider failure captured |
| Fedora, Flatpak, vendor, and agent paths | Fedora, Flatpak, vendor, and Codex agent paths passed |
| PM checkpoint 4 | Not approved |

No completion claim is based solely on source inspection, package metadata,
QMP command success, or historical screenshots.

## Remaining defects before PM approval

- P2: fresh-user defaults and changed Ghostty setting persistence across package upgrade still need a fresh release-ISO capture.
- P2: a package reinstall/upgrade persistence capture remains open because the live guest's enabled repositories do not expose the installed `proper-terminal` package for reinstall.
- P3: the generic provider failure message does not include captured provider stderr, making root-cause diagnosis less direct.

## Remaining work

Continue with fresh disposable guests booted from the ISO above. Capture the
remaining acceptance journeys, update this matrix with paths and checksums,
and stop at PM checkpoint 4. Do not begin Phase 6.
