# Proper Linux repository instructions

## Start here

Before changing this repository, read:

1. `docs/PRODUCT.md`
2. `docs/EXPERIENCE.md`
3. `docs/ARCHITECTURE.md`
4. `docs/IMPLEMENTATION_PLAN.md`
5. `docs/ACCEPTANCE.md`
6. `docs/DECISIONS.md`

Before changing any visible desktop behaviour or styling, also read:

7. `docs/UX_STRATEGY.md`
8. `docs/UI_ITERATION.md`

The user is the product manager and primary customer. Their visual judgment is authoritative at the explicit PM checkpoints.

## Working principles

- Keep Fedora's kernel, drivers, networking, security, installer, updater, and normal mutable package model unless they directly block the intended experience.
- Treat Proper Linux as a curated desktop product, not an excuse to invent a kernel, package manager, installer, or configuration framework.
- Prefer upstream components and configuration packages over forks.
- Prefer system packages and supported Plasma extension points over copying a developer's entire home directory.
- Every normal desktop operation must remain available through ordinary pointer interaction. Shortcuts are accelerators, not prerequisites.
- Do not force a choice between floating and tiled workflows. Floating is the default; snapping and quick tiling are always available.
- Keep the default installation lean. Put optional software in the curated application catalogue.
- Do not add office suites to the default image.
- Do not introduce a privileged AI daemon in version 0.1.
- Do not expand into broad hardware certification, performance benchmarking, or public release infrastructure unless it blocks the current milestone.

## Execution behaviour

- Work autonomously between the five PM checkpoints defined in `docs/ACCEPTANCE.md`.
- Do not stop for ordinary implementation choices already resolved by these documents.
- At a visual checkpoint, provide screenshots and a short list of interactions ready for review.
- Build the ISO on the Linux BOX host. Use QEMU/KVM for desktop and installer evaluation; a normal Docker container cannot validate a graphical operating-system session.
- Pin external component versions in builds. Record their source, licence, and update method.
- Keep secrets, signing keys, access tokens, and proprietary credentials out of Git.
- When upstream behaviour changes, update `docs/DECISIONS.md` and `docs/RESEARCH.md` rather than silently changing direction.
- Use the three feedback loops in `docs/UI_ITERATION.md`: prototype in the running development session, promote approved work into an RPM, and rebuild the ISO only for image integration and checkpoint validation.
- Treat hand-edited user configuration as a prototype. Reduce it to intentional, versioned defaults before calling the work implemented.

## BOX and VM discipline

- At the start of build or VM work, run `scripts/check-box` and verify the current hostname and `/dev/kvm` access. Treat logs or claims from earlier tasks as historical context, not evidence about the current task environment.
- Launch every product-manager-facing review with the default local GTK presentation from `scripts/run-vm`: one 1920x1080 output in a normal resizable window with zoom-to-fit enabled, so maximising the host window fills its client area. Do not force full screen. VNC and multi-output modes are automation/compatibility tools, not PM presentation surfaces; never substitute them for the visible review window.
- Run at most one Proper Linux QEMU VM at a time. Before launching one, inspect existing QEMU command lines and monitor sockets. Reuse the intended VM when possible; otherwise verify the exact PID, ISO, disk, and socket before terminating a stale VM gracefully. Never kill VMs with a broad process-name pattern.
- Give the active VM a unique disk plus explicit monitor/control sockets, and verify that each socket is owned by the sole expected QEMU PID before sending input.
- A QEMU `screendump` proves only that the guest can be observed. It does not prove that Codex can control the GTK window, and a successful `socat` exit proves only that QEMU accepted a monitor command—not that the installer accepted the intended click.
- Do not drive an absolute USB tablet with HMP `mouse_move` pixel deltas. For graphical automation, use a QMP input socket with absolute pointer events scaled to the current framebuffer, or expose the VM through VNC/noVNC or another explicitly controllable surface. Use keyboard navigation only after focus and state changes have been verified.
- After every graphical action, capture the screen and confirm that the expected page, focus, selection, or progress state changed. If it did not, make at most one corrected retry, then diagnose the socket target, active input device, coordinate mapping, and focus instead of repeating blind inputs or waits.
- Use Kickstart or another deterministic Fedora-supported automation path for routine repeat installations. Still exercise the normal graphical installer with real pointer interaction for the PM acceptance journey.
- Before reporting progress or leaving a VM running, verify that exactly one Proper Linux VM exists and state whether installation actually started, completed, or is still waiting for input.

## Definition of progress

A package compiling is not a product milestone. A milestone is complete when the relevant behaviour works in the installed VM and satisfies its acceptance criteria.
