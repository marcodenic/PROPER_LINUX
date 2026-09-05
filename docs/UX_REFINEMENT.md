# Everyday UX refinement

## App interiors: first implementation pass

Proper Apps now uses flexible product rows with native keyboard actions,
search above the catalogue, wrapping navigation, an honestly scoped Installed
view, and in-window details. Back retains the search and existing catalogue
widgets/scroll position. Categories reset when changing views, preventing an
invisible filter from hiding recommendations. Provider execution and state
reconciliation remain in their existing owner.

Start Here has an unboxed greeting, two primary destinations and compact rows
for settings, updates, shortcuts and help. Whole rows are native buttons with
accessible names and descriptions. The shortcut guide includes Command Centre
and explains the Meta key. Launch errors identify the failed destination.
The live installer welcome composition is unchanged.

`proper-look-and-feel` owns the shared descriptive-button sizing helper and
styles. Labels inherit text size; the native combo arrow is retained; hover is
reserved for actual actions. The Apps and Welcome RPMs require the matching
style revision. No user configuration is migrated or reset by this pass.

## Compatibility and validation

Target: Fedora 44, Qt 6.11.2, Plasma 6.7.4, KF6 6.29. Native QPushButton keeps
keyboard, focus and accessibility semantics, while a focused subclass measures
its child layout. Catalogue filtering and detail-page cleanup have separate
functions. Exact RPM versions live in the owning specs.

Named installed-VM states are versioned in
`packages/proper-apps/tests/ux-acceptance.tsv`. Generated screenshots, package
logs, and the handoff live outside Git in the build area's
`reviews/app-polish-20260905/`. This is app/package validation on the existing
installed disk, not a new ISO, installer, release, or hardware validation pass.

Official guidance consulted:
- https://develop.kde.org/hig/layout_and_nav/
- https://develop.kde.org/hig/accessibility/
- https://develop.kde.org/hig/status_changes/
- https://doc.qt.io/qt-6.11/qabstractbutton.html
- https://fedoraproject.org/wiki/QA:Testcase_upgrade_plasma-discover_current_kde

## Material direction

`experiments/app-material` proves an alpha-backed Qt window with a bounded
KWindowEffects navigation blur region, an opaque file canvas and a manual solid
comparison. It is not packaged and is not Dolphin. It uses the active palette
and a read-only directory model. See its README for exact limitations and
upstream sources. Native Dolphin client integration and automatic fallback
remain open; title decoration alone cannot make opaque app widgets translucent.

## Remaining work from the design audit

The full 5 September visual/source audit is retained in the generated build
area at `reviews/ux-audit-20260905/REVIEW.md`; its 43 entries distinguish observed
problems from risks and design proposals. Continue in this order:

1. Files: compare smaller Places icons and calmer spacing in a disposable
   profile; then investigate a maintainable native navigation-material hook.
   Keep file content opaque, Dolphin's identity, user folders and saved choices.
   Verify populated rename/copy/conflict/undo/trash and removable-drive journeys.
2. Proper Apps: validate real offline, cancellation, partial-result and provider
   error journeys; keep app identity attached to progress. Review agent selection
   and web-app creation/removal with populated fixtures. Do not invent store
   ratings, screenshots, installed-state coverage or provider success.
3. Appearance and settings: scale typography throughout forms and toolbars,
   tighten preview hierarchy, make restart requirements clear, and verify search,
   back navigation, long labels and real devices.
4. Shell and status: review popup placement, truncation, keyboard dismissal,
   mixed tray identities, notification actions/history, calendar and tooltips
   across themes and scale. Keep upstream controls and behaviour.
5. First-run and recovery: review live welcome at constrained sizes, launch
   failure, installation completion, login/lock failures, update/reboot progress
   and recovery copy. These changes require an image integration pass.
6. Finish the cross-cutting matrix: 200% scale, reduced motion, blur disabled,
   keyboard-only use, screen-reader names, multiple/rotated displays, low storage,
   disconnected hardware and uncommon failure states.

These remaining items are not claimed fixed or validated by the app pass.
