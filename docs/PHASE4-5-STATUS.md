# Phase 4/5 status — checkpoint 4 review package

## Current integration artifact

- Branch: `codex/complete-phase-4-and-5`
- ISO: `/home/code/.codex/worktrees/7b43/proper-linux-build-final3/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.iso`
- ISO SHA-256: `a416ec1b59b8cd4699305135f308b51c3ec94685337b053bdf1a2a9f8939bb71`
- Package manifest: `/home/code/.codex/worktrees/7b43/proper-linux-build-final3/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.packages`
- Proper Apps RPM: `/home/code/.codex/worktrees/7b43/proper-linux-build-final3/rpms/proper-apps/RPMS/x86_64/proper-apps-0.1-3.fc44.x86_64.rpm`
- Proper Terminal RPM: `/home/code/.codex/worktrees/7b43/proper-linux-build-final3/rpms/proper-terminal/RPMS/x86_64/proper-terminal-1.2.3-6.fc44.x86_64.rpm`
- Proper Terminal RPM SHA-256: `8c5786da3285796bf06c17025d6f9d8a1575f6a9d841ebc30b2f9edc0e6a032a`

The manifest contains `proper-apps-0.1-3.fc44.x86_64` and `proper-terminal-1.2.3-5.fc44.x86_64`; no LibreOffice package is present. The ISO was composed from the same rebuilt local RPM repository and passed KIWI image creation and media verification.

## Implementation in this revision

Proper Apps now presents bounded operation progress and a restrained technical-details disclosure. Provider operations capture the failed step, process-start errors, nonzero exit status, and up to 1200 characters of stderr. The normal view uses plain-language failure and recovery guidance; credentials and unbounded provider output are never shown.

## Authoritative final-ISO evidence

All evidence in `docs/evidence/checkpoint4-final/` must be captured from the ISO and disposable guest identified above. Items 1–6 and 14–16 are final3 captures; operation captures 8–13 still require final3 recapture before this package can be called consolidated.

