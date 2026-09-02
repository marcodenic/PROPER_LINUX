# Proper Linux repository instructions

Read only these project documents before changing the repository:

1. `docs/PRODUCT.md`
2. `docs/ARCHITECTURE.md`

The user is the product manager. Their visual judgement is authoritative.

## Rules

- Preserve Fedora's working foundation and mutable package model. Proper owns
  curation, defaults, presentation, and integration.
- Prefer upstream components, supported Plasma extension points, and versioned
  RPM defaults over forks or copied home directories.
- Every ordinary action needs a pointer path. Floating is the default;
  shortcuts, snapping, tiling, and workspace arrangement are accelerators.
- Keep the image lean, remove noise and duplication, and put optional software
  in Proper Apps.
- Seed defaults once and preserve later user choices.
- Pin external inputs and keep provenance beside the package or lock file.
- Keep secrets and generated build/VM artifacts out of Git.

## Work

- Work through ordinary implementation decisions without stopping. Ask only
  when product direction or authority must change.
- Prototype visible work in a disposable session, promote it into its owning
  RPM, then rebuild the ISO when image integration is involved.
- A successful build is not completion. Verify the changed behaviour in the
  installed graphical system and provide screenshots for visual review.

## VM reviews

- Always use `scripts/run-vm` with its single-output `fullhd` GTK default:
  1920×1080 at 100% scale with zoom-to-fit.
- Immediately maximise the QEMU window. The guest must fill a normal
  laptop-sized display; never present the tiny default window, VNC, multiple
  outputs, or a high-DPI test profile as the main review surface.
- Run at most one Proper Linux VM and verify its exact ISO, disk, PID, and
  sockets before reusing or stopping it. Never kill QEMU by a broad name match.
- After graphical input, capture the screen and confirm the guest changed
  state. A successful input command alone proves nothing.

## Done

A change is done only when it is versioned, works in the installed VM,
preserves user choices, and supports the ordinary pointer workflow.
