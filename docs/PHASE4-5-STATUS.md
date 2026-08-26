# Phase 4/5 status — checkpoint 4 review package

## Current integration artifact

- Branch: `codex/complete-phase-4-and-5`
- ISO: `/home/code/.codex/worktrees/7b43/proper-linux-build-final3/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.iso`
- ISO SHA-256: `a416ec1b59b8cd4699305135f308b51c3ec94685337b053bdf1a2a9f8939bb71`
- Package manifest: `/home/code/.codex/worktrees/7b43/proper-linux-build-final3/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.packages`
- Proper Apps RPM: `/home/code/.codex/worktrees/7b43/proper-linux-build-final3/rpms/proper-apps/RPMS/x86_64/proper-apps-0.1-3.fc44.x86_64.rpm`
- Proper Terminal RPM: `/home/code/.codex/worktrees/7b43/proper-linux-build-final3/rpms/proper-terminal/RPMS/x86_64/proper-terminal-1.2.3-6.fc44.x86_64.rpm`
- Proper Terminal RPM SHA-256: `8c5786da3285796bf06c17025d6f9d8a1575f6a9d841ebc30b2f9edc0e6a032a`

The manifest contains `proper-apps-0.1-3.fc44.x86_64` and `proper-terminal-1.2.3-6.fc44.x86_64`; no LibreOffice package is present. The ISO was composed from the same rebuilt local RPM repository and passed KIWI image creation and media verification.

## Implementation in this revision

Proper Apps now presents bounded operation progress and a restrained technical-details disclosure. Provider operations capture the failed step, process-start errors, nonzero exit status, and up to 1200 characters of stderr. The normal view uses plain-language failure and recovery guidance; credentials and unbounded provider output are never shown.

## Authoritative final-ISO evidence

All evidence in `docs/evidence/checkpoint4-final/` is captured from the ISO and disposable guests identified above. Items 1–16 are final3 captures.

1. [Fresh 1920×1080 Proper desktop](evidence/checkpoint4-final/01-desktop.png) — final3 wallpaper and floating taskbar visible; SHA-256 `d38e1dc8afa20a308f9a5b661deed16c2cf5e73ed12b342feb8e7ff547e8538c`.
2. [Proper Apps catalogue home](evidence/checkpoint4-final/02-proper-apps-home.png) — final3 catalogue icons, detail hierarchy, and primary/secondary actions; SHA-256 `dda0885c81a4550874f46a2dc30628917ae01597bf3bdc46fcbc5cbb3ac9d79e`.
3. [Advanced source control](evidence/checkpoint4-final/03-advanced.png) — final3 source disclosure state inspected; SHA-256 `294bf97316c570c418e1336f56251fb790c2e84eebfbf2915232a79348718f14`.
4. [Category control open](evidence/checkpoint4-final/04-categories-open.png) — final3 category menu exposes Web, Development, AI, and Utilities; SHA-256 `86b6fc833cc770b6d1a9466ac3cfad90b63e0d6e9e1920d769f8ab03304509d7`.
5. [Filtered category view](evidence/checkpoint4-final/05-category-filtered.png) — final3 Web category narrows the catalogue to Google Chrome; SHA-256 `cc1d59de0856ef96d2c53b385d16b2a5b856ba158dc0a46582f4959ddc6afed2`.
6. [Search results](evidence/checkpoint4-final/06-search-results.png) — final3 `btop` search returns the installed application and enables Launch/Uninstall; SHA-256 `76f5cf5daf9c4c97615c8f863ee5ac22bb4d9c9db5e460dda872fc67456ab377`.
7. [High-DPI desktop](evidence/checkpoint4-final/07-hidpi-200-percent.png) — fresh 3840×2160 framebuffer at 200% scale; floating taskbar remains legible and proportionate; SHA-256 `fdeca0f46d6373c6021e2b0392828e81a82b128d55d3c2b7b0b5f2283888005b`.
8. [Install progress](evidence/checkpoint4-final/08-install-progress.png) — Chrome vendor operation visibly reports `Working… step 1 of 1`; SHA-256 `f7edcd7686d5e95cef139c4de417bd13d9f2a550b25e76b8c2ebe7a1d3088442`.
9. [Installed state](evidence/checkpoint4-final/09-installed-state.png) — Chrome detail shows Installed and exposes Launch and Uninstall / recover; SHA-256 `184b04f8e9a28f558c6f69713e1b3a1704fa196fbc49577a273e81d74e9a3eec`.
10. [Vendor recovery](evidence/checkpoint4-final/10-recovery.png) — recovery explains official-vendor removal and credential handling; SHA-256 `fe26a846c5d47b7f7d05b483264d14057d0cbabd50de45549b567c4e9769ad0b`.
11. [Expanded source details](evidence/checkpoint4-final/11-advanced-source.png) — expanded panel exposes provider, maintenance status, licence, and architecture; SHA-256 `d557ce8b4a76e3eaa2e3ea574e12b06f7d10d2f695e7c958e02c18956e1021ed`.
12. [Provider failure](evidence/checkpoint4-final/12-provider-failure.png) — offline Codex vendor installation gives plain-language status and recovery guidance; SHA-256 `6d339843c1a062be2005b56d216467dbb54ffb9a8f2ed2a74e052af9da368b58`.
13. [Technical failure details](evidence/checkpoint4-final/13-technical-failure.png) — expandable panel shows failed provider step, exit status, process, and bounded stderr; SHA-256 `7bae449350771c9647c4c0f1f7f2e9b794c328668d336cf518c49b2baa4caeac`.
14. [Final3 dropdown Ghostty](evidence/checkpoint4-final/14-dropdown-ghostty.png) — widened retained terminal surface; SHA-256 `4241cc4ad2c38cd4c99ec1883f4fcf30c7f0a0b0a718f7b08a455544067004f4`.
15. [Final3 restored dropdown](evidence/checkpoint4-final/15-dropdown-restored.png) — retained terminal restored after toggle; SHA-256 `f30a89ec25b61e8d69f630df3924f220c4313c0d86f7dcaa73f5ccf07ed598d6`.
16. [Final3 btop](evidence/checkpoint4-final/16-btop.png) — btop fills the widened terminal without the prior minimum-size warning; SHA-256 `37c3b6142996e49f30f65fa1e8f294a27c8b4b8acd8f06122af56d5c8874191f`.

The provider-operation, recovery, source, and 200% journeys are now consolidated against this exact ISO; retained-desktop journeys remain open.

## Validation

Passed: `scripts/check-box`; `scripts/validate-catalogue`; `git diff --check`; `bash -n scripts/build-rpms scripts/build-iso scripts/run-vm`; full `PROPER_OUTPUT_DIR=/home/code/.codex/worktrees/7b43/proper-linux-build-final scripts/build-iso`; ISO checksum; package-manifest inspection; and fresh UEFI/KVM boot at 1920×1080/100%.

## Acceptance state

Checkpoint 4 is not PM-approved. Do not begin Phase 6. Continue the single fresh guest journey and capture catalogue home, categories, search, details, progress, installed/launch/recovery/failure states, advanced details, and the retained desktop interactions from this exact ISO. Perform a focused 200% inspection before requesting approval.

## Known defects

- P2: AI-agent launch and retained Dolphin/Vicinae journeys remain directly unevidenced. The widened retained dropdown and readable `btop` session are verified.

## PM handoff request

After the evidence index is complete, request PM visual approval for checkpoint 4. No approval is asserted by this document.
