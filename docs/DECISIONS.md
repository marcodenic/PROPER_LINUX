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

## D008 — AppGrid plus Vicinae

- **Status:** Provisional through PM checkpoint 3
- **Date:** 2026-08-24
- **Decision:** AppGrid is the browsable mouse-first app surface. Vicinae is the Raycast-style command/search surface. KRunner remains a fallback.
- **Reason:** The two products serve distinct browse and command intents. The PM will remove one if the installed prototype feels redundant.

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
