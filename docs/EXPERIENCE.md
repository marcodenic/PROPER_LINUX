# Proper Linux experience specification

## Experience statement

Proper Linux should feel familiar within seconds and considered after hours of use. It may borrow successful interaction patterns from Windows, macOS, Raycast, Omarchy, and Plasma, but it must not look like a costume version of any of them.

The visual standard is “clean, contemporary, and tasteful,” not “Linux-themed,” retro, gamer, cyberpunk, or aggressively minimal.

## Design language

### Visual character

- Clean geometry and restrained colour
- Translucency and blur on system chrome such as the taskbar, launchers, overlays, and notifications
- Opaque or nearly opaque content surfaces where reading and sustained work matter
- Clear layering, depth, and focus without excessive borders
- Comfortable spacing and pointer targets
- Smooth, quick animation that communicates state rather than showing off
- A coherent light and dark treatment
- Simple ASCII-influenced branding rather than a complex mascot or imitation corporate mark

Windows 11 and current macOS establish the minimum visual ambition. Raycast establishes the command-surface reference. Neither is a template to reproduce literally.

### What to avoid

- Flat grey boxes presented as “modern”
- Full-width panels that visually dominate the desktop without need
- Tiny controls, cramped tray icons, and ambiguous click targets
- Gratuitous top bars
- Redundant docks and taskbars
- Themes that break native application contrast or legibility
- Excessive gradients, glow, neon, or “hacker” ornament
- Long first-run tours and feature walls
- Exposing package terminology in primary software-install flows

## Arrival experience

### Boot and installer

- Boot branding is minimal and unmistakably Proper Linux.
- Retain Fedora's installer flow unless a concrete defect is found.
- Account creation remains part of installation.
- Do not add a separate onboarding wizard for appearance, accounts, software bundles, or AI tools.

### Login

- Use Plasma Login Manager from current Fedora KDE.
- Display orientation selected during installation must be respected at the first installed login where technically possible.
- The shipped Proper wallpaper is used consistently by the live desktop, installed desktop, lock screen, and login screen.
- The idle lock screen shows only the recognisable wallpaper and a restrained
  clock/date. Typing reveals a compact, unlabelled translucent password field;
  no avatar, account label, placeholder, or submit arrow is shown.
- A quiet three-dot control in the lower-right reveals icon actions for sleep,
  switching user, and power without permanently occupying the wallpaper.
- The login screen uses the same restrained visual language: centred time,
  date, identity, and authentication; no avatar, placeholder text, permanent
  card, or submit arrow. A quiet lower-right three-dot menu contains user,
  session, sleep, restart, and power actions.
- Keep Plasma Login Manager's authentication, session, accessibility, and
  power behaviour. Proper owns only the approved composition and must rebase
  its narrow downstream QML entry-point patch for each PLM update until KDE
  provides a supported external composition surface.
- No user should need to type a password while physically tilting their head to read a rotated display.

### First desktop

After login, the user sees the wallpaper and bottom taskbar. No welcome carousel or forced tour appears. A small non-modal “Start here” entry may exist inside the application launcher, but it must not interrupt use.

## Desktop shell

### Taskbar

- Located at the bottom.
- Visually floating rather than attached edge-to-edge to the viewport.
- Translucent, blurred, rounded, and restrained.
- Visible by default.
- User-selectable intelligent hide and auto-hide modes remain available.
- Pinned and running applications are centred or visually central.
- The Proper launcher affordance and system status have obvious locations without forcing a full-width slab.
- Running, focused, urgent, and pinned states must be distinguishable without noise.

The first implementation should use supported Plasma panel and widget facilities. Replace the shell only if those facilities cannot achieve the approved result.

### Desktop surface

- Clean wallpaper with no icons by default.
- Normal right-click access to relevant desktop options remains.
- Clicking empty wallpaper should be prototyped as a “show desktop” action that hides or reveals windows without changing their state. The product manager decides at the desktop checkpoint whether this remains enabled.
- Virtual desktops and Plasma Activities remain available but are not promoted or given persistent space.

## Launching and finding

### Vicinae

Vicinae is the single promoted launch and command surface:

- opened by clicking the Proper launcher affordance or pressing `Meta+Space`;
- presents a useful mouse-accessible home state with pinned applications, recent items, and common actions before the user types;
- searches applications, files, commands, clipboard history, and supported extensions;
- ships with a useful empty state and initial favourites so it is not a blank search box;
- must support clicking results, scrolling, opening secondary actions, and choosing the screen containing the pointer;
- gains Proper styling primarily through configuration rather than a permanent fork.

