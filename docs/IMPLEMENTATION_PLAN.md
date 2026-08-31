# Proper Linux implementation plan

## Operating model

The Linux BOX host is the build and VM environment. Work proceeds autonomously inside each phase. The product manager is interrupted only for the five visual checkpoints or a genuine decision that would materially change product scope.

Each phase ends with a concrete artifact or an interaction running in the installed VM. Planning files and package builds alone do not complete a phase.

Visible work follows `docs/UI_ITERATION.md`: use the running development VM for rapid design changes, promote accepted changes into their owning RPM, and reserve full ISO rebuilds for image integration and checkpoint validation.

## Phase 0 — BOX readiness and baseline

### Objective

Establish a fast, repeatable Fedora image-build and VM-review loop.

### Work

- Inspect BOX CPU architecture, distribution, storage, memory, container runtime, virtualisation support, and `/dev/kvm` access.
- Record the host facts in `docs/BOX_ENVIRONMENT.md`.
- Install or configure the minimum required Fedora/KIWI, RPM-build, QEMU/KVM, UEFI firmware, screenshot, and checksum tools.
- Create helper scripts for environment checks rather than relying on remembered commands.
- Pin the Fedora 44 KDE live-image description and record its upstream revision.
- Build an unmodified or minimally wrapped Fedora KDE ISO using the intended toolchain.
- Boot it in QEMU/KVM and confirm the live session and installer are reachable.

### Deliverables

- `scripts/check-box`
- `scripts/build-iso`
- `scripts/run-vm`
- `docs/BOX_ENVIRONMENT.md`
- a locally built baseline ISO and checksum outside Git

### Exit criteria

- One command builds the baseline ISO.
- One command boots it with UEFI and KVM acceleration.
- The graphical live session and installer are visible.

## Phase 1 — Product package skeleton and arrival

### Objective

Turn the baseline into an unmistakable Proper Linux installation and solve the first-login paper cuts.

### Work

- Add RPM build structure for `proper-release`, `proper-look-and-feel`, and `proper-defaults`.
- Replace placeholder Fedora-specific product branding as required for a derivative.
- Create the first simple ASCII-influenced Proper identity.
- Create an original default wallpaper in light/dark-compatible variants.
- Apply the wallpaper to live desktop, installed desktop, lock screen, and PLM.
- Configure the boot splash and product name conservatively.
- Determine how the live installer session's selected display layout can be copied into the installed PLM configuration.
- If automatic installer-to-greeter transfer is not viable, implement the smallest visible “Use this display layout at login” action and document the first-login limitation for the prototype.
- Produce an installable ISO and complete an installed-VM boot.

### Deliverables

- first Proper RPMs
- branded installable ISO
- documented display-layout mechanism
- installed VM with coherent boot/login/desktop wallpaper

### PM checkpoint 1 — Login

Show the boot-to-login path, login screen at normal and 90-degree rotation, and transition into the desktop. Approval criteria are in `ACCEPTANCE.md`.

## Phase 2 — Desktop shell and visual system

### Objective

Deliver the core visual identity and daily mouse surface.

### Work

- Define versioned design tokens for colour, opacity, radius, blur, spacing, animation timing, and typography.
- Implement the Plasma Global Theme and colour scheme.
- Configure a floating, fit-content bottom panel.
- Place the launcher, pinned/running applications, terminal affordance, system tray, and clock.
- Style taskbar states and system overlays coherently.
- Configure wallpaper-click “show desktop” as a reversible prototype.
- Simplify and style Dolphin as the initial Proper “Files” experience.
- Install current Nautilus and COSMIC Files in the development VM for a like-for-like PM comparison without adding them to the image.
- Verify light/dark variants, blur-disabled fallback, 100% scaling, and a high-DPI configuration.
- Ensure changes apply to new users without overwriting later customisation.

### Deliverables

- `proper-look-and-feel` usable in the installed VM
- `proper-defaults` panel layout
- design-token source files
- checkpoint screenshots

### PM checkpoint 2 — Desktop/taskbar

Show the clean desktop, taskbar idle and active states, tray, notifications, light/dark treatment, an overlapping-window scene, the wallpaper-click behaviour, and the configured file manager beside Nautilus and COSMIC Files.

## Phase 3 — Launching and window workflow

### Objective

