# UI iteration workflow

## Objective

Make visual and interaction work fast without allowing an unrepeatable
hand-configured development account to become the product.

Use the shortest feedback loop that can answer the current question. An ISO
rebuild is an integration test, not the normal way to adjust colour, spacing or
panel behaviour.

## The three loops

### 1. Live design loop — seconds

Use a dedicated development account in the current Proper VM. Install or link
the in-progress theme, widget, layout or application configuration into that
account and restart only the affected component.

Use this loop for:

- colour, opacity, radius, blur and typography;
- panel geometry and widget ordering;
- icons and component states;
- launcher and terminal styling;
- Dolphin toolbar and view experiments;
- shortcuts, KWin rules and scripts; and
- light/dark and wallpaper comparisons.

Keep editable design tokens in source control. Record the exact files and
commands used to apply the experiment. A change visible only in the development
account is a prototype, not a deliverable.

### 2. Package loop — minutes

After the interaction is worth retaining, move it into the owning Proper RPM,
rebuild that RPM and upgrade it inside the VM.

Verify both:

1. a newly created user receives the intended default; and
2. upgrading the package does not overwrite an existing user's later choice.

Prefer system-installed Global Themes, Plasma styles, layout templates,
widgets, KWin scripts, application defaults and narrowly scoped migrations.
Do not solve iteration speed by copying an entire prepared home directory into
the image.

### 3. Image loop — checkpoint scale

Rebuild the ISO when the change affects or must be verified across:

- boot, Plymouth or ISO identity;
- package inclusion or removal;
- live-user creation;
- installer behaviour;
- Plasma Login Manager;
- first login or new-account seeding;
- installed-system repository configuration; or
- a complete acceptance journey.

Run the image loop before each PM checkpoint and release candidate. It need not
run after every visual edit.

## Promotion path

For each visible change:

1. State the user-visible problem and the acceptance state being targeted.
2. Prototype it in the live design loop.
3. Capture before/after evidence at the relevant scale and desktop state.
4. Record approved design values in versioned tokens or configuration.
5. Package the change in the narrowest owning Proper component.
6. Test a new user and an existing customised user.
7. Include it in the next ISO integration build.
8. Recheck it during the appropriate PM checkpoint.

Do not promote unexplained configuration dumps. Reduce captured configuration
to the settings that intentionally produce the approved behaviour.

## Efficient review

For focused iteration, capture only the states that could have changed. For a
panel adjustment that usually means idle, multiple running applications,
hover/focus, notification/tray, a bright wallpaper region and blur-disabled
fallback. Run the complete matrix in `docs/ACCEPTANCE.md` at the checkpoint.

When a Plasma or KWin reload is sufficient, use it instead of rebooting. When a
fresh user is sufficient, do not reinstall the OS. When login, installer or
image composition is in question, do not infer success from a running developer
session: rebuild and exercise the ISO.

## Source of truth

- The repository owns defaults, packages, assets and migrations.
- The development VM is a disposable rendering and interaction surface.
- Checkpoint screenshots document approval; they are not configuration input.
- User home directories are never copied wholesale into packages or images.
- Upstream versions used by a release are pinned or recorded as required by
  `docs/ARCHITECTURE.md`.
