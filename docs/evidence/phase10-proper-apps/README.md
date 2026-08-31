# Phase 10 Proper Apps evidence

## Review status

Implementation and installed-VM validation are complete. This directory is
the PM catalogue-review checkpoint; visual approval is pending.

## Environment

- Installed Fedora 44 Proper review VM under QEMU/KVM
- 1920x1080 framebuffer at 100% and 200% scale
- `proper-apps-0.1-6.fc44.x86_64`
  (`43b06fdc2ade010a54f6ddb3ef7e7a832e1202cdc4cece567dd36e05ea23db11`)
- Catalogue v2 with 53 entries
  (`4a0efe64f5abaa7883e9b31322e4df583060c3e19c61b48274b8bdee9bcea526`)
- 52 checked upstream/publisher icon assets and one generic Plasma capability
  glyph, recorded in `apps/icon-sources.json`
  (`37b8fa7eeb64800e5632be440269634c0f6bfb8c9782e6028ae3f4f30ea6b455`)

## Visual captures

1. [Catalogue home at 1920x1080](01-catalogue-home.webp)
2. [Cross-catalogue search and official code-tool artwork](02-search-code.webp)
3. [Responsive catalogue at 200% scale](03-scale-200.webp)

## Interaction results

| Journey | Installed-VM result |
| --- | --- |
| Browse, filter, search, details | Pointer and keyboard paths passed; a query from Recommended searches the complete catalogue |
| Fedora RPM | VLC installed through the graphical Polkit prompt and opened successfully |
| Flatpak | GNOME Calculator installed for the user, opened, and removed successfully |
| Official vendor/agent path | OpenCode installed through Fedora Node 24 and the official npm package, then opened in Ghostty |
| Web app | Example Domain launcher created, opened in Chromium app mode, and removed with its generated files |
| Failure/recovery | A deliberately non-graphical privileged request produced a bounded explanation with expandable diagnostics; package state remained recoverable |
| Scaling | The catalogue reflowed at 200% without clipped controls; normal 100% scale was restored afterward |

VLC and OpenCode remain installed in the disposable review VM. The Calculator
and generated Example Domain web app were removed at the end of their journeys.

## Icon policy

Named products use recognisable artwork obtained from their current AppStream
record or a pinned official upstream/publisher source. Assets, source URLs,
retrieval dates, transformations, rights notes, and SHA-256 values are recorded
in `apps/icon-sources.json` and checked by `scripts/validate-catalogue`. The
generic printer-support capability is intentionally represented by Plasma's
system printer glyph rather than by a vendor logo.
