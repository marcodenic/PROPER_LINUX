# Phase 4/5 status — checkpoint 4 review package

## Current integration artifact

- Branch: `codex/complete-phase-4-and-5`
- ISO: `/home/code/.codex/worktrees/7b43/proper-linux-build-final/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.iso`
- ISO SHA-256: `3fcb5b8ace303d6d1af6c0cfdb264e48a178630a8bdbde3239df1b00b0c063f5`
- Package manifest: `/home/code/.codex/worktrees/7b43/proper-linux-build-final/iso/proper-linux-0.1-dfc49a5a10f6/image-build/Fedora.x86_64-44.packages`
- Proper Apps RPM: `/home/code/.codex/worktrees/7b43/proper-linux-build-final/rpms/proper-apps/RPMS/x86_64/proper-apps-0.1-3.fc44.x86_64.rpm`
- RPM SHA-256: `72a3c72bed7638866c7c758e8fa524d963cd6dae309d28a2c2d2173aab77bdd5`

The manifest contains `proper-apps-0.1-3.fc44.x86_64` and `proper-terminal-1.2.3-5.fc44.x86_64`; no LibreOffice package is present. The ISO was composed from the same rebuilt local RPM repository and passed KIWI image creation and media verification.

## Implementation in this revision

Proper Apps now presents bounded operation progress and a restrained technical-details disclosure. Provider operations capture the failed step, process-start errors, nonzero exit status, and up to 1200 characters of stderr. The normal view uses plain-language failure and recovery guidance; credentials and unbounded provider output are never shown.

## Authoritative final-ISO evidence

All evidence in `docs/evidence/checkpoint4-final/` must be captured from the ISO and disposable guest identified above. Current capture:

1. [Fresh 1920×1080 Proper desktop](evidence/checkpoint4-final/01-desktop.png) — wallpaper and floating taskbar visible; SHA-256 `e2431100369282f8016574a39905abf4a555d1f457917c1266eb315dbe18ee89`.

The remaining catalogue and desktop journeys are still being recaptured from this exact ISO; screenshots from earlier ISO generations are intentionally not treated as current evidence.

## Validation

Passed: `scripts/check-box`; `scripts/validate-catalogue`; `git diff --check`; `bash -n scripts/build-rpms scripts/build-iso scripts/run-vm`; full `PROPER_OUTPUT_DIR=/home/code/.codex/worktrees/7b43/proper-linux-build-final scripts/build-iso`; ISO checksum; package-manifest inspection; and fresh UEFI/KVM boot at 1920×1080/100%.

## Acceptance state

Checkpoint 4 is not PM-approved. Do not begin Phase 6. Continue the single fresh guest journey and capture catalogue home, categories, search, details, progress, installed/launch/recovery/failure states, advanced details, and the retained desktop interactions from this exact ISO. Perform a focused 200% inspection before requesting approval.

## Known defects

- P3: full final-ISO interaction journey and 200% inspection evidence remain to be captured in this guest.

## PM handoff request

After the evidence index is complete, request PM visual approval for checkpoint 4. No approval is asserted by this document.