Combine excellent pointer discovery with fast command and window shortcuts.

### Work

- Package a pinned Vicinae release as a Proper-managed RPM if no suitable trusted Fedora package exists.
- Configure the Proper taskbar launcher action and `Meta+Space` to open Vicinae.
- Seed useful Vicinae favourites and empty-state actions.
- Keep `Alt+F2` mapped to KRunner.
- Audit all primary Vicinae actions with a mouse.
- Configure edge/corner snapping and visible layout feedback.
- Configure Windows-style `Meta`+arrow quick tiling.
- Map useful, non-conflicting Omarchy shortcuts to KWin/Plasma equivalents.
- Document shortcuts in an attractive, searchable reference reachable from the launcher.

### Deliverables

- a single polished, pointer-accessible Vicinae entry point
- working mouse and keyboard window arrangement
- shortcut manifest and user reference

### PM checkpoint 3 — Launcher and windows

Demonstrate launching pinned/recent applications entirely with the mouse, searching and acting in Vicinae with both mouse and keyboard, dragging/snapping windows, quick tiling, and normal floating-window behaviour.

## Phase 4 — Terminal and developer essentials

### Objective

Make the terminal and essential technical workflow feel intentionally designed.

### Work

- Package or select a maintained Ghostty source for Fedora.
- Apply the approved font, colours, padding, cursor, and shell presentation.
- Make Ghostty the default terminal.
- Add an ordinary Ghostty launcher to the taskbar.
- Integrate “Open terminal here” into Dolphin.
- Install and theme `btop` appropriately.
- Ensure Git and expected baseline developer utilities are present without turning the image into a large SDK bundle.

### Deliverables

- normal Ghostty workflow
- Dolphin integration
- `btop` in the image

### Exit criteria

- Clicking the taskbar terminal affordance opens Ghostty normally.
- Ghostty is used by launcher actions and file-manager terminal actions.

## Phase 5 — Proper Apps and agent access

### Objective

Provide one clear installation surface for the applications the primary customer actually uses.

### Work

- Define and validate the catalogue schema.
- Implement the smallest polished native catalogue UI, preferably with Qt/Kirigami so it integrates with Plasma.
- Implement provider adapters without creating a new package manager.
- Add the priority catalogue entries first: Chrome, GitHub Desktop, VS Code Insiders, Codex, and Docker tooling.
- Add the reviewed secondary categories from `APPLICATIONS.md`.
- Clearly label community-maintained software only in advanced details.
- Add install progress, installed state, launch, and failure recovery.
- Add Vicinae actions to open Proper Apps searches and launch installed agents in Ghostty.
- Validate at least one Flatpak, one Fedora RPM, and one official vendor-source installation path.

### Deliverables

- `proper-apps` package
- versioned catalogue manifest
- initial agent-launch actions
- focused installation tests

### PM checkpoint 4 — Software directory

Show the catalogue home, search, application detail, one-click install, installed state, failure state, and an agent being launched. Package terminology must not dominate the normal flow.

## Phase 6 — Integrated review system

### Objective

Produce an installed, usable review system, resolve the highest-priority
integration defects, and collect product-manager feedback before final release
hardening.

### Work

- Remove unwanted upstream default applications through the image definition:
  office suites; the KDE PIM/Akonadi/MariaDB stack; KMines, KPat, and
  KMahjongg; NeoChat; Plasma/Fedora Welcome; Fedora Media Writer; Elisa;
  Dragon Player; KolourPaint; Skanpage; and QRca.
- Retain Kamoso and KDE's KRDC/KRFB remote-desktop tools.
- Present the installed review VM at a normal 1920x1080 desktop size.
- Resolve visible taskbar, dark-appearance, wallpaper, Vicinae, and terminal
  integration defects in the development VM, then promote accepted work into
  versioned package sources.
- Record new product scope discovered through the installed-system review.

### Exit criteria

- The installed review VM is usable with Vicinae, Dolphin, Ghostty, Proper
  Apps, and an installed browser.
- The product manager approves the Phase 7–12 plan.

## Phase 7 — Curation and browser

### Objective

Reduce the default image to the primary customer's actual requirements and
make Chromium the promoted browser without disrupting Fedora's installer.

### Work

