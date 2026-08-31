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
