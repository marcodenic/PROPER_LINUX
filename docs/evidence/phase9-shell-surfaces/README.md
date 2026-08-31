# Phase 9 shell-surface evidence

## Environment

- Installed Fedora 44 Proper review VM, not a container or HTML mock-up
- 1920×1080 framebuffer at 100% and 200% scale
- Blur enabled for the primary set and explicitly unloaded for the fallback
  capture
- `proper-look-and-feel-0.1-10.fc44.noarch`
  (`ddee8fad9ca06dd19e3b72ddc21a889b3baad1f520575fbced77749191965631`)
- `proper-defaults-0.1-13.fc44.noarch`
  (`15314e4ee8cf96dc206e4352106f89b997e7656c906cee8a899370f424b9a582`)

## Captures

1. [Taskbar at rest](01-taskbar.webp)
2. [Vicinae from the taskbar](02-vicinae.webp)
3. [Clock and calendar](03-calendar.webp)
4. [Expanded system tray](04-tray.webp)
5. [Notification popup](05-notification.webp)
6. [Notification history](05b-notification-history.webp)
7. [Volume OSD](06-volume-osd.webp)
8. [Connected-network panel](07-network.webp)
9. [Audio empty state](07b-audio-empty.webp)
10. [Power management](07c-power-management.webp)
11. [Brightness and colour](07d-brightness-colour.webp)
12. [Brightness OSD](07e-brightness-osd.webp)
13. [Clipboard empty state](08-clipboard.webp)
14. [Emoji selector](09-emoji.webp)
15. [Polkit failure state](10-polkit-failure.webp)
16. [Alt+Tab switcher](11-alt-tab.webp)
17. [KWin Overview](12-overview.webp)
18. [KWin Desktop Grid](13-desktop-grid.webp)
19. [Taskbar at 200%](14-scale-200-panel.webp)
20. [Notification at 200%](15-scale-200-notification.webp)
21. [Readable blur-disabled fallback](16-blur-disabled.webp)

## Interaction results

| Surface | Pointer path | Keyboard path | Result | Recommendation |
| --- | --- | --- | --- | --- |
| Taskbar and tasks | Clicked all three pinned applications and status items | Alt+Tab exercised with two applications | Pass; Ghostty now groups under its pinned launcher | Keep upstream Icon Tasks with Proper's curated layout |
| Vicinae | Taskbar button opened it reliably | Existing `Meta+Space` path retained | Pass | Keep Vicinae |
| Tray and clock | Expanded tray and calendar by pointer | Focus and Escape paths retained | Pass | Keep upstream Plasma widgets |
| Notifications | Popup, timeout, close affordance, and Discover busy state exercised | Upstream focus path retained | Pass | Keep upstream delivery and history |
| OSDs | Volume status remains discoverable through the tray | Volume-up and mute keys exercised | Pass | Keep upstream workspace OSD |
| Network | Opened connected wired state and its actions | Search field accepts focus | Pass | Keep `plasma-nm` |
| Audio | Opened the no-device VM state | Volume and mute keys exercised | Pass for empty state; VM has no audio device | Keep `plasma-pa` |
| Power and brightness | Opened balanced profile, sleep-blocking, brightness, Night Light, and theme controls | Brightness key OSD exercised | Pass for desktop state; VM has no battery | Keep PowerDevil |
| Clipboard | Pointer-accessible tray item retained | `Meta+V` opens searchable history | Pass | Keep Klipper and surface it through Vicinae later |
| Emoji | Ordinary window is pointer operated | `Meta+.` opens it | Pass | Keep the KDE selector |
| Authentication | Buttons and Details remain ordinary controls | Failure, cancellation, and success exercised | Pass | Keep the KDE Polkit agent |
| Workspace controls | Overview/Grid expose pointer controls | Alt+Tab, `Meta+W`, and `Meta+G` exercised | Pass at the normal desktop size | Keep upstream KWin effects |
| Blur fallback | N/A | Blur effect explicitly unloaded and restored | Pass; all text and icons remain legible | Keep blur as enhancement, never a dependency |

The 200% pass used the same 1920×1080 virtual output, producing a deliberately
small 960×540 logical workspace. The panel, notification, calendar, clipboard,
network panel, OSD, and task switcher stayed inside the viewport and remained
legible. KWin Overview becomes very dense at that logical size; Proper will not
fork it in version 0.1 because normal window switching and pointer workspace
controls remain available.

The VM exposes one wired network interface, no Bluetooth adapter, no battery,
and no real audio device. BlueDevil, PowerDevil, and Plasma PA remain
Fedora/KDE-owned and their hardware-present states require later hardware or a
suitable emulated device. A second-display placement capture is likewise not
represented by this single-output VM. These are evidence limits, not
replacements with Proper code.