- Package only the PM-approved upstream wallpapers (`Path`, `Volna`, and
  `summer_1am`) alongside Proper Blue Hour and Proper Horizon, including their
  upstream licences and attribution.
- Exclude `plasma-workspace-wallpapers` after the approved assets are owned by
  a Proper package.
- Install Chromium and make it the XDG, Plasma, and Vicinae browser default.
- Retain Firefox when the Fedora graphical installer requires it; do not
  promote it over Chromium.
- Exclude the weak AWS Python/S3 dependency stack.
- Move Podman/Skopeo/Toolbox and additional HPLIP/Gutenprint compatibility
  drivers to Proper Apps while retaining core printing.
- Record installed-size and compressed-ISO changes with the final integrated
  Phase 12 build; the PM explicitly waived an intermediate Phase 7 rebuild.

### Exit criteria

- The live and installed systems browse normally through Chromium.
- The graphical installer, Fedora updates, core printing, and hardware support
  remain intact.

## Phase 8 — Proper arrival and personalisation

### Objective

Make login, lock, wallpaper selection, and the first visible moments of the
system feel deliberately designed.

### Work

- Explicitly synchronise the default desktop, lock-screen, and PLM wallpaper.
- Replace the stock lock-screen composition through Plasma's supported
  `ShellPackage` selection. Use Plasma's fallback-package mechanism for every
  non-lock surface so Fedora's upstream shell fixes continue to land, and avoid
  whole-screen blur that destroys the artwork.
- Implement the approved restrained PLM composition with centred time and
  authentication, no avatar or submit arrow, and a lower-right icon menu for
  user, session, sleep, restart, and power actions.
- PLM 6.7.4 embeds its greeter QML and has no supported external composition
  theme. Carry one auditable, version-pinned Fedora source-package patch for the
  layout while retaining the upstream backend and all normal package ownership.
- Add a visual wallpaper gallery with previews for the curated collection.
- Keep Proper Dark as the primary appearance and an ordinary light option.
  Additional colour palettes are not a version 0.1 release blocker.

### PM arrival review

Show the login and lock alternatives, wallpaper switching, and persistence
after logout and reboot.

The PM approved the minimal lock composition and centred login direction on
2026-08-31. Source packaging, isolated greeter validation, installed login,
lock and unlock, first-character preservation, wallpaper persistence, the
pointer-operated action menu, and Switch User all pass in the Fedora 44 review
VM. The arrival checkpoint is complete.

## Phase 9 — Plasma shell surfaces

### Objective

Review every persistent and transient Plasma shell surface as one product
system, adopt the strongest maintained Plasma 6 building blocks, and refine
only the surfaces that fail Proper's visual or interaction standard without
replacing Plasma.

### Work

- Use `docs/SHELL_SURFACES.md` as the ownership, extension-point, and candidate
  record.
- Capture the taskbar and task states, tray, notifications, volume and
  brightness OSDs, network/Bluetooth/audio/power panels, clock/calendar,
  clipboard, emoji path, Polkit prompt, Alt+Tab, Overview, Desktop Grid, and
  workspace switching at 1920x1080 and 200% scaling.
- Compare the installed Fedora, Breeze, Breeze Dark, and Breeze Twilight
  baselines with a small, source- and licence-audited set of current Plasma 6
  Global Themes and Plasma Styles.
- Record the component owner, supported extension point, source, licence,
  pinned version, and update method for every retained external asset.
- Define a narrow Proper Plasma Style only where configuration and existing
  assets cannot produce the approved result. Let unowned theme elements fall
  back to Breeze.
- Keep Vicinae as the promoted launcher and use stock Plasma launchers only as
  interaction/reference baselines.
- Prefer upstream applets and supported configuration for notifications,
  networking, Bluetooth, audio, power, and clipboard. Fork or rewrite an applet
  only for a documented acceptance failure and with explicit PM approval and
  an update/rebase exit plan.
- Test pointer, keyboard, focus, reduced-motion, blur-disabled, third-party tray
  icon, notification action, authentication failure/cancellation, and
  multi-display states.
- Package accepted assets and defaults through `proper-look-and-feel` and
  `proper-defaults`; preserve existing user choices during package updates.

### PM shell-surfaces review

Compare the complete baseline and selected screenshot sets, exercise every
ordinary surface with the pointer, and approve which surfaces remain
Breeze-derived, which gain Proper theme assets, and which—if any—justify
targeted widget work.

