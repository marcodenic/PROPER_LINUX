# Plasma shell-surface review

## Purpose

This review defines how Proper Linux should evaluate and refine the visible
Fedora KDE/Plasma shell without taking ownership of the shell itself. It covers
Plasma 6.7.4 on Fedora 44, the current version 0.1 base.

The architectural review can proceed while Phase 8 is in progress. Final
same-VM screenshots and interaction tests must use the installed Phase 8 result
so that arrival work, shell styling, and user-setting persistence are assessed
together.

## Current Proper baseline

`proper-look-and-feel` is already a Proper Global Theme, but it selects Breeze
application styling, Breeze Dark colours and icons, and the `breeze-dark`
Plasma Style. The custom lock screen is the exception. Consequently, the panel,
task states, tray, widget pop-ups, notifications, tooltips, and OSDs are still
substantially Breeze-derived.

Fedora currently supplies these useful local baselines:

- Fedora, Fedora Dark, and Fedora Light Global Themes;
- Breeze, Breeze Dark, and Breeze Twilight Global Themes;
- Breeze Light, Breeze Dark, and default Plasma Styles; and
- the standard compact, sidebar, large-icon, cover, and flip task switchers.

This is enough to perform a controlled baseline comparison without installing
third-party code.

## What Plasma lets Proper own

Plasma deliberately separates several levels of customisation:

1. A **Global Theme** selects a coordinated set of colours, icons, Plasma
   Style, window decoration, task switcher, lock-screen package, and optional
   panel layout.
2. A **Plasma Style** supplies the scalable visual assets used by panels,
   widgets, tasks, dialogs, tooltips, and many transient shell surfaces. Missing
   assets can continue to fall back to Breeze.
3. Colour schemes, icon themes, fonts, KWin decorations, panel configuration,
   and supported widget settings refine the result without replacing the
   components.
4. A widget, KWin effect, task-switcher package, or source patch changes
   composition or behaviour. Proper then owns more code and update risk.

