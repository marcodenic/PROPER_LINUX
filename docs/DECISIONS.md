# Proper Linux decision log

This file records product and architecture choices so future work does not reopen settled questions without new evidence.

Status values:

- **Accepted:** proceed unless evidence materially changes.
- **Provisional:** implement and decide at a named PM checkpoint.
- **Deferred:** deliberately outside the current release.

## D001 — Build on mutable Fedora KDE

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Use the normal package-based Fedora KDE Plasma Desktop rather than Arch, Omarchy, or Fedora Atomic.
- **Reason:** Fedora already supplies the desired conventional desktop, hardware foundation, installer, updater, and mutable `dnf` workflow. Proper Linux focuses on the visible product experience.

## D002 — Preserve Fedora plumbing

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Keep Fedora's kernel, drivers, networking, security, installer, updater, and package management unless a concrete UX requirement is blocked.
- **Reason:** The product problem is UX, not the operating-system foundation.

## D003 — Use KIWI for the live image

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Derive the package-based live image from Fedora KDE's current KIWI description.
- **Reason:** Fedora now uses KIWI for package-based live media. Older kickstart/livecd and Arch `archiso` guidance is not the current base path.

## D004 — Keep Plasma and KWin

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Customise KDE Plasma 6 and KWin through supported packages, themes, layouts, widgets, scripts, and defaults.
- **Reason:** Plasma already provides mature floating-window, pointer, settings, system-tray, notification, and application behaviour.

## D005 — Mouse and keyboard are both normal

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Every ordinary desktop action remains usable with a mouse. Strong shortcuts are shipped for speed but are not prerequisites.
- **Reason:** Proper Linux takes Omarchy's curation without its keyboard-only operating model.

## D006 — Floating default with snapping and quick tiling

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Windows float by default. Mouse edge/corner snapping and Windows-style `Meta`+arrow quick tiling are always available. Useful Omarchy bindings are added where they do not conflict.
- **Reason:** Floating and tiling are complementary behaviours, not mutually exclusive editions.

## D007 — Bottom floating taskbar

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Use a tasteful translucent floating bottom taskbar, visible by default with user-controlled hide behaviour. Do not add a top bar.
- **Reason:** It is familiar, space-efficient, pointer-friendly, and matches the intended visual direction.

## D008 — Vicinae only

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Vicinae is the single promoted application launcher and Raycast-style command/search surface. The Proper taskbar button and `Meta+Space` both open it. KRunner remains an unobtrusive fallback.
- **Reason:** AppGrid does not meet the product manager's visual standard. One well-configured Vicinae surface is more coherent than shipping an unattractive second launcher.

## D009 — Plasma Login Manager

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Use Fedora KDE 44's Plasma Login Manager rather than adding SDDM.
- **Reason:** PLM is the current Fedora KDE path, shares the Plasma/KWin stack, supports appearance and display-setting synchronisation, and avoids known SDDM configuration mismatch.

## D010 — Login consistency before custom layout

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Make wallpaper, theme, and monitor layout correct using PLM's supported surfaces. Do not fork the login layout merely to make it different.
- **Reason:** The painful defects are wrong orientation and inconsistent wallpaper, not lack of a novel account selector.

## D011 — Ghostty and btop

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Ship Ghostty as the default terminal and include `btop`. Prototype a retained dropdown/slide-out Ghostty action from the taskbar.
- **Reason:** The terminal is central to the audience and should feel like a deliberate product surface.

## D012 — Lean image, curated optional software

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Keep the default installation lean. Put likely software one click away through Proper Apps. Do not install an office suite by default.
- **Reason:** The primary customer's real application set is small; preinstallation is not the same as ease of access.

## D013 — Proper Apps is not a package manager

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Maintain a curated catalogue and delegate installation to Flatpak, Fedora, PackageKit/Discover, or official vendor sources.
- **Reason:** Users need one product-level choice without duplicating mature installation and update mechanisms.

## D014 — Agent clients first, OS agent later

- **Status:** Accepted for 0.1; deeper integration deferred
- **Date:** 2026-08-24
- **Decision:** Make Codex, Claude Code, OpenCode, and similar clients easy to install and launch. Do not add a privileged background agent service.
- **Reason:** Deep OS agency requires a separate permissions and trust design. It is not needed to prove the desktop.

## D015 — Upstream installer and updater

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Retain Fedora's graphical installer and update mechanisms with only necessary branding/default integration.
- **Reason:** Replacing functioning infrastructure does not improve the target experience.

## D016 — VM, not Docker, is the acceptance environment

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Containers may build the image. QEMU/KVM boots and installs it for visual acceptance.
- **Reason:** A container shares its host kernel and cannot faithfully validate UEFI, the installer, KWin/Wayland, login manager, or a complete graphical boot.

## D017 — Hardware scope follows Fedora

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Target Fedora-supported x86-64 computers without separate lightweight, workstation, or server editions in 0.1.
- **Reason:** Proper Linux should avoid needless overhead but should not invent a narrower compatibility promise or a broader certification claim.

## D018 — Entirely free distribution

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Public ISO and source downloads have no account requirement, paid edition, delay, or feature gate.
- **Reason:** Charging to remove artificial download friction conflicts with the product's identity.

## D019 — Working name Proper Linux

- **Status:** Provisional until formal name/trademark review
- **Date:** 2026-08-24
- **Decision:** Use Proper Linux as the working name with a simple ASCII-influenced identity.
- **Reason:** It clearly expresses the product attitude. A preliminary web/GitHub search found no prominent Linux distribution with the exact name, but that is not legal clearance.

## D020 — Proposed project licences

- **Status:** Provisional until PM approval and component audit
- **Date:** 2026-08-24
- **Decision:** Prefer GPL-3.0-or-later for Proper Linux code and packaging, and CC BY-SA 4.0 or CC0 for original documentation/artwork as appropriate.
- **Reason:** The project must remain genuinely open and redistributable. A final choice must account for copied upstream code, icon licences, fonts, and artwork sources before release.

## D021 — PM checkpoints govern visual approval

