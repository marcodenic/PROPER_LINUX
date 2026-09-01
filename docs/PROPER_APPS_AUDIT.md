# Proper Apps 2 source audit

## Audit baseline

The Phase 10 Omarchy comparison uses the official `omacom/omarchy` `quattro`
branch at commit `b686ed892d9c3020c3336203f6d34cc75b544e2b`, checked on
2026-08-31. The primary inputs were its
[`omarchy-menu.jsonc`](https://github.com/omacom/omarchy/blob/quattro/default/omarchy/omarchy-menu.jsonc)
and [current manual](https://github.com/omacom/omarchy/tree/quattro/manual).
Proper adopts the breadth and discoverability of the install menu, not its
Arch packages, AUR trust model, Hyprland integrations, or shell scripts.

## Included directions

| Omarchy area | Proper treatment |
|---|---|
| Chrome, Edge, Brave, Firefox, Zen | Curated browser cards; Chromium remains Proper's installed default |
| 1Password, Bitwarden, Dropbox, Spotify, Signal, Tailscale | Maintained Fedora or Flathub path with source status in advanced details |
| VS Code, Zed, Sublime Text, Helix, Vim, Emacs | Fedora, Flathub, or official Microsoft source as appropriate |
| Alacritty, Ghostty, Kitty | Ghostty remains installed by default; safe optional Fedora alternatives are listed |
| LM Studio and Ollama | Honest community-Flathub caveat for LM Studio; Fedora package for Ollama |
| Steam, RetroArch, Minecraft, Lutris, Heroic | Maintained Flatpak path; nothing is preinstalled |
| User-created web apps | Name, validated HTTP(S) URL, optional local icon, launcher, app-mode Chromium window, and removal |

Proper also keeps its existing product-specific priorities and broadens the
directory with communication, media, creative, utility, container, printing,
and official coding-agent entries. Catalogue version 2 contains 55 entries.
The Recommended landing shelf is deliberately much narrower: Google Chrome,
Helium, Signal, VLC, Spotify, GitHub Desktop, Visual Studio Code Insiders,
Codex desktop, Codex CLI, and Claude Code CLI. Everything else remains
searchable in All and its category, including Podman, printing, and Calculator.

## Deliberate exclusions

- Omarchy, Hyprland, Quickshell, Arch, AUR, theme, background, font, and shell
  internals are not applications for Proper's Fedora/Plasma catalogue.
- Arbitrary package and AUR search remain outside Proper Apps. Discover and
  `dnf` remain available for uncurated software.
- Development-runtime installers are deferred until Proper has a coherent
  version-manager policy; blindly translating Omarchy's `mise` setup would
  make the catalogue own developer environments it cannot safely remove.
- Cursor, Grok Bot, T3 Code, NordVPN, ONCE, Sunshine,
  Battle.net, Xbox-controller DKMS, and the Windows VM are omitted because the
  audited snapshot does not supply a low-risk Fedora path that meets Proper's
  provider and removal requirements.
- Google's Antigravity CLI supersedes Gemini CLI for individual users, but its
  current official Linux path is a downloaded shell installer. Proper does not
  execute remote installer scripts from catalogue data. Gemini CLI remains an
  unpromoted, clearly caveated entry for supported Enterprise and API-key
  users until Antigravity has a pinned, reversible provider path.
- Xbox Cloud Gaming and GeForce NOW do not need bespoke installers in version
  0.1; the web-app creator provides the safe general path.
- Anthropic currently documents Claude Desktop for macOS and Windows, not
  Linux. Proper therefore recommends the official Claude Code CLI and leaves
  claude.ai available through the general web-app creator rather than shipping
  an unofficial desktop wrapper.

## Provider checks

- Every Flatpak application ID returned a current Flathub AppStream record on
  2026-08-31.
- Every Fedora package ID was resolved against the Fedora 44 repositories in
  the installed review VM.
- Microsoft VS Code and Docker repository endpoints were fetched and their
  Fedora packages resolved before inclusion.
- Helium uses the project's official Fedora COPR and `helium-bin` package; its
  official Linux packaging repository explicitly recommends that route.
- Codex desktop uses OpenAI's official Fedora 43/44 Linux preview RPM. Proper
  pins the reviewed bootstrap package URL; that package configures OpenAI's
  repository so later updates arrive through the normal system update path.
- Agent npm installs use Fedora 44's actual `nodejs24` and `nodejs24-npm`
  package names, then install into `~/.local`; they do not run npm as root.
- Catalogue install steps are data-only `QProcess` invocations. The validator
  rejects shell-control characters, non-allow-listed installer programs, and
  privileged operations other than Fedora package operations.

Provider status, licence, provider ID, source URL, architecture, caveat, and
validation date remain visible behind the advanced disclosure for every card.

## Artwork audit

Named products use their recognisable AppStream, upstream-project, or official
publisher artwork. The 54 checked-in assets are mapped independently from the
theme-icon fallback so a missing host icon cannot turn a product into a letter
tile. `apps/icon-sources.json` records the exact source URL, pinned source
revision where available, retrieval date, rights note, any image transform,
and SHA-256 for every asset. `scripts/validate-catalogue` rejects missing,
extra, non-HTTPS, or checksum-mismatched ledger entries.

The printer-compatibility entry is a generic capability bundle rather than a
named product, so it deliberately uses Plasma's system printer glyph. Shipping
an upstream product mark does not imply endorsement; upstream copyright and
trademark terms continue to apply.
