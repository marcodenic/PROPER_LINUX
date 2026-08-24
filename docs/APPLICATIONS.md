# Proper Linux application policy and initial catalogue

## Goal

Make the obvious software easy to install without forcing users to understand Fedora packaging, Flatpak remotes, vendor repositories, or community build systems.

Proper Apps is a curated directory and installation front end. It is not a new package manager.

## Default image

### Intentionally included

- Firefox or Fedora's maintained default browser as a safe initial browser
- Dolphin file manager
- Ghostty terminal
- `btop`
- Vicinae
- KDE System Settings
- KDE Discover and the system package/Flatpak backends Proper Apps delegates to
- Git and a small set of ordinary developer/system utilities
- Proper Linux themes, settings, catalogue, and integration helpers

### Intentionally excluded

- LibreOffice, Calligra, OnlyOffice, or another office suite
- Multiple preinstalled browsers
- Large IDEs and SDK collections
- Communication clients
- Gaming libraries and launchers
- Creative suites
- Local language models
- Every available AI-agent CLI
- Duplicate terminals, app launchers, software centres, or media applications without a clear fallback role

The upstream Fedora KDE package set must be reviewed rather than assumed lean. Remove unneeded defaults through the image description, not with a post-install cleanup script.

## Priority catalogue

These entries serve the primary customer's actual workflow and must be implemented first.

| Application | Role | Intended treatment |
|---|---|---|
| Google Chrome | Primary browser choice | One-click enable/install from Google's supported Linux source; do not redistribute proprietary binaries without permission. |
| GitHub Desktop | Git GUI | Validate the best maintained Linux community port and clearly label that it is not an official GitHub Linux release if that remains true. |
| Visual Studio Code Insiders | Editor | Install from Microsoft's supported repository/package and preserve its update path. |
| Codex | Coding agent | Use OpenAI's current supported installation and authentication path. |
| Docker tooling | Containers | Offer Docker Engine/Desktop as appropriate for Fedora and explain conflicts with existing container tooling only when relevant. Do not silently replace Fedora components. |

## Secondary catalogue

The initial catalogue may include the following after source and licence review.

### Web

- Chromium
- Brave
- Firefox variants only if they solve a clear need

### Communication

- Discord
- Slack
- Signal
- Telegram
- Zoom

### Media

- Spotify
- VLC
- OBS Studio

### Passwords and notes

- Bitwarden
- 1Password
- Obsidian

### Development

- Stable Visual Studio Code
- Zed
- JetBrains Toolbox
- Podman Desktop
- common database clients only when requested

### AI

- Claude Code
- OpenCode
- Gemini CLI
- LM Studio
- Ollama

### Creative

- Blender
- Krita
- GIMP
- Inkscape
- Kdenlive

### Gaming

- Steam
- Heroic Games Launcher
- Lutris

### Utilities

- Flatseal
- LocalSend

Office software is intentionally omitted from the initial catalogue. It can be added later if actual demand appears; it does not deserve privileged placement merely because Linux distributions traditionally ship it.

## Source-selection policy

For each application, choose the first source that is maintained, distributable, and appropriate:

1. Verified or upstream-maintained Flatpak
2. Fedora RPM
3. Official vendor repository or package
4. Clearly identified community-maintained package
5. AppImage or a custom integration as a last resort

The policy is not “Flatpak always.” It is “one dependable path selected by the product.”

## Catalogue data requirements

Each entry must record:

- stable ID;
- display name;
- short, plain-language purpose;
- category;
- homepage;
- icon and icon licence;
- selected provider and package/application ID;
- whether the provider is official, upstream, Fedora, or community-maintained;
- supported architectures;
- proprietary/open-source status;
- install, installed-state, launch, update, and uninstall behaviour;
- known caveats; and
- date/source of the last validation.

Provider facts must live in data rather than being buried in UI code.

## User experience

Normal application cards show:

- icon;
- product name;
- one-sentence description;
- Install/Open button; and
- installed/progress state.

Advanced details may show provider, licence, download size, homepage, architecture, and maintenance status.

Do not show package names, remote names, repositories, or command lines as the dominant card content.

## Safety

- Never pipe downloaded scripts into a privileged shell.
- Prefer signed repositories and verifiable publisher identities.
- Do not bundle proprietary applications when their licence permits installation but not redistribution.
- Clearly identify community ports such as a Linux GitHub Desktop build.
- Never collect or store application credentials.
- Use the standard authentication dialog for privileged installation.
- Failed installs must leave the provider/package system in a recoverable state.