- **Status:** Accepted
- **Date:** 2026-08-24
- **Decision:** Use five reviews: login, desktop/taskbar, launchers/windows, software directory, and final installed system.
- **Reason:** The PM's taste is the central product input. Infrastructure work continues autonomously between those reviews.

## D022 — Dolphin is the file-manager baseline

- **Status:** Provisional through PM checkpoint 2
- **Date:** 2026-08-24
- **Decision:** Begin with a simplified and styled Dolphin configuration presented as “Files.” Compare it directly with current Nautilus and COSMIC Files in the Proper Plasma VM before locking the default.
- **Reason:** Dolphin has the strongest Plasma integration and mature file operations, but stock Dolphin's visual density may not meet the product standard. Nautilus is cleaner but deliberately less capable and visually tied to GNOME; COSMIC Files is attractive and Fedora-packaged but brings its own toolkit/theme and less mature integration. The installed comparison should decide.

## D023 — Validate recent mainstream x86-64 hardware first

- **Status:** Accepted; refines D017
- **Date:** 2026-08-25
- **Decision:** Retain Fedora's general x86-64 compatibility, but concentrate Proper Linux product validation on mainstream laptops and desktops from roughly the previous four years and on current Fedora-supported hardware. Do not make old-hardware rejuvenation, Intel Mac enablement or Apple Silicon support a version 0.1 requirement.
- **Reason:** Proper Linux should not add needless overhead, but its visual and interaction goals should not be constrained by a promise to optimise for obsolete machines. Apple Silicon requires the separate Fedora Asahi platform stack rather than the version 0.1 x86-64 image.

## D024 — Use three UI feedback loops

- **Status:** Accepted
- **Date:** 2026-08-25
- **Decision:** Prototype visual work in a dedicated development VM session, promote approved work into the owning RPM, and rebuild the complete ISO for integration and checkpoint validation.
- **Reason:** Rebuilding an operating-system image for every styling adjustment makes design iteration needlessly slow, while leaving changes only in a prepared user account makes the product unreproducible.

## D025 — Dolphin is the default Files application

- **Status:** Accepted at PM checkpoint 2
- **Date:** 2026-08-25
- **Decision:** Ship Dolphin as the default file manager, presented in the launcher as “Files,” with Proper's restrained defaults.
- **Reason:** The like-for-like checkpoint comparison confirmed Dolphin's mature Plasma integration and complete ordinary file operations outweigh the cleaner but less integrated alternatives.

## D026 — Pin Vicinae 0.24.0 in Proper Linux

- **Status:** Accepted for Phase 3
- **Date:** 2026-08-25
- **Decision:** Package the upstream `vicinaehq/vicinae` v0.24.0 x86_64 Linux tarball as `proper-launchers`.
- **Source:** https://github.com/vicinaehq/vicinae/releases/tag/v0.24.0 (official release asset `vicinae-linux-x86_64-v0.24.0.tar.gz`).
- **Licence:** GPL-3.0-or-later for Vicinae; Proper integration files remain under the project's applicable package licence.
- **Update method:** Manually audit the upstream release page, update the pinned Source0 tag and checksum in the package audit, rebuild the RPM, verify it in the development VM, then include it in the next ISO integration build.

## D027 — Phase 4/5 implementation sources

- **Status:** Implemented pending PM checkpoint 4
- **Date:** 2026-08-25
- **Decision:** Use the official Ghostty 1.2.3 source tarball, built with the pinned official Zig 0.14.1 binary toolchain, and MIT licence. Use a small versioned Proper Apps catalogue that delegates to Fedora, Flatpak, and official vendor installation paths; GitHub Desktop is explicitly community-maintained.
- **Reason:** Fedora 44's configured repositories do not provide Ghostty, while upstream provides a maintained source release and packaging guidance. Proper Apps must remain a catalogue and not become a second package manager.
- **Update method:** Audit the upstream release/source checksum and Fedora build dependencies for each Ghostty update; validate catalogue provider metadata and installation flow in the disposable VM before changing the manifest.

## D028 — PM checkpoint 3 approval recorded

- **Status:** Approved by PM handoff
- **Date:** 2026-08-25
- **Decision:** Treat Phase 3 launcher/window behaviour and the verified ISO `b6e4bb0098d77ac29c79cc28352bfb1bb2328cb1b5615dd5f7b21cdff83c82dc` as approved baseline; do not redo Phase 3 beyond focused regression checks.

## D029 — Build Vicinae from source against Fedora Qt

