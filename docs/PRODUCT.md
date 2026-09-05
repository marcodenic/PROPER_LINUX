# Proper Linux product and experience

## The idea

Proper Linux is a tasteful Fedora KDE desktop for people who want full Linux
power without accepting the usual rough edges, visual clutter, or hours of
post-install configuration.

It is aimed first at its product manager and at technically capable people with
similar preferences: mouse users who also value good shortcuts, developers who
live in browsers and terminals, and anyone who wants strong defaults without
losing the freedom to change them.

The product promise is simple: install the system, log in, and find a computer
that already feels considered.

## Ethos

- **Defaults are the product.** Customisation remains available, but it is not
  an excuse to ship an indecisive or unfinished starting point.
- **Curate aggressively, restrict sparingly.** Proper chooses what to promote
  and what to omit while keeping Plasma settings, DNF, Flatpak, the terminal,
  and the underlying system available.
- **Mouse and keyboard are peers.** Every ordinary operation has a visible
  pointer path. Shortcuts make frequent actions quicker; they are never an
  entrance exam.
- **Remove noise before adding features.** Fewer duplicate apps, redundant
  controls, popups, tooltips, panels, and setup screens make the useful parts
  easier to see.
- **Use the mature foundation.** Fedora and KDE continue to own the kernel,
  hardware support, networking, security, installer, updates, compositor, and
  ordinary system controls.
- **Respect ownership.** Defaults seed a new profile once. Updates do not keep
  resetting choices the user has made.
- **Be honest and open.** Preview releases are public, signed source revisions
  that a user or their agent can build without an account, paid edition, or
  deliberately limited source tree.

## What changed and why

### A calmer starting point

Proper opens on a clean desktop with no icons, forced tour, welcome carousel,
or wall of configuration choices. The default is dark, uses Inter for interface
text and JetBrains Mono where fixed-width text belongs, enables natural
scrolling for new pointer profiles, and keeps normal application content
opaque. Translucency is reserved for the shelf, shell popups, authentication,
and terminal, where it adds a sense of place without making work harder to
read.

This is the clearest expression of the product: dozens of small defaults work
together, and none is allowed to become a permanent override of the user's
later preferences.

### Arrival and appearance

Boot, login, lock, and desktop share Proper's identity and selected wallpaper.
Login and lock screens are quiet, clock-first surfaces whose authentication
controls appear when needed; account and power functions remain reachable
without permanently covering the artwork.

Proper Appearance offers a small preview-first set of coherent styles, three
coordinated text-size presets, and the curated wallpaper gallery. It changes
the normal KDE, GTK, terminal, desktop, and lock settings rather than creating a
second theme system. The result is personalisation with clear choices instead
of another settings maze.

### The shelf and system surfaces

The desktop uses one centred, floating bottom shelf. Its quiet resting material
keeps the wallpaper present through native compositor blur, a restrained tint,
and a directional rim and shadow. Its material stays consistent when a window
meets it.
It contains the Proper launcher, browser, Files, terminal, running applications,
system status, and a readable clock and date. A compact gap separates tasks from
status. Selected status glyphs share consistent rounded strokes; the calendar
remains one click away. The active application has one short line. An inactive
application has one small dot per window, capped before the count becomes
visual noise, and an opening application has one oscillating dot. Running
applications expose their native window previews on hover; status tooltips pair
a recognisable icon with a clear title and secondary status after a restrained
delay. The shelf grows when needed but
keeps visual separation between application tasks and status controls. Where
compositor animations are available, its first appearance uses one eased reveal that lets its contents settle. App icons retain clear space above
their running marks.

Network, Bluetooth, audio, power, notifications, authentication, overview, and
workspace controls remain KDE's maintained components. Proper gives their
containers and common controls one calmer visual language, with bounded focus
layers and coherent toggles, without rearranging or forking their behaviour.
This keeps the desktop coherent without taking on fragile replacements for
security- and hardware-sensitive code.

A quiet Command Centre button in the shelf opens its bounded surface by pointer
or `Meta+S`. It gives a current view of CPU temperature and load, memory, root
storage, the active network and its last minute of in-memory throughput, and
installed-agent usage, with readable desktop typography and an explicit
unconnected-agent state. The surface is always available; the absence of Codex
or Claude is shown as a neutral state instead of hiding the system view. It
complements rather than replaces KDE's maintained network, audio, power, and
notification controls in the shelf.

### One launcher, many useful paths

Vicinae is the promoted application launcher and command surface. Clicking the
Proper button or tapping `Meta` opens a useful home with favourites, recent
items, installed applications, and common actions before the user types.
Search extends to applications, files, clipboard history, commands, settings,
and supported extensions. KRunner remains available as a quiet fallback.

