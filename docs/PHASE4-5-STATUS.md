# Phase 4/5 status — checkpoint 4 review package

## Current integration artifact

- Branch: `codex/complete-phase-4-and-5`
- ISO: `/home/code/.codex/worktrees/7b43/proper-linux-build-final2/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.iso`
- ISO SHA-256: `22927203a3a04439c1b7feaa8014d7ee95ccd1ae8486f7475db7aacdad456feb`
- Package manifest: `/home/code/.codex/worktrees/7b43/proper-linux-build-final2/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.packages`
- Proper Apps RPM: `/home/code/.codex/worktrees/7b43/proper-linux-build-final2/rpms/proper-apps/RPMS/x86_64/proper-apps-0.1-3.fc44.x86_64.rpm`
- RPM SHA-256: `2ad322b9cabd21662da7c8cac7fe1242eb8b9b5d8b1500cc4736e93dcf60cc1c`

The manifest contains `proper-apps-0.1-3.fc44.x86_64` and `proper-terminal-1.2.3-5.fc44.x86_64`; no LibreOffice package is present. The ISO was composed from the same rebuilt local RPM repository and passed KIWI image creation and media verification.

## Implementation in this revision

Proper Apps now presents bounded operation progress and a restrained technical-details disclosure. Provider operations capture the failed step, process-start errors, nonzero exit status, and up to 1200 characters of stderr. The normal view uses plain-language failure and recovery guidance; credentials and unbounded provider output are never shown.

## Authoritative final-ISO evidence

All evidence in `docs/evidence/checkpoint4-final/` must be captured from the ISO and disposable guest identified above. Current capture:

1. [Fresh 1920×1080 Proper desktop](evidence/checkpoint4-final/01-desktop.png) — wallpaper and floating taskbar visible; SHA-256 `b517798b6570aec78b09998f2ff510c0fbad231bade477d958e60cb355e14d84`.
2. [Proper Apps catalogue home](evidence/checkpoint4-final/02-proper-apps-home.png) — recognizable catalogue icons, detail hierarchy, and primary/secondary actions; SHA-256 `1ae74c9c4176c4b7cea20233273b25546ef7cc0c7fcc331472bbe7ccf1b122fd`.
3. [Advanced control focused](evidence/checkpoint4-final/03-advanced.png) — pointer/QMP focus state inspected; SHA-256 `7c0e18bf476b28a16f933a4f8b24b20354caebf5512d7e63e5bd1d5f0d0b857a`.
4. [Category control state](evidence/checkpoint4-final/04-categories-open.png) — category control received the verified click but the popup was not visibly open; SHA-256 `f099fba5bf584ce1e0b9c245f5e709e9f1a7e6e5627dc19e085f8126c1f92441`.

The remaining catalogue and desktop journeys are still being recaptured from this exact ISO; screenshots from earlier ISO generations are intentionally not treated as current evidence.

## Validation

Passed: `scripts/check-box`; `scripts/validate-catalogue`; `git diff --check`; `bash -n scripts/build-rpms scripts/build-iso scripts/run-vm`; full `PROPER_OUTPUT_DIR=/home/code/.codex/worktrees/7b43/proper-linux-build-final scripts/build-iso`; ISO checksum; package-manifest inspection; and fresh UEFI/KVM boot at 1920×1080/100%.

## Acceptance state

Checkpoint 4 is not PM-approved. Do not begin Phase 6. Continue the single fresh guest journey and capture catalogue home, categories, search, details, progress, installed/launch/recovery/failure states, advanced details, and the retained desktop interactions from this exact ISO. Perform a focused 200% inspection before requesting approval.

## Known defects

- P3: full final2-ISO interaction journey and 200% inspection evidence remain to be captured in this guest.

## PM handoff request

After the evidence index is complete, request PM visual approval for checkpoint 4. No approval is asserted by this document.
