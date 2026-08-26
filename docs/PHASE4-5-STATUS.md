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

All evidence in `docs/evidence/checkpoint4-final/` must be captured from the ISO and disposable guest identified above. The terminal captures below are final3; the earlier Proper Apps captures remain clearly identified for recapture and are not yet claimed as final3 evidence. Current capture:

1. [Fresh 1920×1080 Proper desktop](evidence/checkpoint4-final/01-desktop.png) — wallpaper and floating taskbar visible; SHA-256 `b517798b6570aec78b09998f2ff510c0fbad231bade477d958e60cb355e14d84`.
2. [Proper Apps catalogue home](evidence/checkpoint4-final/02-proper-apps-home.png) — recognizable catalogue icons, detail hierarchy, and primary/secondary actions; SHA-256 `1ae74c9c4176c4b7cea20233273b25546ef7cc0c7fcc331472bbe7ccf1b122fd`.
3. [Advanced control focused](evidence/checkpoint4-final/03-advanced.png) — pointer/QMP focus state inspected; SHA-256 `7c0e18bf476b28a16f933a4f8b24b20354caebf5512d7e63e5bd1d5f0d0b857a`.
4. [Category control open](evidence/checkpoint4-final/04-categories-open.png) — category menu visibly exposes Web, Development, AI, and Utilities; SHA-256 `b8cfd883fc718d4a29aa48bcb77ad2b5ae18dfc95f6f47f6e0991caeedf3c3d1`.
5. [Filtered category view](evidence/checkpoint4-final/05-category-filtered.png) — Web category narrows the catalogue to Google Chrome; SHA-256 `9660a58cd939a62a397767cf8856061cc3af3a93a0f20c305f6fa9ebc0e6343e`.
6. [Search results](evidence/checkpoint4-final/06-search-results.png) — `btop` search returns the installed application and enables Launch/Uninstall; SHA-256 `b06e081ee4de614796800ff5f183461281da0bf0c4bd07861f491a618217f08c`.
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

- P2: all Proper Apps captures must be recaptured from final3 after the terminal-only rebuild so the package has one authoritative ISO. The final3 guest verified the widened retained dropdown and a readable `btop` session; AI-agent launch and other retained desktop interactions remain open.

## PM handoff request

After the evidence index is complete, request PM visual approval for checkpoint 4. No approval is asserted by this document.
