# Proper Linux

> Normal Linux. Properly finished.

Proper Linux is an opinionated, mouse-friendly developer desktop built on Fedora KDE. It keeps Fedora's working operating-system foundation and concentrates on the part desktop Linux repeatedly neglects: a coherent, attractive, sensible experience from login to daily work.

The project takes inspiration from Omarchy's strong curation, aesthetics, shortcuts, and developer focus without adopting its keyboard-only operating model. Floating windows, mouse movement and resizing, snapping, a conventional taskbar, and discoverable graphical controls remain first-class. Keyboard shortcuts accelerate the same actions; they are never the only way to reach them.

## Status

Proper Linux is in product-definition and prototype planning. There is not yet an installable release.

The first engineering objective is a Fedora KDE-based live ISO that installs into a QEMU/KVM virtual machine and presents the approved Proper Linux login and desktop experience.

## Version 0.1

- Mutable Fedora KDE foundation
- Proper Linux boot, login, lock, wallpaper, and desktop branding
- Correct login-screen display orientation
- Tasteful translucent floating bottom taskbar
- AppGrid for mouse-first application browsing
- Vicinae for Raycast-style search and commands
- Floating windows with mouse snapping and `Meta`+arrow quick tiling
- Useful Omarchy-inspired shortcuts as optional accelerators
- Ghostty as the default terminal, with a taskbar-accessible dropdown mode
- `btop` installed by default
- Lean base installation
- A curated, one-click application directory
- Easy installation and launch of Codex, Claude Code, OpenCode, and related tools
- Fedora's existing installer and update machinery
- No paid edition, account gate, or download paywall

## Product documentation

- [Product definition](docs/PRODUCT.md)
- [Experience specification](docs/EXPERIENCE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Implementation plan](docs/IMPLEMENTATION_PLAN.md)
- [Acceptance criteria](docs/ACCEPTANCE.md)
- [Application catalogue](docs/APPLICATIONS.md)
- [Decision log](docs/DECISIONS.md)
- [Research and upstream references](docs/RESEARCH.md)
- [BOX continuation guide](docs/BOX_KICKOFF.md)

## Product rule

Preserve Fedora unless a user can see the problem, feel the problem, or is unnecessarily forced to understand the problem.

## Naming and licensing

“Proper Linux” is a working name pending a formal trademark check. The project will remain publicly downloadable and open source. Exact code, documentation, and artwork licences must be selected before the first public release; the proposed choices are recorded in the decision log.
