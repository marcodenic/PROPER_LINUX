# Proper Linux repository instructions

Read only these project documents before changing the repository:

1. `docs/PRODUCT.md`
2. `docs/ARCHITECTURE.md`

The user is the product manager. Their visual judgement is authoritative.

## Rules

- Preserve Fedora's working foundation and mutable package model. Proper owns
  curation, defaults, presentation, and integration.
- Prefer upstream components, supported Plasma extension points, and versioned
  RPM defaults over forks or copied home directories.
- Every ordinary action needs a pointer path. Floating is the default;
  shortcuts, snapping, tiling, and workspace arrangement are accelerators.
- Keep the image lean, remove noise and duplication, and put optional software
  in Proper Apps.
- Seed defaults once and preserve later user choices.
- Pin external inputs and keep provenance beside the package or lock file.
- Keep secrets and generated build/VM artifacts out of Git.

## Work

- Work through ordinary implementation decisions without stopping. Ask only
  when product direction or authority must change.
- Use the fastest representative feedback loop. For visible work, iterate with
  a local, offscreen, nested, or otherwise disposable preview and provide
  screenshots when they help visual review.
- Do not build an RPM, rebuild the ISO, or start a VM merely because a source
  file changed. Static checks and a local preview are the default during
  iteration.
- Batch related edits and validation. Never run a full build after each small
  change.

## Validation levels

- Source/UI iteration: run focused static checks and the cheapest preview that
  exercises the changed code. This is sufficient while refining a design.
- Package validation: build only the owning RPM or the smallest required set of
  RPMs when package contents, metadata, dependencies, or install behaviour need
  checking. Do not rebuild unrelated packages. Reuse matching build outputs
  when safe.
- Image integration: rebuild the ISO only when the user explicitly requests an
  ISO, release, installation, or VM review; when image composition, boot,
  installer, first-boot, or live-environment integration changed; or when the
  behaviour cannot be validated accurately at a cheaper level.
- A UI package being shipped on the ISO does not, by itself, make every UI edit
  an image-integration change.
- Before starting a full ISO build, state why it is necessary. If it would
  rebuild unrelated heavyweight components, do not start it without an
  explicit integration or release need.
- When image integration is required, finish the accepted source and package
  changes first, then perform one ISO build and one graphical verification
  pass.

## VM reviews

- Apply these rules only when VM validation is required by the validation
  levels above or explicitly requested by the user.
- Always use `scripts/run-vm` with its single-output `fullhd` GTK default:
  1920×1080 at 100% scale with zoom-to-fit.
- Immediately maximise the QEMU window. The guest must fill a normal
  laptop-sized display; never present the tiny default window, VNC, multiple
  outputs, or a high-DPI test profile as the main review surface.
- Run at most one Proper Linux VM and verify its exact ISO, disk, PID, and
  sockets before reusing or stopping it. Never kill QEMU by a broad name match.
- After graphical input, capture the screen and confirm the guest changed
  state. A successful input command alone proves nothing.

## Done

A change is done when it is versioned, preserves user choices, supports the
ordinary pointer workflow, and passes the validation level appropriate to its
scope. Do not claim package, image, installation, or VM validation unless that
level was actually run. Installed-system and screenshot evidence are required
for image-integration work, not for every source or design iteration.
