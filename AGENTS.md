# Proper Linux repository instructions

## Required context

Before changing the repository, read only these project documents:

1. `docs/PRODUCT.md`
2. `docs/ARCHITECTURE.md`

Use `PRODUCT.md` for intent, `ARCHITECTURE.md` for ownership and delivery, and
the owning spec or lock for exact versions and provenance. Resolve ordinary
implementation decisions; ask only when product direction or authority must
change. The user is the product manager, and their visual judgement is
authoritative.

## Product and architecture invariants

- Keep Fedora's mutable foundation and upstream system components. Proper owns
  curation, defaults, presentation, and integration.
- Prefer supported Plasma extension points and versioned RPM defaults over
  forks or copied home directories. Seed once; preserve later user choices.
- Give every ordinary action a pointer path. Shortcuts, snapping, tiling, and
  workspace arrangement are accelerators; windows float by default.
- Remove noise and duplication, keep the image lean, and put optional software
  in Proper Apps.
- Keep project-owned functions and UI components focused and single-purpose.
  Refactor mixed responsibilities rather than adding branching or nesting.
- Do not increase measured complexity in changed code. Necessary exceptions
  require focused tests and a brief justification; never raise or suppress a
  configured limit silently.

## Research and upstream documentation

- Before visible UX or platform-integration work, consult current official KDE,
  Fedora, and Qt guidance for the component and shipped version. Verify
  newer-only documentation against the pinned source.
- Prefer primary documentation and source to tutorials. Record material
  compatibility or UX constraints in the handoff.
- Guidance informs implementation; `PRODUCT.md` and product-manager approval
  remain authoritative for Proper's design.

## Validation decision table

| Scope | Required validation |
| --- | --- |
| Source or UI | Focused static checks and the cheapest representative disposable preview. |
| Package | Build only the owning RPM or smallest required set; reuse safe matching outputs. |
| Image integration | Finish source and package work, then perform one ISO build and one graphical pass. |

Image integration means image composition, boot, installer, first boot, or live
behaviour; an explicit release, installation, or VM review; or behaviour no
cheaper loop can validate. Merely shipping a UI package on the ISO does not
qualify. State why a full ISO build is needed before starting it.

## Safety and release rules

- Git is Proper's canonical distribution source. Releases are agent-assisted
  source builds identified by signed tags, without a hosted ISO or Proper
  package server.
- Fedora provides ordinary system and security updates. Proper updates use
  verified release source and never pin or restore stale Fedora code.
- Pin external inputs and keep source, checksum, licence, patch, and update
  method beside the owning package or lock file.
- Keep secrets and generated artifacts out of Git. Never expose signing
  credentials to untrusted code.
- For VM review, use only `scripts/run-vm` with its single-output `fullhd` GTK
  default: 1920×1080, 100% scale, zoom-to-fit, and a maximised window. Run one
  Proper VM at most; verify its ISO, disk, PID, and sockets before reuse or
  shutdown, and never kill QEMU by a broad name match.
- Capture the screen after graphical input. Command success is not visual
  evidence.

## Definition of done

A change is done when it is versioned, preserves user choices and pointer use,
and passes its validation level. Report exactly what ran; never claim unrun
package, image, installation, or VM validation. Image integration also requires
installed-system and screenshot evidence.
