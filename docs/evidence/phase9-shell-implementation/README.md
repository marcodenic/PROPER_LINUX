# Phase 9 approved shell implementation

Status: first approved implementation, exercised in the installed Fedora 44
review VM at 1920x1080.

## Evidence

1. `01-desktop-soft-shelf.png` — variant D as one centred, fit-content upstream
   Plasma panel, including the quiet search launcher.
2. `02-pointer-launcher.png` — the launcher opened by clicking the search glyph;
   favourites, applications, files, clipboard, emoji, and commands remain
   pointer-selectable.
3. `03-calendar.png` — neutral charcoal popup and heading with blue limited to
   selection and focus.
4. `04-network.png` — the upstream `plasma-nm` workflow on the same surface
   system.
5. `05-notification.png` — upstream notification behaviour with the Proper
   charcoal container. The thin blue line is progress, not a title bar; the
   information glyph belongs to the notification payload and varies by sender.

## Implementation boundary

The result is a deliberately partial Plasma Style. Proper owns the panel,
dialog, heading, tooltip, and translucent-background assets and lets missing
elements fall back to Breeze. Plasma continues to own task handling, tray,
notification delivery, networking, audio, power, clipboard, OSD, authentication,
and workspace behaviour.

The taskbar launcher is presented as **Applications & Search** with a semantic
search icon. Its implementation remains the pinned, source-built Vicinae. The
installed source indexes displayable desktop applications, including Plasma
System Settings, and supplies built-in lock, log-out, sleep, restart, and power
commands. Proper enables Vicinae's upstream-disabled **Browse Apps** command and
pins it first for an alphabetical, pointer-scrollable all-apps view. KRunner
remains installed as an unobtrusive fallback.

This is functional menu coverage, not a Kickoff-style category tree: **Browse
Apps** is an alphabetical list, while the home field narrows applications and
commands by name. Proper can retain a stock launcher as an unpromoted fallback
if later pointer testing exposes an inaccessible entry.
