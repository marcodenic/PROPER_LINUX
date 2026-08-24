# Proper Linux repository instructions

## Start here

Before changing this repository, read:

1. `docs/PRODUCT.md`
2. `docs/EXPERIENCE.md`
3. `docs/ARCHITECTURE.md`
4. `docs/IMPLEMENTATION_PLAN.md`
5. `docs/ACCEPTANCE.md`
6. `docs/DECISIONS.md`

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

## Definition of progress

A package compiling is not a product milestone. A milestone is complete when the relevant behaviour works in the installed VM and satisfies its acceptance criteria.
