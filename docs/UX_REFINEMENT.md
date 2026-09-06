# Outstanding UX work

Product direction and shipped behaviour live in [PRODUCT.md](PRODUCT.md) and
[ARCHITECTURE.md](ARCHITECTURE.md). The items below remain to be investigated or
validated; they are not claims of completed work.

- Files: refine toolbar and Places spacing, investigate native sidebar frost,
  and exercise rename, copy conflicts, undo, trash and removable drives.
- Proper Apps: verify offline, cancellation, partial results and provider errors,
  plus agent selection and web-app creation/removal with populated fixtures.
- Settings: check typography, theme propagation, restart guidance, search, Back,
  long labels and real devices. Review native file pickers and permission dialogs.
- Shell: check popup placement, truncation, keyboard dismissal, tray identities,
  notification actions/history and calendar across themes and scale.
- Arrival and recovery: validate constrained live-welcome layouts, launch errors,
  installation completion, login/lock failures and update/reboot progress.
- Accessibility and hardware: finish 200% scale, reduced motion, blur-disabled,
  keyboard, screen-reader, multiple/rotated display, low-storage and disconnected
  device checks. Review Discover's update presentation without replacing Fedora's
  updater.

## Compatibility findings to retain

Native Dolphin sidebar frost remains unshipped. A Dolphin 26.08.0 / Kvantum
1.1.6 trial achieved translucent Places with opaque content, but changed other
controls and lacked a satisfactory blur-disabled fallback. Any candidate must
preserve readable text, native file operations, palette changes and scaling.
Whole-window opacity also fades text; forcing blur cannot make opaque widgets
translucent. See the [Kvantum theme contract](https://raw.githubusercontent.com/tsujan/Kvantum/V1.1.6/Kvantum/doc/Theme-Config)
and [Qt translucency requirements](https://doc.qt.io/qt-6/qwidget.html#creating-translucent-windows).

The shared material helper reads the application palette: a transparent widget
stylesheet can overwrite the root widget palette. Keep blur confined to the
navigation rail and retain the solid fallback.

Qt 6.11.2 embeds resource timestamps from `SOURCE_DATE_EPOCH`, which Fedora's RPM
build derives from the changelog. Advance the changelog when changing embedded
QML, and test normal upgrades with existing QML caches intact. Clearing caches
can conceal an invalidation failure. See [Qt's resource compiler](https://github.com/qt/qtbase/blob/v6.11.2/src/tools/rcc/rcc.cpp).

## Acceptance checks

Keep observable states with their owning packages:

- [Apps acceptance states](../packages/proper-apps/tests/ux-acceptance.tsv)
- [Material acceptance states](../packages/proper-look-and-feel/tests/app-material-acceptance.tsv)

Follow the validation requirements in [AGENTS.md](../AGENTS.md). Generated
screenshots and build logs belong outside Git; package or screenshot checks do
not substitute for an installed-system review.