Start Here is a passive hub for applications, appearance, updates, shortcuts,
System Settings, and support. Start Here never autostarts and does not turn first
boot into onboarding. System Settings opens on a concise set of everyday
settings cards, with coordinated symbolic category icons; the complete sidebar
and search remain available.

### Windows that work both ways

Windows float, overlap, drag, resize, minimise, maximise, and close normally.
Title bars use frosted material matched to the selected light or dark style,
without a painted frame around application content.
Edge snapping and quick tiling make halves and quadrants easy with either mouse
or keyboard. Arrange Workspace can temporarily place eligible windows into a
chosen native KWin layout and restore their previous floating geometry; new
windows stay floating. Balanced halves is the default for two windows, and
dragging their shared edge resizes both sides together.

This avoids the false choice between a conventional desktop and a fast tiling
workflow. The layout editor, window buttons, pointer actions, Vicinae commands,
and shortcut guide keep the system discoverable.

### Cleaner everyday applications

Dolphin remains the file manager because it has excellent Plasma integration,
remote locations, previews, tabs, split view, undo, trash, and removable-device
support. Proper presents it as Files with a plain blue folder identity, a
restrained toolbar and sidebar, hides optional panels and duplicated controls
by default, and adds Open in Ghostty.

Chromium is the promoted browser. Ghostty 1.3.1 is the default terminal, with a
coherent palette, an edge-to-edge terminal canvas, uniform translucency, and `btop` included.
These are ordinary applications in ordinary windows, not special modes the user
must learn.

### Less baggage, more useful choice

The base image contains one clear default for each common job and removes
office suites, personal-information stacks, bundled games, duplicate media
apps, redundant launchers, and promotional welcome software. Core printing,
camera, remote-desktop, installer, updater, and system tools remain.

The build enforces a complete image below 3 GiB. Start Here presents that as
evidence of deliberate curation—not as a vanity number—and explains that the
broader software catalogue remains one click away.

Optional software belongs in Proper Apps. Its cards show recognisable products,
plain descriptions, and one Install or Open action. Provider, licence, and
maintenance details remain inspectable without dominating the normal flow.
Proper Apps delegates installation and updates to Fedora, Flatpak, or a vetted
vendor source; it does not become a package manager. It explains progress,
cancellation, partial results, offline state, and storage problems in human
terms and reconciles what is actually installed before reporting success.

The broad catalogue can include browsers, communication, media, development,
creative, gaming, container, printer, and AI tools. Its Recommended shelf presents Codex Desktop, Spotify, and GitHub Desktop.
The browser, terminal, and file manager are already installed. Start Here uses
short, practical guidance rather than a product manifesto.

### Developer and agent workflow

Git and a compact set of useful command-line tools are present without turning
the image into a preinstalled SDK collection. Codex, Claude Code, OpenCode, and
other reviewed tools are easy to install and launch. A generic Coding Agent
action asks the user which client to use, remembers only a valid explicit
choice, and opens it in Ghostty at the requested directory.

Provider authentication stays in each agent's normal flow, and Proper never
silently falls back to a different client.

When a supported agent is installed, a compact meter appears as a right-aligned
sibling of the taskbar. It has the same height, edge inset, material, and native
floating-to-attached response while showing the useful part at a glance:
current remaining usage. A normal rectangular detail panel adds each available
usage window and its reset time. It does not invent historical charts, expose
credentials, or add another menu bar. Clicking the meter is the ordinary
pointer path; installing no agent leaves no visible placeholder.

## Core shortcuts

| Shortcut | Action |
| --- | --- |
| `Meta` or `Meta+Space` | Open or close Vicinae |
| `Meta+Return` | Open Ghostty |
| `Meta+Left/Right` | Tile to a half |
| `Meta+Up/Down` | Maximise or restore |
| `Meta+1/3/7/9` | Tile to a quadrant |
| `Meta+W` | Arrange or restore the workspace |
| `Meta+O` | Open Overview |
| `Meta+S` | Open or close Command Centre |
| `Meta+T` | Open Plasma's visual tile editor |
| `Meta+/` | Open the shortcut overview |

Every listed action also has an ordinary pointer route.

## Product boundaries

Proper Linux 0.1 is an agent-assisted source-build preview of a mutable Fedora
KDE x86-64 desktop and installer image. It is not a new kernel, package
manager, init system, compositor, installer, updater, or office platform. It
does not include mandatory tiling, broad hardware certification, specialised
editions, a hosted ISO, or a large Proper-operated software mirror.

The release is good when it builds reproducibly, installs through the normal
graphical path, boots into the intended experience, keeps Fedora updates
working, preserves user customisation, and makes its daily tasks comfortable
with either pointer or keyboard. Visual polish counts only when the resulting
system remains legible, accessible, and reliable in real applications.