### KRunner

Stock KRunner remains available through `Alt+F2` as an unobtrusive fallback. It is not promoted as a third launcher.

## File management

The default file manager should look simpler than stock Dolphin without throwing away the mature operations and Plasma integration underneath it.

Version 0.1 begins with Dolphin configured as a clean Proper “Files” experience:

- a restrained toolbar containing back, forward, location/search, view, and essential actions;
- a useful sidebar for Home, common folders, removable devices, and network locations;
- comfortable grid and list views;
- tabs, split view, previews, drag/drop, undo, trash, and remote locations retained;
- noisy optional panels and redundant toolbar actions hidden by default;
- double-click to open, ordinary selection, and familiar drag behaviour;
- “Open in Ghostty” available from the current folder and context menu; and
- no embedded terminal panel visible by default.

The launcher may display the friendly name “Files” while About/help remains honest that the application is Dolphin. Configuration must use supported defaults and must not overwrite later user changes.

Nautilus and COSMIC Files are comparison candidates at PM checkpoint 2. They should replace Dolphin only if their installed Plasma experience is materially better, not merely because one screenshot is cleaner.

## Window management

### Default model

- Windows are floating by default.
- Title-bar dragging and edge resizing work normally without a modifier key.
- Minimise, maximise/restore, and close controls remain conventional.
- Dragging to the top maximises.
- Dragging to sides and corners exposes useful half and quadrant layouts.
- Visual snap feedback appears before the drop.

### Keyboard acceleration

- `Meta+Left` and `Meta+Right` place the active window into left and right halves.
- `Meta+Up` maximises or advances the selected quick-tile layout.
- `Meta+Down` restores or minimises according to the final interaction design.
- Additional combinations provide quadrants where they do not conflict with application conventions.
- Useful Omarchy bindings are ported when Plasma/KWin has a clear equivalent.

There is no global “now you are in tiling mode” requirement for ordinary snapping. More advanced automatic tiling may be offered later as an optional KWin script if it behaves well with both mouse and keyboard.

### Overview and workspaces

Retain Plasma's existing overview and workspace capability, but do not spend version 0.1 product space redesigning it. Users who care can use it; users who do not should barely notice it.

## Terminal

- Ghostty is the default terminal.
- First launch uses an approved font, palette, padding, cursor, and shell presentation.
- It opens as a normal window through ordinary application launching.
- A taskbar terminal affordance opens an ordinary Ghostty window.
- Dolphin exposes “Open terminal here” using Ghostty.
- `btop` is installed and visually compatible with the default terminal palette.

The terminal is first-class but never required for ordinary desktop operations such as installing a curated application.

## Applications

### Default installation

The image is lean. Keep the browser, file manager, terminal, system settings, software tooling, and essential utilities. Remove office software and other large defaults that do not support the primary customer's workflow.

### Proper Apps

The curated software directory:

- presents product names, icons, short descriptions, and one Install action;
- organises software by meaningful user category rather than package source;
- selects a maintained source according to the policy in `APPLICATIONS.md`;
- shows source and licence information under an advanced disclosure;
- reports progress and failure in plain language;
- hands actual package operations to supported Fedora, PackageKit, Flatpak, Discover, or vendor mechanisms;
- never becomes its own package manager.

## AI tooling

Version 0.1 provides an Agent section in Proper Apps and useful Vicinae actions for:

- Codex
- Claude Code
- OpenCode
- Gemini CLI where support is sound
- optional local-model tools such as LM Studio and Ollama

An installed agent opens in Ghostty or its own supported UI. Authentication remains the provider's flow. Proper Linux does not store provider credentials or grant a background agent root access.

A deeper OS-level OpenCode or agent service is deliberately postponed until its permissions, consent, activity visibility, and failure behaviour are designed.

## Settings and updates

- Retain Plasma System Settings for version 0.1.
- Apply tasteful defaults without repeatedly overwriting user changes.
- Keep advanced controls available.
- Use Fedora's existing updater and update notifications.
- The normal path should communicate “updates available,” “install,” and “restart required” without teaching repository internals.

## Interaction quality

- Normal controls must have obvious hover, pressed, disabled, and focus states.
- Pointer targets must remain comfortable at common scaling factors.
- Keyboard focus remains visible even though keyboard use is not mandatory.
- Important actions must not be hidden exclusively behind right-click or modifier-drag gestures.
- Motion respects reduced-animation preferences where Plasma exposes them.
- Blur and translucency must degrade gracefully when effects are disabled.