- **Status:** Implemented pending PM checkpoint 4
- **Date:** 2026-08-26
- **Decision:** Replace the prebuilt Vicinae v0.24.0 binary and private-Qt relabeling workaround with the official Vicinae source archive at commit `01cd7cb4936d9cb14272091623da85e7c880f0dc`, built against Fedora 44's Qt 6.11.1. The archive SHA-256 is `ee4e80d6e69193820b294a43a008794d8761cda9914256c32aed3be091f5c0e3`.
- **Reason:** The immutable final3 baseline reproduced a launcher exit when the search field was clicked or first typed into. A source build removes the incompatible private-Qt ABI shim; the exact source-built RPM and fresh ISO pass the focused interaction regression.
- **Additional fetched build dependencies:** Upstream CMake FetchContent retrieves Glaze v7.2.0 at commit `b518eec7a22e56ffa238b072c07f47efa7cea97f` (MIT, <https://github.com/stephenberry/glaze>) and QtKeychain v0.14.0 at commit `e63da2868465db18eb35a312b2635c26fdc46923` (BSD-3-Clause, <https://github.com/frankosterfeld/qtkeychain>); these are build-only and must be re-audited and checksum-recorded on each Vicinae source update.
- **Update method:** Audit the official Vicinae source commit, archive checksum, upstream dependency tags/commits and licences; rebuild in the pinned Fedora builder, install the RPM in a disposable guest, then rebuild and boot the exact ISO before promotion.

## D030 — PM checkpoint 4 approval and Phase 6 continuation

- **Status:** Accepted
- **Date:** 2026-08-26
- **Decision:** Treat PM checkpoint 4 and all preceding checkpoints as approved
  for Phase 6 continuation. Preserve the source-built Vicinae ISO and its
  evidence as the immutable baseline while producing a new integrated candidate.
- **Reason:** The product manager explicitly approved the Phase 4/5 handoff;
  remaining work is final-image curation, installation, persistence, display
  compatibility, and the complete installed checkpoint-5 journey.

## D031 — Proper Blue Hour is the interim default wallpaper

- **Status:** Accepted for the next Phase 6 candidate
- **Date:** 2026-08-30
- **Decision:** Use the product-manager-selected `Proper Blue Hour` mountain,
  lake, and city artwork as the default live, installed, lock-screen, and Plasma
  Login Manager wallpaper. Keep `Proper Horizon` installed as an alternate.
- **Reason:** The blue-hour composition provides the requested calm,
  awe-inspiring arrival while supporting the planned dark translucent desktop
  chrome and clear login typography.

## D032 — Proper Dark is the default desktop appearance

- **Status:** Accepted for the next Phase 6 candidate
- **Date:** 2026-08-30
- **Decision:** Default new and live sessions to the `Proper Dark` global
  look-and-feel, Breeze Dark colours and icons, Breeze Dark's adaptive
  translucent Plasma shell, and KWin background blur. Keep light appearance
  available as an ordinary user choice.
- **Reason:** The product manager rejected the white fallback panel and asked
  for a dark-by-default system with a dark translucent floating panel and real
  background blur. Reusing Plasma's supported adaptive theme surfaces avoids a
  fragile fork while delivering that appearance.

## D033 — All Vicinae launch surfaces use Proper's readiness-aware opener

- **Status:** Accepted for the next Phase 6 candidate
- **Date:** 2026-08-30
- **Decision:** Replace Vicinae's upstream application entry after installation
  so the taskbar, application menu, and shortcut all run `proper-launcher`.
  The wrapper starts or recovers the user service, waits for IPC readiness,
  sends an idempotent `open`, and reports a genuine failure visibly.
- **Reason:** Vicinae's upstream desktop entry starts `server --replace` without
  opening its window, while an immediate `toggle` races service startup. Both
  paths made a normal pointer click appear broken even when the binary itself
  was healthy.

## D034 — Remove the dropdown-terminal prototype from version 0.1

- **Status:** Accepted; supersedes the prototype portion of D011
- **Date:** 2026-08-30
- **Decision:** Keep Ghostty as the default terminal and keep `btop`, but replace
  the retained dropdown prototype with an ordinary pinned Ghostty launcher.
- **Reason:** The product manager does not need the feature, and the prototype's
  normal-window presentation, duplicate task identity, and KWin integration add
  complexity without improving the current desktop.

## D035 — Extend version 0.1 through focused expansion phases

- **Status:** Accepted
- **Date:** 2026-08-31
- **Decision:** Treat Phase 6 as the installed review-system milestone. Add
  dedicated curation/browser, arrival/personalisation, Proper Apps 2, and
  window/utility phases before producing the then-numbered Phase 11 release
  candidate. D044 subsequently inserts the shell-surfaces review and renumbers
  that release candidate as Phase 12.
- **Reason:** Installed-system review proved the core desktop while identifying
  material product work that should be designed and reviewed independently,
  rather than hidden inside a final ISO punch list.

## D036 — Chromium is the promoted default browser

- **Status:** Accepted
- **Date:** 2026-08-31
- **Decision:** Install and promote Fedora Chromium as Proper's default browser.
  Firefox may remain installed when required by Fedora's graphical live
  installer or as an unpromoted fallback.
- **Reason:** Chromium matches the primary customer's preference and supports
  the planned web-app workflow. Retaining Firefox is acceptable when removing
  it would complicate or weaken the upstream installer path.

## D037 — Curate wallpapers and move optional stacks out of the base image

- **Status:** Accepted
- **Date:** 2026-08-31
- **Decision:** Retain Path, Volna, summer_1am, Proper Horizon, and Proper Blue
  Hour. Exclude the complete upstream wallpaper bundle after packaging the
  selected upstream assets with provenance. Exclude the AWS Python/S3 stack,
  and offer Podman/Skopeo/Toolbox and additional HPLIP/Gutenprint compatibility
  through Proper Apps instead of the default image.
- **Reason:** Proper Linux is curated around the primary customer's actual use.
  Optional software remains easy to install without consuming every default
  installation.

## D038 — Login and lock layouts are now explicit product surfaces

- **Status:** Accepted; refines D010
- **Date:** 2026-08-31
- **Decision:** Create Proper lock and Plasma Login Manager compositions using
  supported theme/configuration mechanisms. Keep the selected wallpaper
  recognisable, avoid destructive whole-screen blur, and improve the hierarchy
  of time, authentication, account, session, and power controls.
- **Reason:** The installed review exposed concrete visual problems in both
  layouts. This is no longer customisation merely for novelty.

## D039 — Proper Apps 2 is a broad optional catalogue

- **Status:** Accepted
- **Date:** 2026-08-31
- **Decision:** Redesign Proper Apps around an icon-grid catalogue and expand it
  to the useful general-purpose application selection inspired by Omarchy.
  Optional catalogue entries are not preinstalled, and every entry requires a
  maintained, auditable Fedora-appropriate provider and removal path.
- **Reason:** A rich, approachable catalogue and a lean installed image are
  complementary rather than conflicting goals.

## D040 — Use a minimal two-state lock screen through Plasma ShellPackage

- **Status:** Accepted at PM arrival review
- **Date:** 2026-08-31
- **Decision:** The idle lock screen shows only the current wallpaper and a
  restrained clock/date. The first typed character reveals a compact,
  unlabelled translucent password field containing that character. Do not show
  an avatar, account name, placeholder, permanent authentication card, or
  submit arrow. A lower-right three-dot button reveals icon actions for sleep,
  switching user, and power. Package the implementation as
  `com.properlinux.desktop`, selected with Plasma's supported `ShellPackage`
  setting. Use `org.kde.plasma.desktop` as Plasma's fallback package for all
  non-lock shell content.
- **Reason:** The product manager rejected form-heavy lock-screen compositions.
  This preserves the artwork at rest, reveals authentication only when needed,
  retains pointer access to system actions, and avoids replacing Fedora-owned
  QML or maintaining a full Plasma shell fork.

## D041 — Measure curation at final integration, not between Phases 7 and 8

- **Status:** Accepted
- **Date:** 2026-08-31
- **Decision:** Do not rebuild the ISO solely to measure Phase 7. Proceed
  directly into Phase 8 and record the installed-size and compressed-ISO delta
  during the clean final release-candidate build (now Phase 12 under D044).
- **Reason:** The image definition and package boundaries can be verified now;
  an intermediate full rebuild would delay the approved arrival work without
  replacing the final integration measurement.

## D042 — Use a bounded Proper wallpaper gallery and explicit arrival sync

- **Status:** Accepted at PM arrival review
- **Date:** 2026-08-31
- **Decision:** Ship `proper-appearance` as the visual gallery for the five
  curated wallpapers. A normal selection updates the desktop and lock screen;
  “Use everywhere” additionally writes a PLM configuration fragment through an
  authenticated helper that accepts only packaged wallpaper IDs.
- **Reason:** Plasma's complete wallpaper picker includes assets owned by core
  desktop packages and does not make login synchronisation obvious. A small
  product-level gallery exposes only the approved collection while continuing
  to use Plasma's wallpaper API and PLM's supported configuration cascade.

## D043 — Rebuild Fedora's PLM package for the approved centred composition

- **Status:** Accepted at PM arrival review
- **Date:** 2026-08-31
- **Decision:** Build Fedora 44's exact `plasma-login-manager` 6.7.4 source RPM
  with a narrow downstream patch that embeds and selects `ProperMain.qml`. The
  composition uses centred time, date, identity, and authentication; omits the
  avatar, placeholder, permanent card, and submit arrow; and puts user,
  session, sleep, restart, and power actions behind a lower-right icon menu.
  Keep PLM's existing models, authenticator, session management, state storage,
  and Fedora package ownership. Verify the source checksum and rebase the patch
  deliberately on every PLM update.
- **Reason:** PLM 6.7.4 compiles its greeter QML into the executable and offers
  wallpaper plugins but no SDDM-style external composition theme. The accepted
  design therefore cannot be delivered by a supported theme package alone.
  A small source-package patch is more auditable and updateable than replacing
  Fedora-owned runtime files or forking the login manager.

## D044 — Review Plasma shell surfaces before expanding the application catalogue

- **Status:** Accepted for implementation
- **Date:** 2026-08-31
- **Decision:** Add a dedicated Phase 9 review of the panel, task states, tray,
  notifications, OSDs, connectivity/audio/power panels, clipboard and emoji
  paths, authentication prompts, and KWin workspace controls. Prefer supported
  Global Theme, Plasma Style, colour, icon, layout, widget, and KWin extension
  points. Create a narrow Proper Plasma Style where approved and fall back to
  Breeze for unowned assets. Keep the functional applets upstream unless a
  documented acceptance failure and explicit PM decision justify maintained
  widget or source code. Renumber the catalogue, workflow, and release-candidate
  work as Phases 10, 11, and 12.
- **Reason:** Proper currently gives the lock screen a custom composition but
  leaves most other shell surfaces Breeze-derived. A systematic visual and
  interaction review can improve product coherence without adopting Omarchy's
  much larger shell-ownership and maintenance boundary. This extends D035 and
  moves its final release-candidate checkpoint from Phase 11 to Phase 12.

## D045 — Seed and migrate the Proper panel without owning panel behaviour

- **Status:** Accepted for implementation
- **Date:** 2026-08-31
- **Decision:** Keep Plasma's upstream panel, Icon Tasks, System Tray, Show
  Desktop, and Digital Clock components. Seed a centred, fit-content, floating,
  translucent 56-pixel panel for new accounts and provide a one-time
  ShellPackage update that creates the same curated panel only when the
  ShellPackage layout store has no panel. Never recreate a panel after the
  update has run, so a later user decision to remove it remains respected.
- **Reason:** Selecting a custom Plasma ShellPackage also selects a separate
  applet-layout store. Visual fallback to the upstream shell does not populate
  that store, which left an existing review account with no panel. Explicitly
  seeding the store and narrowly migrating only the empty state fixes arrival
  while preserving upstream interaction code and later user customisation.

## D046 — Keep the upstream Plasma component boundary

- **Status:** Accepted at PM shell-surfaces review
- **Date:** 2026-08-31
- **Decision:** Keep the dark translucent floating Proper panel and its task
  identity defaults. Retain Plasma's upstream tray, notifications, OSDs,
  network, Bluetooth, audio, power, clipboard, authentication, Alt+Tab,
  Overview, and Desktop Grid implementations, then apply only the Proper theme
  and configuration changes approved at the visual checkpoint.
- **Reason:** Installed-VM review found no functional acceptance failure that
  justifies owning those applets. The PM approved resolving the visual
  opportunities through a narrow Proper Plasma Style rather than replacing the
  applets.

## D047 — Add reversible workspace arrangement without mandatory auto-tiling

- **Status:** Accepted for Phase 11 implementation
- **Date:** 2026-08-31
- **Decision:** Keep KWin floating by default, edge snapping, `Meta`+arrow
  quick tiling, and the native `Meta+T` tile editor. Add a Proper “Arrange
  workspace” action that applies a chosen layout to ordinary windows on the
  current workspace and monitor, then restores their captured floating
  geometry when toggled. New windows continue to open floating.
- **Reason:** This gives the PM the requested instant tiled/floating workflow
  without continuous auto-reflow, mandatory tiling, or a replacement window
  manager. Pointer, Vicinae, and keyboard paths remain peers.

## D048 — Keep region OCR local, on demand, and unprivileged

- **Status:** Accepted for Phase 11 implementation
- **Date:** 2026-08-31
- **Decision:** Implement “Copy text from screen” as a direct user-session
  action: Spectacle captures a selected region, Fedora's Tesseract English data
  recognises it locally, and `wl-clipboard` copies the result. Remove the
  temporary capture on exit. Do not add a resident OCR service, cloud provider,
  or privileged AI daemon.
- **Reason:** The workflow is useful and auditable while preserving the version
  0.1 security boundary. Its packages come from Fedora's signed repositories,
  update with the normal mutable system, and can be replaced later without
  changing the launcher contract.

## D049 — Approve the soft shelf, calmer popups, and semantic pointer launcher

- **Status:** Accepted at PM shell-surfaces review
- **Date:** 2026-08-31
- **Decision:** Use bar variant D as one centred, fit-content upstream Plasma
  panel with Proper's soft shelf asset. Apply a narrow Proper Plasma Style to
  panel, dialog, heading, tooltip, and translucent/OSD backgrounds, reserving
  desaturated blue for selection, focus, and progress. Present the first panel
  slot as a quiet **Applications & Search** button with a semantic search icon;
  clicking it opens Vicinae. Enable and pin Vicinae's built-in **Browse Apps**
  view so a pointer user can reach an alphabetical all-apps list without typing.
  Retain variant B only as a future visual reference.
- **Reason:** The PM approved the calmer Vicinae-adjacent surfaces and preferred
  D for version 0.1. The semantic button removes the poor upstream Vicinae brand
  mark while preserving an obvious pointer path. Vicinae indexes installed
  desktop applications and settings entries and supplies system power commands,
  so a second promoted application menu is unnecessary. KRunner remains an
  unobtrusive fallback.

## D050 — Ship recognisable, checked product artwork in Proper Apps

- **Status:** Implemented pending Phase 10 PM catalogue review
- **Date:** 2026-08-31
- **Decision:** Show named applications with their current AppStream,
  upstream-project, or official publisher artwork. Pin the shipped assets and
  record their source, rights note, transformation, retrieval date, and
  SHA-256 in `apps/icon-sources.json`. Reserve Plasma theme glyphs for generic
  system capabilities such as printer compatibility; do not use generated
  letter tiles as the normal product identity.
- **Reason:** Application recognition depends on familiar visual identity, and
  host icon themes cannot be assumed to contain optional software. A checked
  local asset set keeps the catalogue coherent and reproducible while the
  provenance ledger makes upstream updates and trademark review explicit.

## D051 — Use hosted RPM updates and release-snapshot ISOs

- **Status:** Accepted for public distribution
- **Date:** 2026-08-31
- **Decision:** Publish Proper-owned RPMs for each supported Fedora release
  through Fedora Copr and enable that hosted repository through
  `proper-release`. Keep Fedora packages on Fedora's normal repositories and
  let DNF/PackageKit/Discover update both sets. Rebuild the Proper ISO for
  tested release snapshots, installer or image-composition changes, and Fedora
  major-version rebases—not for every Proper package update.
- **Reason:** Existing installations need a signed RPM repository, not a new
  installer image. Copr supplies hosted builds and repository metadata without
  requiring Proper Linux to operate a package server, while the ISO remains the
  reproducible path for new installations.

## D052 — Keep source-of-truth documents and bound binary evidence

- **Status:** Accepted
- **Date:** 2026-08-31
- **Decision:** Keep product, architecture, plan, decision, source-audit, and
  acceptance documents in Git alongside package sources, tests, shipped art,
  application icons, licences, and provenance. Keep ISOs, RPMs, VM disks,
  downloaded upstream archives, raw captures, videos, caches, and logs outside
  Git. During development, retain only compressed, curated checkpoint images
  that are needed to record a PM decision; move complete public-release media
  sets to release or website storage.
- **Reason:** The documents make the product and build reproducible, while raw
  review media and downloaded build inputs create permanent repository bloat
  without becoming configuration input. A later one-time history rewrite may
  remove retired binary evidence before public launch, but requires explicit
  PM approval because it rewrites published commit identities.

## D053 — Mask every rounded shell surface and suppress square fallbacks

- **Status:** Accepted after installed-VM defect review
- **Date:** 2026-08-31
- **Decision:** Give the rounded Proper shelf, tooltips, popups, notifications,
  and OSD containers depth through translucency, background blur, restrained
  frames, and spatial separation. Define neutral `shadow-*` slices to suppress
  Plasma's Breeze fallback, but do not ship visible shadow slices in
  Proper-owned shell assets unless a future implementation matches every
  surface radius and has installed-render regression tests. Validate this rule
  before every RPM build. Require `hint-compose-over-border` plus a complete
  rounded `mask-*` frame so Plasma clips its translucent contrast and blur pass,
  and bump the Plasma Style metadata version whenever cached assets change.
- **Reason:** The first Proper Plasma Style described shadows as square
  10-pixel nine-slices and did not ask Plasma to compose the translucent centre
  through its rounded mask. Plasma therefore exposed rectangular shadow and
  contrast tiles around both the taskbar and its tooltips.

## D054 — Use Fedora's native Plasma Setup for installed first boot

- **Status:** Accepted after Phase 12 first-boot defect review
- **Date:** 2026-08-31
- **Decision:** Let Fedora 44's `plasma-setup` own the installed first-boot
  language, keyboard, appearance, and administrator-account flow. Explicitly
  exclude every legacy `initial-setup` package from the Proper image and fail
  the ISO build if legacy Initial Setup returns or Plasma Setup is absent.
- **Reason:** Enabling both systems made legacy Initial Setup take `tty7` while
  Plasma Login Manager configured its supported `plasma-setup` autologin.
  Initial Setup then failed to acquire the VM's DRM device and left a black
  first boot. Removing that redundant package restored Fedora's maintained
  Plasma-native setup flow through the administrator-account page.

## D055 — Refine the shelf without replacing Plasma behaviour

- **Status:** Accepted at PM taskbar review; radius and tooltip details superseded by D057
- **Date:** 2026-08-31
- **Decision:** Keep the approved Proper Horizon shelf, its 18-pixel corner
  geometry, and Plasma's upstream Icon Tasks, System Tray, Show Desktop, and
  Digital Clock. Soften the shelf fill and edge so the frame reads as depth,
  not a white outline; preserve the complete rounded masks and neutral shadow
  slices from D053. Replace the promoted Vicinae search glyph with a larger
  quiet white dot and retain **Applications & Search** as its accessible name
  and tooltip. Add perceptual space after that launcher, use a month-and-day
  clock date without the year, add four pixels of space at the clock end, and
  retain Plasma's native active line and running-dot task states. Do not add a
  moving hover lens.
- **Reason:** The PM approved the refined preview for implementation and asked
  to judge further adjustments in the real desktop. These changes establish a
  distinctive taskbar without custom applet or compositor code and therefore
  keep the interaction and stability boundary established by D046.

## D056 — PM review VMs use a scalable local window

- **Status:** Accepted after review-presentation regression
- **Date:** 2026-08-31
- **Decision:** Present every product-manager-facing VM through QEMU's local
  GTK backend in a normal resizable window, with one 1920x1080 output at 100%
  scaling and zoom-to-fit enabled. Maximising the window must make the guest
  fill the available client area; do not force full screen. Keep VNC and
  additional virtual GPUs available only for unattended automation and focused
  display-compatibility checks; they must not replace the visible PM review
  surface.
- **Reason:** A two-output VNC compatibility run was left as the visible VM.
  Although its guest framebuffer remained 1920x1080, the remote presentation
  appeared as a tiny viewer surface and regressed the explicitly requested
  large review window. Separating presentation from automation prevents a
  correct guest resolution from masking an unusable host window.

## D057 — Remove hover-triggered shell tooltips and tighten the shelf radius

- **Status:** Accepted at PM taskbar review
- **Date:** 2026-08-31
- **Decision:** Disable Plasma's informational tooltips on pointer hover by
  setting the supported global tooltip delay to zero. Keep applet and action
  names in their upstream accessibility metadata, retain click-to-open panels,
  and leave the Workspace Behaviour setting available for users who want to
  re-enable hover tooltips. Reduce the Proper shelf corner radius from 18 to
  16 pixels while preserving the rounded compositor mask and upstream panel
  behaviour.
- **Reason:** Plasma 6.7.4 uses one shared tooltip window. After its initial
  delay, moving between adjacent panel targets replaces the contents
  immediately, making tooltips feel as if they appear on every hover; large
  clock content also looks detached when constrained beside the edge of a
  fit-content panel. The PM rejected hover-only explanations and requested a
  slightly tighter taskbar shape.

## D058 — Brand the QEMU review firmware and keep hardware firmware out of scope

- **Status:** Accepted after Phase 12 boot-path review
- **Date:** 2026-08-31
- **Decision:** Build the PM review VM's OVMF firmware from Fedora 44's exact
  pinned `edk2-20260508-8.fc44` source RPM and patch set, replacing only the
  built-in TianoCore bitmap with Proper's canonical grid wordmark and
  suppressing successful boot-option path chatter while retaining failure
  diagnostics. Make that artifact the default in `scripts/run-vm`; raw host
  OVMF remains an explicit diagnostics profile. Continue to use Fedora's
  signed shim and EFI directory underneath. Physical installations retain the
  computer manufacturer's firmware presentation because an operating-system
  image cannot and should not rewrite motherboard firmware.
- **Source:** Fedora `edk2-20260508-8.fc44.src.rpm`, SHA-256
  `2dc18705f149274cccb0ecd5a184bb9602e4fde57e0f448b9af674502117b5a4`,
  upstream commit `b03a21a63e3b` plus Fedora's packaged patches.
- **Licence:** The source RPM declares Apache-2.0 and its listed BSD, GPL, ISC,
  MIT, patent, and public-domain component terms. Proper's original wordmark
  remains under the project's artwork licence.
- **Update method:** When Fedora's `edk2-ovmf` changes, download and checksum
  the new source RPM, review its patch set and licence metadata, update the
  lock and builder base deliberately, rebuild the firmware, then recapture the
  UEFI-to-Plymouth sequence before promotion.
- **Reason:** TianoCore and successful `/EFI/fedora/...` status text are useful
  implementation diagnostics but visibly break Proper's reviewed arrival.
  Rebuilding the exact distro source preserves the upstream firmware boundary
  while making the controlled VM presentation coherent.

## D059 — Use selective translucency and a small preview-first appearance control

- **Status:** Accepted for implementation
- **Date:** 2026-08-31
- **Decision:** Update the D027 source pin to signed Ghostty 1.3.1 and Zig
  0.15.2, carrying the separately recorded upstream
  `ext-background-effect-v1` backport until it lands in a pinned release. Give
  Ghostty a restrained 92% background opacity with opaque cell backgrounds and
  compositor blur. Keep normal content windows opaque.
  Extend `proper-appearance` from D042 with live previews for Blue Hour,
  Horizon Light, and Midnight plus Compact, Standard, and Large text presets
  coordinated across KDE, GTK, and new Ghostty windows. Continue to apply
  styles through Plasma's supported Global Theme and wallpaper tools.
- **Reason:** Omarchy's useful lesson is selective depth and decisive curation,
  not blanket transparency. Terminal and shell glass can expose enough
  wallpaper to establish place while opaque application content preserves
  contrast. Three coherent looks and three text choices provide useful
  personalisation without recreating the complete system-settings surface.

## D060 — Make the default coding agent explicit and safely recoverable

- **Status:** Accepted for implementation
- **Date:** 2026-08-31
- **Decision:** Expose one generic Coding Agent action through the application
  menu, Dolphin, and Vicinae. On first use, ask the user to choose Codex, Claude
  Code, or OpenCode; detect manually installed commands and offer the audited
  Proper Apps installer otherwise. Save the fixed agent ID only after the
  executable exists or installation succeeds. Launch the saved client in an
  ordinary Ghostty window rooted at the requested folder. If it later goes
  missing, offer reinstall, another selection, or cancel and never infer a
  fallback.
- **Reason:** A stable generic action is convenient only if its target remains
  legible and user-controlled. The explicit bounded choice avoids surprising
  launches, works with existing manual installs, and adds no privileged daemon,
  credential broker, or background process.

## D061 — Make the Phase 12 review image source-fresh and visibly dark

- **Status:** Accepted at Phase 12 integration review
- **Date:** 2026-08-31
- **Decision:** Package the canonical full Proper palette as the `Proper`
  application colour scheme instead of the obsolete light placeholder. Refine
  D059's terminal opacity from 92 to 88 percent while retaining opaque cell
  backgrounds and compositor blur. Inhibit idle locking and display sleep only
  while the live welcome choice is open. Remove the remaining visible Fedora
  attribution from the welcome footer, keep the choice usable at the 640x480
  firmware fallback, and select the advertised 1920x1080 mode before showing
  it in the QEMU review session. Rebuild the complete Proper RPM
  repository for every product ISO composition; repository existence is never
  proof that its payloads match the current source tree.
- **Reason:** The first Phase 12 candidate exposed light application chrome,
  visually negligible terminal translucency, a welcome screen that could lock
  behind a stale framebuffer, and a final Ghostty source edit newer than its
  RPM. These were source-to-image integration failures, not acceptable visual
  variants. The PM rejected that candidate and requested a genuinely current
  image for review.

## D062 — Complete the approved shelf states and restore pointer-first locking

- **Status:** Accepted at Phase 12 shell review
- **Date:** 2026-08-31
- **Decision:** Implement D055's approved task language in Proper's Plasma
  Style instead of inheriting Breeze's filled blue task frames: a focused
  application uses a short cool underline, a running inactive application uses
  a quiet dot, and hover adds no circle or filled tile. Restore equal shelf end
  margins, superseding D055's extra four pixels after the clock. Preserve the
  quiet clock-only lock state, but make a blank-screen pointer click reveal and
  focus authentication controls, with a bounded return to the quiet state.
  Replace the inherited distro session-start splash with the canonical Proper
  icon. Restore the welcome block's approved width and a safe headline line
  box so its text cannot wrap into clipped lines at the review scale.
- **Reason:** The approved shelf preview already specified line and dot states,
  but no Proper `tasks.svg` was promoted, so Plasma exposed Breeze's blue
  backgrounds with geometry that did not match the Proper shelf. The custom
  lock screen also omitted upstream's pointer reveal path, leaving an empty
  password field permanently hidden after the clock view appeared. The PM
  rejected both regressions and reversed the earlier asymmetric clock padding.

## D063 — Complete the task-state language and materialize the dark application palette

- **Status:** Accepted at Phase 12 shell review
- **Date:** 2026-08-31
- **Decision:** Replace the task manager's circular `IsStartup` busy indicator
  with a short dim underline carrying one small highlight dot that travels
  smoothly from side to side. Preserve D062's solid line for the active app
  and static dot for a running inactive app; do not place circles, halos, or
  filled tiles behind task icons. Carry this as a narrow patch against Fedora's
  pinned `plasma-desktop-6.7.4-1.fc44` source package because Plasma exposes no
  task-launch-indicator theme hook; do not change the system-wide busy
  indicator. Seed the full Proper color groups in the new-user and system
  `kdeglobals`, not only `ColorScheme=Proper`, so `KColorScheme` consumers such
  as Dolphin begin with the intended dark view palette on their first launch.
- **Source:** Fedora `plasma-desktop-6.7.4-1.fc44.src.rpm`, SHA-256
  `bc3e4d042be57b1d3d6edac10203f85ddb8690ae36f1ce98368ed53f4f73166a`.
  The retained source version and Fedora patches are unchanged; Proper adds
  one GPL-2.0-or-later QML patch and a `.proper1` release suffix.
- **Update method:** When Fedora updates `plasma-desktop`, pin and checksum the
  new source RPM, rebase the one QML hunk, run its package tests, and verify the
  launching, active, and running-inactive states in the review VM. Drop the
  patch if upstream adds a supported task-specific launch-indicator hook.
- **Reason:** Plasma's task startup feedback is a separate QML busy indicator,
  so styling `tasks.svg` alone cannot remove the blue circle. The first-boot
  palette also selected the Proper scheme by name without materializing its
  color groups; Dolphin's `KColorScheme::View` consequently used a light
  fallback until another scheme was applied and Proper was selected again.

## D064 — Make Proper's tokens, app icons, and product home one system

- **Status:** Accepted for implementation
- **Date:** 2026-09-01
- **Decision:** Generate the shared Qt widget styles and shortcut-reference CSS
  from `tokens.yaml` during the `proper-look-and-feel` build. Proper Apps,
  Appearance, the live welcome, Start Here, and the local shortcut reference
  consume those generated assets instead of maintaining parallel colour and
  radius literals. Ship a related dark-tile icon family for Proper Apps,
  Appearance, Shortcuts, and Coding Agent; keep the approved white launcher
  dot unchanged and use Ghostty's own identity for the terminal wrapper. Add a
  passive Start Here application that links to apps, appearance, updates,
  shortcuts, System Settings, and support. Promote it in Vicinae, but never
  autostart it or insert it into first boot.
- **Reason:** A coherent product needs one visual source of truth and a stable
  home without turning onboarding into another modal journey. Build-generated
  assets let native Qt and local web surfaces share the same decisions while
  leaving upstream KDE controls and application identities intact.

## D065 — Separate the Recommended shelf from the broad application directory

- **Status:** Accepted for implementation
- **Date:** 2026-09-01
- **Decision:** Keep the 55-entry Omarchy-compatible directory searchable by
  category and in All, but limit Recommended to Google Chrome, Helium, Signal,
  VLC, Spotify, GitHub Desktop, Visual Studio Code Insiders, Codex desktop,
  Codex CLI, and Claude Code CLI. Podman, printer compatibility, Calculator,
  stable VS Code, and all other alternatives remain available without being
  presented as Proper's front-page choices. Install Helium through its official
  Fedora COPR. Bootstrap OpenAI's official Fedora 43/44 ChatGPT desktop preview
  with the pinned reviewed RPM, which includes Codex and configures its update
  repository. Do not list Claude Desktop until Anthropic publishes a supported,
  reversible Linux provider; Claude Code CLI and the general web-app path remain
  available.
- **Sources:** [Helium Linux packaging](https://github.com/imputnet/helium-linux),
  [OpenAI ChatGPT Linux release notes](https://help.openai.com/en/articles/6825453),
  and [Anthropic Claude Desktop requirements](https://support.anthropic.com/en/articles/10065433-installing-claude-for-desktop),
  checked 2026-09-01.
- **Update method:** Review the Helium COPR and OpenAI RPM repository metadata,
  update the pinned bootstrap RPM and icon ledger when their providers change,
  and revalidate every install, removal, detection, and launch command. Recheck
  Anthropic's official platform list before adding a Claude Desktop entry.
- **Reason:** Recommended is a product opinion, not a popularity list. The full
  directory preserves breadth and user choice without making the landing page
  look indecisive or giving unofficial desktop wrappers Proper's endorsement.

## D066 — Use Inter 4 for desktop UI with Noto Sans fallback

- **Status:** Accepted from the approved taskbar typography direction
- **Date:** 2026-09-01
- **Decision:** Use Inter as the primary Proper Linux desktop, taskbar, clock,
  first-party application, GTK, login, lock-screen, and restrained boot-text
  family. Keep Noto Sans as the explicit international fallback. Keep
  JetBrains Mono only for terminal, code, fixed-width, and keyboard-reference
  surfaces. Fedora's maintained `rsms-inter-fonts-4.1-3.fc44.noarch` package is
  the pinned Inter source for version 0.1; its installed files report family
  `Inter` and OpenType font version 4.001 through fontconfig.
- **Source:** Fedora `rsms-inter-fonts-4.1-3.fc44.noarch`, from the Fedora 44
  release repository and upstream <https://rsms.me/inter/>. Noto fallback is
  Fedora `google-noto-sans-fonts-20251201-2.fc44.noarch`; the fixed-width face
  is Fedora `jetbrains-mono-fonts-2.304-10.fc44.noarch`.
- **Licence:** OFL-1.1 for Inter, Noto Sans, and JetBrains Mono as declared by
  their Fedora packages.
- **Update method:** Review the Fedora package source, installed family name,
  font metadata, licence, and fontconfig rules; update the exact RPM dependency
  and image-manifest validation deliberately; regenerate the shared UI assets;
  then require `fc-match Inter` and the desktop font settings to resolve to
  Inter in the next exact ISO guest before promotion.
- **Reason:** Inter was approved in the taskbar preview and gives Proper's
  interface a more deliberate UI-specific voice. Explicit packaging and
  regression checks prevent a missing font from silently turning that design
  choice back into Noto Sans while retaining broad glyph fallback.

## D067 — Correct the installed shelf, terminal, window, and application feedback

- **Status:** Accepted from installed-image feedback
- **Date:** 2026-09-01
- **Decision:** Keep the bottom shelf in fit-content mode, retain a nominal
  560-pixel minimum, and insert a fixed 86-pixel spacer between icon tasks and
  the system tray. Plasma 6.7 applies its minimum-length clamp only to custom
  panels, so the spacer is the supported fit-content input that produces the
  requested visible floor of about 560 pixels while still allowing the shelf
  to grow with additional tasks and tray items. Migrate only a panel retaining
  the complete old Proper geometry and structure; never overwrite a user-set
  width. Replace D064's off-centre white launcher dot with four centred cells
  from Proper's ASCII-influenced identity and disable startup notification for
  its idempotent opener. Bind both a bare `Meta` tap and `Meta+Space` to that
  opener through KDE's native modifier-only shortcut support, whose state
  machine suppresses the tap whenever Meta participates in another chord.
  Move reversible workspace arrangement from `Meta+Shift+T` to `Meta+Z`, and
  promote both arrangement and search as Start Here pointer cards.

  Supersede D061's 88-percent blurred terminal treatment with 50-percent
  opacity and no compositor blur so the desktop is plainly visible through
  Ghostty. In Proper Apps, present authentication, download, install, and
  configuration phases as active work; reconcile RPM, Flatpak, or command
  detection after every provider exit; distinguish cancellation and partial
  completion; and never claim that nothing changed without checking.
- **Reason:** The latest installed ISO made the shelf collapse around its
  icons, visually merged tasks with status controls, mis-centred the promoted
  launcher, advertised every idempotent launcher click as a new application
  startup, obscured the desktop behind Ghostty, hid workspace arrangement, and
  collapsed several materially different package outcomes into one ambiguous
  failure. These are product-state defects visible only in the installed
  experience, so the new defaults, narrow migrations, and acceptance checks
  must reflect the observed behaviour.

## D068 — Restyle system controls without forking their applets

- **Status:** Accepted at the installed-image system-surfaces review
- **Date:** 2026-09-01
- **Decision:** Keep Fedora's unmodified `plasma-nm`, `bluedevil`, `plasma-pa`,
  `powerdevil`, and `kscreen` packages and their upstream popup hierarchy.
  Extend the Proper Plasma Style only through the supported `button`, `line`,
  `lineedit`, `listitem`, `slider`, `switch`, `tabbar`, and `viewitem` SVG
  element contracts. Use Proper's restrained blue selection, dark heading and
  popup surfaces, nine-pixel controls, Inter typography, and Breeze-derived
  system icons. Brightness and Display Configuration remain separate upstream
  applets; audio retains its Devices and Applications tabs; no device summary
  cards, new footer actions, or reordered controls are introduced.
- **Update method:** Fedora continues updating all five applet RPMs normally.
  On a Plasma major update, rebuild the generated Style assets from
  `tokens.yaml`, validate every required SVG element, and exercise the unchanged
  applets at normal and 200% scale. Do not add an applet patch merely to retain
  the approved appearance.
- **Reason:** Plasma Style can change supported control presentation but cannot
  safely alter applet information hierarchy. A proposed richer device-first
  composition would have required five maintained downstream package patches.
  The PM rejected that update burden and approved the honest style-only result.
