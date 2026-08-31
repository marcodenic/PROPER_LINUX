# Proper Linux

> Normal Linux. Properly finished.

Proper Linux is an opinionated, mouse-friendly developer desktop built on Fedora KDE. It keeps Fedora's working operating-system foundation and concentrates on the part desktop Linux repeatedly neglects: a coherent, attractive, sensible experience from login to daily work.

The project takes inspiration from Omarchy's strong curation, aesthetics, shortcuts, and developer focus without adopting its keyboard-only operating model. Floating windows, mouse movement and resizing, snapping, a conventional taskbar, and discoverable graphical controls remain first-class. Keyboard shortcuts accelerate the same actions; they are never the only way to reach them.

## Status

Proper Linux is in active pre-release development. Phases 9–11 are integrated
and have installed-VM evidence; the next engineering milestone is the clean
Phase 12 ISO, installation, and final acceptance journey. There is not yet a
public release candidate.

## Version 0.1

- Mutable Fedora KDE foundation
- Proper Linux boot, login, lock, wallpaper, and desktop branding
- Correct login-screen display orientation
- Tasteful translucent floating bottom taskbar
- Vicinae as the single mouse-accessible, Raycast-style application launcher and command surface
- Floating windows with mouse snapping and `Meta`+arrow quick tiling
- Useful Omarchy-inspired shortcuts as optional accelerators
- Ghostty 1.2.3 as the default terminal, with an ordinary taskbar launcher
- `btop` installed by default
- A deliberately simplified and styled file-manager experience
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
- [UX strategy and competitive position](docs/UX_STRATEGY.md)
- [UI iteration workflow](docs/UI_ITERATION.md)
- [Releases, updates, and repository policy](docs/RELEASES_AND_UPDATES.md)
- [BOX continuation guide](docs/BOX_KICKOFF.md)

## Product rule

Preserve Fedora unless a user can see the problem, feel the problem, or is unnecessarily forced to understand the problem.

## Naming and licensing

“Proper Linux” is a working name pending a formal trademark check. The project will remain publicly downloadable and open source. Exact code, documentation, and artwork licences must be selected before the first public release; the proposed choices are recorded in the decision log.