1. [Fresh 1920×1080 Proper desktop](evidence/checkpoint4-final/01-desktop.png) — final3 wallpaper and floating taskbar visible; SHA-256 `d38e1dc8afa20a308f9a5b661deed16c2cf5e73ed12b342feb8e7ff547e8538c`.
2. [Proper Apps catalogue home](evidence/checkpoint4-final/02-proper-apps-home.png) — final3 catalogue icons, detail hierarchy, and primary/secondary actions; SHA-256 `dda0885c81a4550874f46a2dc30628917ae01597bf3bdc46fcbc5cbb3ac9d79e`.
3. [Advanced source control](evidence/checkpoint4-final/03-advanced.png) — final3 source disclosure state inspected; SHA-256 `294bf97316c570c418e1336f56251fb790c2e84eebfbf2915232a79348718f14`.
4. [Category control open](evidence/checkpoint4-final/04-categories-open.png) — final3 category menu exposes Web, Development, AI, and Utilities; SHA-256 `86b6fc833cc770b6d1a9466ac3cfad90b63e0d6e9e1920d769f8ab03304509d7`.
5. [Filtered category view](evidence/checkpoint4-final/05-category-filtered.png) — final3 Web category narrows the catalogue to Google Chrome; SHA-256 `cc1d59de0856ef96d2c53b385d16b2a5b856ba158dc0a46582f4959ddc6afed2`.
6. [Search results](evidence/checkpoint4-final/06-search-results.png) — final3 `btop` search returns the installed application and enables Launch/Uninstall; SHA-256 `76f5cf5daf9c4c97615c8f863ee5ac22bb4d9c9db5e460dda872fc67456ab377`.
7. [High-DPI desktop](evidence/checkpoint4-final/07-hidpi-200-percent.png) — fresh 3840×2160 framebuffer at 200% scale; floating taskbar remains legible and proportionate; SHA-256 `59da004bfcdaa31e8efc10232173c6a91163735dad9ee3832bf218b497235e1a`.
8. [Install progress](evidence/checkpoint4-final/08-install-progress.png) — Chrome vendor operation visibly reports `Working… step 1 of 1`; SHA-256 `350d5e9e382ee5df38a4af6c21353365ccddfcd063b6183bf83a4e8ba576ba41`.
9. [Installed state](evidence/checkpoint4-final/09-installed-state.png) — Chrome detail shows Installed and exposes Launch and Uninstall / recover; SHA-256 `447ec7c72a62cf333402b6e2acdbd7938365702c7edc320c176a405b7fc0491d`.
10. [Vendor recovery](evidence/checkpoint4-final/10-recovery.png) — recovery explains official-vendor removal and credential handling; SHA-256 `f3070005e1a224bef24ca8ebb868df81f5bf039a33d13caa7b6ba51fa66b43a5`.
11. [Expanded source details](evidence/checkpoint4-final/11-advanced-source.png) — expanded panel exposes provider, maintenance status, licence, and architecture; SHA-256 `201ed4d0bdadef4d576cb07bf8e169842a3702f41b2e416e2d87e2f11cc7bac4`.
12. [Provider failure](evidence/checkpoint4-final/12-provider-failure.png) — offline Codex vendor installation gives plain-language status and recovery guidance; SHA-256 `3a90aa6f96cc5bc0a5bee32e08d79195903d2d667a4accfc7d045420118d4bc2`.
13. [Technical failure details](evidence/checkpoint4-final/13-technical-failure.png) — expandable panel shows failed provider step, exit status, process, and bounded stderr; SHA-256 `9994913dd9bb1f159ec7061fd5cb8f43e58d7653fe0ba93dbfaba32d14d5eb4d`.
14. [Final3 dropdown Ghostty](evidence/checkpoint4-final/14-dropdown-ghostty.png) — widened retained terminal surface; SHA-256 `4241cc4ad2c38cd4c99ec1883f4fcf30c7f0a0b0a718f7b08a455544067004f4`.
15. [Final3 restored dropdown](evidence/checkpoint4-final/15-dropdown-restored.png) — retained terminal restored after toggle; SHA-256 `f30a89ec25b61e8d69f630df3924f220c4313c0d86f7dcaa73f5ccf07ed598d6`.
16. [Final3 btop](evidence/checkpoint4-final/16-btop.png) — btop fills the widened terminal without the prior minimum-size warning; SHA-256 `37c3b6142996e49f30f65fa1e8f294a27c8b4b8acd8f06122af56d5c8874191f`.

The remaining provider-operation, recovery, retained-desktop, and 200% journeys are still being recaptured from this exact ISO; screenshots from earlier ISO generations are intentionally not treated as current evidence.

## Validation

Passed: `scripts/check-box`; `scripts/validate-catalogue`; `git diff --check`; `bash -n scripts/build-rpms scripts/build-iso scripts/run-vm`; full `PROPER_OUTPUT_DIR=/home/code/.codex/worktrees/7b43/proper-linux-build-final scripts/build-iso`; ISO checksum; package-manifest inspection; and fresh UEFI/KVM boot at 1920×1080/100%.

## Acceptance state

Checkpoint 4 is not PM-approved. Do not begin Phase 6. Continue the single fresh guest journey and capture catalogue home, categories, search, details, progress, installed/launch/recovery/failure states, advanced details, and the retained desktop interactions from this exact ISO. Perform a focused 200% inspection before requesting approval.

## Known defects

- P2: final3 operation captures 8–13 and the 200% inspection still need recapture so the package has one authoritative ISO. The final3 guest verified the widened retained dropdown and a readable `btop` session; AI-agent launch and other retained desktop interactions remain open.

## PM handoff request

After the evidence index is complete, request PM visual approval for checkpoint 4. No approval is asserted by this document.
