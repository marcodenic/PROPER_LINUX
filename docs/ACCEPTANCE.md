# Proper Linux acceptance criteria

## Purpose

These checks define whether Proper Linux behaves like the intended product. They are focused on the visible experience and the build/install path required to deliver it. They are not a general Fedora certification programme.

## Global gates

Every version 0.1 candidate must satisfy all of these:

- Builds from the committed repository on BOX without manual changes inside the output filesystem.
- Produces a bootable x86-64 ISO and checksum.
- Boots a graphical live session under QEMU/KVM with UEFI firmware.
- Installs to a blank virtual disk using the included graphical installer.
- Boots the installed disk after the ISO is removed.
- Preserves Fedora's normal network, update, package, and system-settings functionality.
- Contains no secret, private signing key, access token, or user credential.
- Does not require a terminal for the normal flows in this document.
- Does not install an office suite by default.

## PM checkpoint 1 — Login

### Evidence

- Short capture from boot splash to login
- Login screenshot at normal orientation
- Login screenshot or capture using a configured 90-degree display layout
- Login-to-desktop transition
- Login, lock-screen, and desktop wallpaper comparison

### Pass criteria

- Proper Linux identity is visible and restrained.
- Login wallpaper matches the shipped Proper desktop wallpaper by default.
- The chosen display layout can be applied to the login manager.
- Password entry, user selection, power actions, and session selection are usable.
- No Fedora placeholder wallpaper or obviously mismatched theme remains.
- No custom login-layout patch is required merely for novelty.

## PM checkpoint 2 — Desktop and taskbar

### Evidence

- Clean desktop at rest
- Taskbar with no applications running
- Taskbar with multiple pinned and running applications
- Active, inactive, urgent, and hover states
- System tray/clock and a notification
- Light and dark variants
- 100% and high-DPI rendering
- Wallpaper-click “show desktop” prototype
- The configured Dolphin “Files” view beside current Nautilus and COSMIC Files

### Pass criteria

- The taskbar is floating, bottom-aligned, translucent, and visually balanced.
- It remains visible by default and exposes hide behaviour through settings.
- Pinned and running applications are obvious without excessive decoration.
- Blur, colour, contrast, spacing, and animation feel coherent.
- Normal application content remains readable.
- Disabling blur does not leave broken or illegible surfaces.
- The desktop does not resemble an unmodified Fedora KDE screenshot.
- The default file manager has a restrained toolbar and sidebar, visually belongs on the Proper desktop, and completes ordinary copy/move/rename/trash/undo, removable-device, search, preview, tab, and drag/drop flows.
- The PM explicitly confirms Dolphin, Nautilus, or COSMIC Files as the final default after the like-for-like comparison.

## PM checkpoint 3 — Launchers and windows

### Vicinae mouse path

1. Click the Proper launcher affordance.
2. Click a pinned, recent, or empty-state application without typing.
3. Search for an application or file.
4. Scroll and click a result.
5. Open and choose a secondary action without a required shortcut.

### Keyboard path

1. Press `Meta+Space` and launch an application through Vicinae.
2. Press `Alt+F2` and confirm KRunner remains available.
3. Use the documented quick-tile shortcuts.

### Window path

- Drag and resize a floating window normally.
- Drag a window into left/right halves and all supported quadrants.
- Maximise by dragging to the top.
- Use `Meta`+arrow keys for equivalent placement.
- Restore the window to floating state.
- Use at least three retained Omarchy-inspired shortcuts.

### Pass criteria

- No primary launcher or window action requires memorising a key.
- Vicinae works as both the obvious application launcher and the deeper command surface.
- Pointer selection and scrolling work reliably throughout the promoted launcher flow.
- Launcher surfaces open on a sensible display, preferably the display containing the pointer.
- Floating behaviour is always available.

## PM checkpoint 4 — Proper Apps

### Evidence

- Catalogue home and category view
- Search results
- Detail view for a priority application
- Install progress and installed state
- Launch and uninstall/recovery affordances
- An intentional failure state
- Advanced source details
- One AI-agent installation/launch path

### Pass criteria

- The main path asks which application the user wants, not which package format they prefer.
- One Install action initiates the selected maintained provider.
- Authentication prompts come from expected system mechanisms.
- Progress and errors are understandable.
- Source, licence, and maintenance status are still inspectable.
- At least one Flatpak, Fedora RPM, and official vendor-source path has been exercised.
- No office suite appears in the default image; office applications are not a launch priority.

## PM shell-surfaces review

Status: installed-VM evidence is ready in
`docs/evidence/phase9-shell-surfaces`; PM keep/theme/replace approval is
pending.

### Evidence

- Matched 1920×1080 and 200% screenshots for the taskbar, tray, notifications,
  OSDs, network, Bluetooth, audio, power, clock/calendar, clipboard,
  authentication prompts, task switching, Overview, Desktop Grid, and
  workspace switching
- Blur-enabled and blur-disabled views
- Pointer and keyboard interaction captures for every promoted surface
- Normal, empty, busy, action, cancellation, and error states where applicable
- A keep/theme/replace decision for each surface, including source, licence,
  update method, and maintenance owner for every non-Fedora asset

### Pass criteria

- Persistent and transient surfaces share a coherent hierarchy, spacing,
  colour, icon, focus, and motion language.
- Every ordinary operation remains available by pointer and the existing
  upstream accessibility and authentication paths still function.
- Disabling blur, using 200% scaling, or opening a surface on another display
  does not make it illegible or misplaced.
- Network, Bluetooth, audio, power, notification delivery, clipboard, and
  authentication remain upstream components unless a documented acceptance
  failure and explicit PM decision justify maintained code.
- Every custom Plasma Style asset or component is packaged reproducibly and
  survives an upstream package update without resetting user choices.
- The PM approves which surfaces remain Breeze-derived and which receive
  Proper-owned visual assets or targeted implementation work.

## PM checkpoint 5 — Final installed system

### Journey

1. Boot the live ISO.
2. Inspect the live desktop.
3. Start the graphical installer.
4. Create the user and install to a blank virtual disk.
5. Reboot to the installed login screen.
6. Log in.
7. Launch Chrome or another installed browser.
8. Browse applications and use Vicinae.
9. Arrange several windows by mouse and keyboard.
10. Launch Ghostty from the taskbar.
11. Run `btop`.
12. Install one priority application through Proper Apps.
13. Check for updates through Fedora's normal UI.
14. Change a visible Proper default, reboot, and confirm the user's choice persists.

### Pass criteria

- The complete journey contains no unexplained terminal requirement.
- There is no long post-install setup journey.
- No high-priority visual paper cut remains in login, taskbar, launcher, terminal, or software installation.
- User settings are not reset by reboot or normal Proper package updates.
- The product manager says the installed experience is worth using.

## Focused compatibility views

Before version 0.1 approval, capture at least:

- 1920×1080 at 100% scaling;
- a high-DPI mode at 200% scaling;
- a two-display virtual arrangement; and
- one rotated virtual display configuration.

These checks exist because layout and login orientation are part of the product. They do not imply general hardware certification.

## Defect priority

- **P0:** cannot build, boot, install, or log in; destructive data risk.
- **P1:** core mouse interaction unavailable; wrong login orientation/wallpaper; launcher, taskbar, terminal, app installation, or updates unusable.
- **P2:** visible inconsistency or interaction defect that materially damages the Proper experience.
- **P3:** polish issue that can be scheduled after the current checkpoint.

No release candidate may contain P0 or P1 defects. The product manager decides whether P2 defects block approval.
