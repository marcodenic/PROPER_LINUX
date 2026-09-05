# Everyday UX refinement

## App interiors: first implementation pass

Proper Apps now uses flexible product rows with native keyboard actions,
search and browsing in a left navigation rail, an honestly scoped Installed
view, and in-window details. Back retains the search and existing catalogue
widgets/scroll position. Categories reset when changing views, preventing an
invisible filter from hiding recommendations. Provider execution and state
reconciliation remain in their existing owner.

Start Here has a frosted greeting rail, two primary destinations and compact rows
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
upstream sources. The shared production helper now powers the actual Apps and Start Here
windows, using the 80% navigation token, a persisted solid/frosted choice and
KWindowEffects capability detection. Only the rail receives a blur region;
content, text and buttons retain their own opacity. It reads the application
palette rather than the root widget palette, which a transparent stylesheet
can overwrite. Native Dolphin integration remains open; title decoration alone
cannot make opaque widgets translucent.

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

## Follow-up: materials and Settings chrome

The follow-up retains native page headings and actions. A pinned System
Settings presentation patch gives search the full sidebar width and
moves the application menu to its footer. The normal window-operations menu
remains in the title bar. This is a fourth explicit source-package exception;
its provenance and update method are in packages/plasma-systemsettings.
The validator lists that exact exception, rather than permitting arbitrary forks.

Tray cards set the native PopupPlasmaWindow margin to 8 logical pixels when
reparented into their tooltip window. The gap is outside the painted card and
uses Plasma's orientation-aware placement. No libplasma fork is added.

Follow-up acceptance states live in
packages/proper-look-and-feel/tests/app-material-acceptance.tsv; native captures
and exact package/build results live in reviews/material-pass-20260905.
The review baseline is local main commit 0aa20d1. Follow-up changes stay
uncommitted until the product manager reviews them; nothing is pushed.

Material compatibility was checked against Fedora's exact 6.7.4 source RPMs,
Qt 6.11.2 and KWindowSystem 6.29. Official API references:
- https://api.kde.org/kwindoweffects.html
- https://doc.qt.io/qt-6/qwidget.html#creating-translucent-windows
- https://api.kde.org/plasmaquick-popupplasmawindow.html
- https://packages.fedoraproject.org/pkgs/plasma-systemsettings/plasma-systemsettings/
The Fedora web index was older than the installed RPM; the checksummed SRPM
and installed package supplied the actual version and compiled QML contract.

Next visual priorities remain Files' toolbar/Places/content transition,
Appearance's tall preview-and-Apply hierarchy and theme propagation, duplicate
window/application menu glyphs, and inconsistent native file-picker/permission
surfaces. Real provider failures, notification actions and hardware states need
journey tests; a screenshot of an empty page does not establish those behaviours.
For Files, evaluate a maintained Qt application-style integration in a disposable
profile before adopting it. Whole-window opacity fades text as well as material,
and force-blur alone cannot change Dolphin's opaque widget paint. No Dolphin
fork or global widget-style replacement is introduced in this pass.

The installed review also found that Start Here’s Help destination returns a
GitHub 404 in an unsigned-in browser (the configured URL matches the repository
remote). Public help needs a shipped local guide or an accessible published
destination; this pass does not change repository visibility. Discover’s Updates
route opens correctly, but its crowded catalogue sidebar and multi-backend loading
copy remain visually inconsistent with Proper Apps. No updates were applied.

An experiment to suppress the Settings home heading through the KCM toolbar
style did not remove the visible host strip. That ineffective code was removed;
the final chrome cleanup preserves the heading. Intermediate captures are not
accepted as evidence of heading removal.
