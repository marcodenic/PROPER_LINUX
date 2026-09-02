# Proper Agent Status

This package owns two related native Plasma surfaces: the global Proper Status
Shade and the small Agent Usage meter. Plasma supplies their panel placement,
popup, focus, shortcut, and theme behaviour. The implementation is original
Proper Linux code; it does not copy a menu bar app, Waybar module, or
third-party widget.

## Status shade

The shade is available whether or not a coding agent is installed. Move the
pointer to the top edge to reveal its slim handle, then click or pull down; use
`Meta+S` for the keyboard path. The full-width surface shows:

- current CPU load and package temperature;
- used and total memory and root-storage capacity;
- the active NetworkManager connection plus live upload/download rates;
- a rolling, in-memory 60-second network graph; and
- current Codex and Claude state from the same reduced provider model as the
  compact meter.

The system sampler reads Linux's ordinary `/proc` and `/sys` counters and asks
NetworkManager only for the active connection's display name. Samples exist in
the running widget only; no system or network history is written to disk.

The shade's top-edge panel and shortcut are seeded once. Removing or moving it
later is a user choice and package updates do not recreate it.

## Agent Usage meter

The separate bottom-right meter remains conditional: no supported agent means
no placeholder. When Codex or Claude is installed it is seeded once, shows the
white provider mark and ten-square remaining-usage strip, and opens its existing
detailed limits popup on click.

## Supported inputs

- **Codex:** the stable local `codex app-server` JSON-RPC interface. The helper
  performs the required `initialize` / `initialized` handshake, calls
  `account/rateLimits/read`, prefers the `codex` member of
  `rateLimitsByLimitId`, and falls back to `rateLimits`. It retains only
  `usedPercent`, `windowDurationMins`, `resetsAt`, and an optional plan label.
- **Claude Code:** the supported status-line JSON feed. An explicit Connect
  Claude action installs the capture command in `~/.claude/settings.json`. The
  capture stores only `five_hour` and `seven_day` percentages and reset times;
  any previous status-line command is preserved, proxied, and restorable.

Provider clients continue to own authentication. The helper does not read
their credential files, call private web endpoints, or retain prompts,
transcripts, workspace paths, session identifiers, or historical samples.

## Upstream contract references

- OpenAI, *Codex App Server*: <https://learn.chatgpt.com/docs/app-server>
- Anthropic, *Customize your status line*: <https://code.claude.com/docs/en/statusline>

Both contracts were revalidated on 2026-09-02. Revalidate these pages and the
live adapter tests before changing fields or bumping the supported client
floor.

The compact panel's one-colour provider marks are reduced from the already
pinned official OpenAI developer-site and Anthropic Claude Code artwork in
`packages/proper-apps/icons/`; their publisher trademark terms continue to
apply. The remaining-usage strip is original Proper UI and uses the square-dot
language of the Proper mark.

`tests/fake_codex` implements only the documented handshake and read method. It
is test data, is never installed by the RPM, and supplies deterministic visual
values for an installed-VM review without copying a real account into a guest.
