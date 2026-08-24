# Proper Linux product definition

## One sentence

Proper Linux is a tasteful, opinionated Fedora KDE developer desktop that keeps normal Linux power while making the default graphical experience coherent, attractive, discoverable, and equally comfortable with a mouse or keyboard.

## The problem

Desktop Linux plumbing is generally good enough. The recurring failure is the product experience placed on top of it:

- Defaults look assembled rather than designed.
- Distributions advertise implementation details and acronyms instead of showing why the desktop is desirable.
- Users are asked to understand package formats and repositories to install ordinary software.
- “Modern” enthusiast systems often make keyboard shortcuts mandatory rather than optional accelerators.
- Login, wallpaper, screen orientation, application discovery, terminal styling, and window management contain small but needless paper cuts.
- Customisability is treated as a substitute for choosing excellent defaults.

Proper Linux is an attempt to apply taste and sustained attention to those failures without rebuilding the parts Fedora already handles well.

## Primary customer

The product manager is also the primary customer.

The broader audience is technically capable people who:

- want full access to Linux rather than an appliance that hides it;
- dislike Linux's traditional visual and interaction conventions;
- use a mouse normally and keyboard shortcuts opportunistically;
- value developer tools, terminals, and AI coding agents;
- want strong defaults without losing the ability to change them;
- want to install the system, log in, and work without a setup ceremony.

This is not designed around a hypothetical beginner or a committee average. It begins with the primary customer's actual workflow and may serve people with similar preferences.

## Product promise

Install Proper Linux and receive a current, capable Linux workstation whose visible experience feels deliberately finished. Normal operations work as expected with the mouse. Excellent shortcuts are available when useful. Common applications are one click away. The terminal and AI tooling feel native to the product rather than bolted on.

## Product principles

### Preserve what works

Keep Fedora's kernel, hardware enablement, networking, security, package system, installer, and updater unless a concrete user-facing problem requires intervention.

### Fix the experience, not Linux

Proper Linux does not protect technically capable users from the operating system. It removes needless friction and poor presentation.

### Defaults are the product

The initial layout, theme, shortcuts, applications, and behaviour must be good without requiring a rice, dotfile repository, or configuration guide.

### Mouse and keyboard are peers

Every normal desktop operation remains visually discoverable and usable with the pointer. Shortcuts make the same actions faster. Neither input method invalidates the other.

### Reject false choices

Floating windows and tiling can coexist. Pointer discovery and typed commands can coexist in one launcher. A lean installation and a rich software catalogue can coexist.

### Curate aggressively, restrict sparingly

Proper Linux makes strong default choices. Users can still reach normal Plasma settings, `dnf`, Flatpak, the terminal, and the underlying system.

### No paywall theatre

The ISO and source will be publicly downloadable without an account, paid edition, delayed download, or deliberately crippled community build. Optional donations or sponsorship may exist later but never gate the product.

## Experience pillars

### 1. A coherent arrival

Boot, installer, login, lock screen, and desktop use the same visual language. The login screen uses the intended wallpaper and correct monitor layout. Installation ends with login and immediate use, not a long onboarding questionnaire.

### 2. A proper desktop shell

A tasteful translucent floating bottom taskbar provides applications, running-window state, a terminal affordance, and system status. It stays visible by default and can be hidden by user preference.

### 3. Normal windows, excellent arrangement

Windows float, overlap, drag, resize, minimise, maximise, and close normally. Dragging to edges offers halves and grids. `Meta` plus arrow keys provides fast Windows-style quick tiling. More advanced Omarchy-inspired bindings are available without becoming mandatory.

### 4. One deliberate launcher

Vicinae answers both “open an application” and “find or do something” with a polished Raycast-style surface. Clicking the Proper button opens a useful mouse-accessible home state with pinned and recent applications; typing searches applications, files, commands, actions, and extensions.

### 5. A first-class terminal and agent workflow

Ghostty is the default terminal and looks finished on first launch. A taskbar action toggles a convenient dropdown or slide-out terminal. `btop` is available immediately. Codex, Claude Code, OpenCode, and other agents are easy to install, authenticate, and launch.

### 6. One obvious path to software

A curated application directory presents recognisable products and a single Install action. Provider details remain available under an advanced disclosure, but users do not need to decide between RPM, Flatpak, a vendor repository, or another source during the normal path.

## Version 0.1 scope

Version 0.1 must include:

- a mutable Fedora KDE base;
- Proper Linux name and simple ASCII-influenced identity;
- coherent system-wide wallpaper and visual defaults;
- Plasma Login Manager configured for the correct wallpaper and display layout;
- a polished floating bottom taskbar;
- Vicinae as the single promoted application launcher and command surface;
- mouse snapping and quick-tiling shortcuts;
- a useful subset of Omarchy-inspired bindings;
- Ghostty and `btop`;
- a lean default application set;
- the curated application directory;
- straightforward access to selected AI coding agents;
- Fedora's installer and update experience with minimal necessary branding;
- a bootable x86-64 live ISO that installs successfully in QEMU/KVM.

## Explicit non-goals for version 0.1

- A new kernel, package manager, init system, display server, installer, or updater
- A complete replacement for KDE Plasma
- A keyboard-only or mandatory tiling workflow
- A privileged system-wide AI agent daemon
- A new office suite or office applications in the default image
- A separate server, gaming, lightweight, NVIDIA, or atomic edition
- Support for 32-bit machines
- Broad hardware certification or a recruitment campaign for external testers
- A custom public package mirror or large repository operation
- Paid editions or download gates
- Perfect visual consistency inside every third-party application
- Reorganising every page of Plasma System Settings

## Hardware position

Proper Linux version 0.1 inherits Fedora KDE's supported x86-64 hardware range. It should avoid needless overhead and remain usable wherever current Fedora KDE is appropriate, from older supported laptops to high-end workstations. It does not make stronger hardware promises than Fedora and does not treat server hardware as a separate product.

## Success definition

Version 0.1 succeeds when the product manager can:

1. boot the ISO in a VM;
2. install it through the normal graphical installer;
3. reboot into a correctly oriented, correctly branded login screen;
4. log in to the approved Proper Linux desktop;
5. use the taskbar, browse apps, search with Vicinae, and arrange windows entirely with the mouse;
6. perform the same window operations efficiently with shortcuts;
7. toggle a polished Ghostty terminal and run `btop`;
8. install a curated application without understanding its package source; and
9. update the system using Fedora's normal mechanism.

The product manager must approve the five visual checkpoints described in `ACCEPTANCE.md`.

## Public description

> Proper Linux is normal Linux with proper defaults: Fedora KDE underneath, a finished desktop on top, excellent mouse and keyboard workflows, a first-class terminal, and common software one click away.