The relevant upstream interfaces are documented in KDE's
[Plasma customisation overview](https://develop.kde.org/docs/plasma/),
[Plasma Style tutorial](https://develop.kde.org/docs/plasma/theme/), and
[theme-element reference](https://develop.kde.org/docs/plasma/theme/theme-elements/).

## Surface ownership and initial recommendation

| Surface | Fedora/Plasma owner | Supported visual controls | Boundary for deeper change | Initial Proper direction |
| --- | --- | --- | --- | --- |
| Taskbar/status bar | Plasma panel, Task Manager, clock, and widgets | Panel layout/configuration, Plasma Style, colours, icons | Different task semantics or widget structure requires widget work | Keep upstream behaviour; refine proportions, states, spacing, and surface assets |
| Application launcher | Vicinae is promoted; Kickoff/Kicker/KRunner remain installed | Vicinae configuration; Plasma controls for stock launchers | A new launcher means owning a separate application/widget | Keep Vicinae; use stock launchers only as comparison and fallback |
| System tray | Plasma System Tray and StatusNotifier items | Plasma Style, icon theme, tray configuration | Third-party applications own many tray icons and menus | Theme the container; test hostile icons and overflow rather than replacing the tray |
| Notifications | Plasma Notifications applet and service | Plasma Style, colours, icons, placement, settings | New grouping, history, or interaction model requires widget/service code | Retain upstream notification behaviour; redesign visual hierarchy only if necessary |
| Volume/brightness OSDs | Plasma workspace OSD | Plasma Style, colours, icons, look-and-feel assets | Different composition or timing requires QML/source-level work | First make the stock OSD coherent through the Proper style |
| Network panel | `plasma-nm` applet | Plasma Style, colours, icons, supported applet settings | Reordering or changing connection workflow requires applet work | Keep the upstream, security-maintained workflow |
| Bluetooth panel | BlueDevil applet | Plasma Style, colours, icons, supported applet settings | A new pairing/device workflow requires applet work | Keep upstream behaviour and test empty, pairing, error, and connected states |
| Audio panel | `plasma-pa` applet | Plasma Style, colours, icons, supported applet settings | A new mixer/routing model requires applet work | Keep upstream behaviour; review density and device legibility |
| Power panel | Plasma battery applet and PowerDevil | Plasma Style, colours, icons, supported settings | A new power-profile workflow requires applet/service work | Keep upstream behaviour and ensure power mode/status is obvious |
| Clipboard | Plasma Clipboard/Klipper applet | Plasma Style, colours, icons, applet settings | New history/search/actions require widget/service work | Keep it and expose it through the promoted launcher path |
| Emoji | KDE emoji selector plus application input methods | Colour/application style and launcher integration | A unified custom picker would be a new maintained surface | Surface the existing selector through Vicinae before considering new UI |
| Lock screen | Proper `ShellPackage`, with upstream fallback elsewhere | Proper lock QML, Plasma Style, colours, wallpaper | Authentication mechanics remain upstream | Keep the approved Phase 8 composition |
| Authentication prompts | KDE Polkit agent and application dialogs | Application style, colours, icons | Composition changes require security-sensitive patch/fork work | Review and style through supported controls; do not fork without a concrete failure |
| Workspace controls | KWin Overview, Desktop Grid, Present Windows, virtual desktops, task switchers | Supported settings, KWin scripts/effects, task-switcher packages | Replacing Overview/Grid behaviour creates ongoing KWin compatibility work | Tune upstream effects and select/create a task switcher only if the baseline fails |

## Candidate strategy

Use Breeze Dark as the behavioural baseline, not as the final visual ceiling.
Compare the installed Fedora/Breeze variants first, then a small set of current
Plasma 6 themes as references. Third-party themes are acceptable only when their
source, licence, Plasma version, update method, and complete installed payload
have been audited. Theme-install scripts and Windows/macOS imitation bundles
must not be imported wholesale into the product.

The likely low-maintenance result is a **Proper Plasma Style** containing only
the approved panel, widget-background, task-state, button, tooltip, and OSD
assets. Unowned elements should fall back to Breeze. This gives Proper a
recognisable shell while Fedora and KDE continue to own networking, Bluetooth,
audio, power, notification delivery, authentication, accessibility, and their
bug fixes.

Current third-party Plasma 6 projects such as
[NeoWin](https://github.com/TuxLux40/NeoWin) demonstrate that Global Themes can
compose an existing Plasma Style, application style, decoration, and icon set.
[KDE Windows Modern](https://github.com/Jeysef/KDE-Windows-Modern) demonstrates
the much larger maintenance surface created by bundling custom applets and tray
components. They are research references, not approved dependencies.

## Required visual review

Capture the same states at 1920x1080 and 200% scaling with blur both enabled and
disabled:

- panel at rest, hover, active, urgent, overflow, and edit mode;
- tray collapsed/expanded and representative third-party icons;
- notification popup, history, actions, progress, and do-not-disturb state;
- volume, muted-volume, microphone, and brightness OSDs;
- network, Bluetooth, audio, battery, power-profile, clock/calendar, and
  clipboard panels in normal, empty, busy, and error states where applicable;
- emoji selection through its promoted pointer and keyboard paths;
- Polkit authentication success, cancellation, and failure;
- Alt+Tab, Overview, Desktop Grid, workspace switching, and multi-display
  placement; and
- lock screen as the already-approved custom comparison point.

For each surface, record whether the approved result requires only tokens and
configuration, a Proper Plasma Style asset, a supported package, or maintained
code. A widget or source patch requires a documented acceptance failure,
explicit PM approval, and an upstream/rebase exit plan.

## Review status

The component and extension-point review is complete, and the validated Phase
8 installed VM is available. The missing-panel regression exposed by the first
same-VM Phase 9 capture is fixed: the Proper ShellPackage now has an explicit
new-user layout and a one-time empty-layout migration. The installed review VM
shows the intended centred, floating, translucent panel with Proper's three
promoted launchers and upstream status widgets.

The installed screenshot and interaction comparison is now recorded, with
labelled contact sheets, in `docs/evidence/phase9-shell-surfaces`. It has not
found a functional acceptance failure that justifies a widget fork. The
provisional version 0.1 boundary for PM review is therefore:

- **configure** the upstream panel and task manager with Proper's small layout;
- **keep** Vicinae as the promoted launcher;
- **keep Breeze-derived** tray, popup, notification, OSD, clipboard,
  authentication, task-switcher, Overview, and Desktop Grid surfaces;
- **keep upstream-owned** network, Bluetooth, audio, battery, and power
  applets; and
- **replace no Plasma component** in Phase 9.

This set is ready for the PM shell-surfaces checkpoint; it is not yet approved.
The evidence also records a Vicinae Bluetooth-search mismatch, conflicting
Proper/Breeze wording in the brightness panel, and the absence of a true
brightness-key OSD capture. Bluetooth pairing/connected, battery-present,
real-audio-device, and second-display states are not representable in the
current single-output VM and remain explicit evidence limits.
