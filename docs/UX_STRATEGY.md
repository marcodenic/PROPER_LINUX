# Proper Linux UX strategy

## Product position

Proper Linux treats the visible desktop experience as the product rather than
as decoration applied after selecting packages. It is a curated Fedora KDE
desktop whose reason to exist is coherent visual and interaction judgement.

Many distributions primarily differentiate through another concern:

- Debian prioritises a universal, stable software platform.
- Fedora prioritises current upstream technology and close upstream
  collaboration.
- Arch and EndeavourOS prioritise user control and a direct package model.
- CachyOS prioritises performance, hardware and gaming work.
- MX Linux prioritises practical graphical administration and portability.
- Linux Mint prioritises a conservative, familiar desktop.
- Ubuntu combines a modified GNOME desktop with a broad commercial platform.
- Zorin OS invests heavily in familiar layouts and migration from Windows.
- Pop!_OS goes deeper by owning the COSMIC desktop stack.

Proper Linux sits between a themed downstream distribution and a new desktop
environment. It owns the composition, defaults, integrations and quality bar,
but deliberately does not own a compositor, kernel, package manager or
installer while upstream components can satisfy the intended experience.

## What is and is not distinctive

Blur, transparency, rounded panels, launchers and tiling are not individually
new. Plasma, COSMIC, Zorin and other desktops have implemented versions of
them. Proper Linux should not claim invention of these elements.

The differentiator is their composition:

- a restrained translucent floating taskbar;
- one promoted launcher that works well before and after the user types;
- normal floating windows with excellent mouse snapping and keyboard
  acceleration;
- a polished retained terminal workflow;
- a deliberately simplified file manager;
- application installation organised around products rather than package
  formats;
- a lean default installation;
- one visual language from boot through login, lock and daily use; and
- strong defaults without taking normal Linux control away from the user.

Novelty is not a requirement. A familiar component executed exceptionally
well is preferable to an original component that makes the system less useful.

## Taste is an operating model

Taste is more than selecting a wallpaper or increasing corner radii. It
includes deciding:

- what is absent;
- which actions receive visual priority;
- how many competing ways to perform a task are promoted;
- whether a control is understandable without documentation;
- what the user sees while work is in progress or has failed;
- whether pointer targets, focus and contrast remain clear;
- whether defaults survive real applications and imperfect wallpapers; and
- whether a user's later choices survive updates.

Linux projects often expose extensive customisation because preferences vary.
Proper Linux still exposes that power, but customisability is not a substitute
for choosing and testing an excellent default.

The product manager has final authority at the visual checkpoints. This avoids
the ambiguity that occurs when the distribution, desktop environment, theme
and application projects each own only part of the experience.

## A product, not a screenshot

A clean empty desktop is necessary evidence, but it is not sufficient. Every
major visual surface must also be reviewed with:

- ordinary and maximised application windows;
- pinned, running, focused, urgent and failed states;
- notifications and awkward third-party tray icons;
- light and dark content behind translucent chrome;
- blur unavailable or disabled;
- 100% and high-DPI scaling;
- multiple and rotated displays;
- keyboard focus and reduced-animation preferences; and
- GTK, Qt, Electron and Flatpak applications in the same session.

Translucent surfaces must preserve legibility. Increase opacity, add contrast,
or use an opaque fallback when the compositor or background cannot produce the
approved result. Visual ambition does not override accessibility or reliable
operation.

## Relationship to Omarchy

Proper Linux shares Omarchy's belief that curation, aesthetics, themes,
developer tools, terminals, shortcuts and AI clients can form a motivating
whole. Both projects reject the idea that a distribution is merely a package
selection.

Their intended operating models differ:

| Area | Proper Linux | Omarchy |
| --- | --- | --- |
| Base | Versioned mutable Fedora | Rolling Arch Linux |
| Desktop | KDE Plasma and KWin | Hyprland and an Omarchy Quickshell shell |
| Window model | Floating by default; snapping and quick tiling always available | Tiling-centred |
| Input | Mouse and keyboard are peers | Keyboard and terminal forward |
| Applications | Lean base plus curated catalogue | The maintainer's broad omakase application set |
| Configuration | System packages and supported desktop defaults | Managed text configuration, themes and migrations |
| Updates | Fedora mechanisms plus a small Proper RPM repository | Omarchy and Arch update workflow |
| Hardware strategy | Recent mainstream x86-64 hardware first | Modern PC hardware plus explicit Intel Mac support |

Proper Linux should borrow Omarchy's coherence, theme tokens, searchable
commands, shortcut vocabulary and rapid configuration feedback. It should not
adopt a tiling-first operating model, terminal dependence or a rolling package lifecycle
that conflicts with the Proper product promise.
