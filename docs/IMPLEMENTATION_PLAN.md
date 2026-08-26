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
- Add a taskbar action that toggles a retained dropdown/slide-out Ghostty session using KWin rules or a small integration helper.
- Integrate “Open terminal here” into Dolphin.
- Install and theme `btop` appropriately.
- Ensure Git and expected baseline developer utilities are present without turning the image into a large SDK bundle.

### Deliverables

- normal and dropdown Ghostty workflows
- Dolphin integration
- `btop` in the image

### Exit criteria

- Clicking the taskbar terminal affordance shows and hides the same terminal session.
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

## Phase 6 — Integrated version 0.1 image

### Objective

Produce the complete installable Proper Linux 0.1 candidate.

### Work

- Remove unwanted upstream default applications through the image definition:
  office suites; the KDE PIM/Akonadi/MariaDB stack; KMines, KPat, and
  KMahjongg; NeoChat; Plasma/Fedora Welcome; Fedora Media Writer; Elisa;
  Dragon Player; KolourPaint; Skanpage; and QRca.
- Retain Kamoso and KDE's KRDC/KRFB remote-desktop tools.
- **PM task:** curate Fedora/KDE's upstream wallpapers and identify the small
  subset to retain. Promote that approved selection into versioned image or
  package content; do not ship a manually edited home directory.
- Confirm every Proper package is installed through the image definition rather than manual VM changes.
- Run an ISO build from a clean checkout/cache state where practical.
- Boot the live ISO, install it to a blank VM, remove installation media, and boot the installed system.
- Run the complete acceptance checklist.
- Confirm Fedora updates still operate normally.
- Confirm user customisations survive a Proper package update.
- Generate ISO checksum, bill of included Proper components, and local release notes.
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