The installed-VM baseline, contact sheets, and provisional keep/theme
recommendations are ready in `docs/evidence/phase9-shell-surfaces`. PM review
is pending. Phase 9 is not complete until the PM decides which surfaces are
sufficient, which receive Proper theme assets, and which require deeper work.

## Phase 10 — Proper Apps 2

### Objective

Turn Proper Apps into an attractive, broad, curated software directory without
preinstalling the optional applications it presents.

### Work

- Replace the list-first home screen with a responsive icon grid, Recommended,
  Installed, and All views, category filters, search, and clear install state.
- Audit the useful general-purpose application selection in the current
  Omarchy manual and map each entry to a maintained Fedora RPM, verified
  Flatpak, official vendor source, supported CLI installer, or web app.
- Exclude Omarchy shell internals and any entry without a safe Fedora path.
- Add optional container and printer-compatibility capability entries.
- Add user-created web apps with a name, URL, icon, launcher, and removal path.
- Preserve understandable progress, recovery, and advanced source/licence
  disclosure for every provider.

### PM catalogue review

Browse, search, install, launch, and remove representative entries entirely
with the pointer at 1920x1080 and 200% scaling.

## Phase 11 — Window organisation and desktop utilities

### Objective

Make side-by-side work, discovery, and useful desktop actions exceptionally
fast without making tiling or shortcut memorisation mandatory.

### Work

- Polish pointer and `Meta`+arrow halves, quadrants, maximise, and restore.
- Evaluate supported two-thirds/one-third layouts and a visible layout chooser.
- Add a reversible “Arrange workspace” action that snapshots normal windows on
  the current workspace and monitor, applies the selected layout, and restores
  the previous floating geometry on the next toggle. New windows remain
  floating; dialogs, pop-ups, fullscreen, and picture-in-picture surfaces are
  excluded. Expose it through a pointer path, Vicinae, and `Meta+Shift+T`.
- Add a searchable, pointer-accessible shortcut reference.
- Add Vicinae actions for appearance, wallpaper, night light, screenshots,
  updates, power, Bluetooth, display settings, and diagnostics.
- Surface Plasma's clipboard history and Spectacle capture through the promoted
  launcher path.
- Add region OCR only through an auditable, optional or lightweight provider.

### PM workflow review

Demonstrate the window layouts and every promoted utility with both pointer and
keyboard paths.

## Phase 12 — Final Proper Linux 0.1 candidate

### Objective

Produce and validate the exact release candidate after the approved expansion
phases.

### Work

- Confirm every Proper package is installed through the image definition rather than manual VM changes.
- Run an ISO build from a clean checkout/cache state where practical.
- Boot the live ISO, install it to a blank VM, remove installation media, and boot the installed system.
- Run the complete acceptance checklist.
- Confirm Fedora updates still operate normally.
- Confirm user customisations survive a Proper package update.
- Generate ISO checksum, bill of included Proper components, and local release notes.
- Record the installed-size and compressed-ISO effect of the Phase 7 curation
  against the preserved Phase 6 baseline.
- Document known defects honestly.

### Deliverables

- `Proper-Linux-0.1-<build>.x86_64.iso`
- checksum
- installed reference VM
- release notes and known issues
- screenshot set

### PM checkpoint 5 — Final installed system

The product manager performs or observes the full install-to-daily-use journey and either approves version 0.1 or returns a prioritised visual/interaction punch list.

## After version 0.1 approval

Only after the installed experience is approved:

- select final code/docs/art licences;
- perform formal naming and trademark review;
- establish package and ISO signing keys;
- build a small Proper package repository;
- add CI builds and release artefact retention;
- create a public product site with screenshots rather than a wall of acronyms;
- consider a deeper optional OS agent service;
- consider additional architectures or specialised images based on demonstrated demand.

## Stop conditions

Implementation should pause only when:

- a PM visual checkpoint is ready;
- a choice would materially change product direction;
- a required action needs new credentials or authority;
- an upstream/legal restriction blocks the planned distribution method; or
- continuing would risk destructive changes to BOX or unrelated user data.

Ordinary bugs, dependency adjustments, build failures, and internal code choices are not reasons to return the work prematurely.
