# Plasma Login Manager display layout — prototype

Proper Linux uses Fedora KDE 44's Plasma Login Manager (PLM), not SDDM.

The desktop defaults are deliberately small configuration fragments rather
than a copied reference home directory. Fedora's `livesys` service creates its
temporary live account from `/etc/skel`, so the same fragment also gives the
live desktop its shipped wallpaper without modifying an existing user.

PLM deliberately keeps greeter display settings separate from an ordinary user
profile: it runs as the `plasmalogin` system user. The supported configuration
is `/etc/plasmalogin.conf`, and its System Settings module exposes the greeter
appearance and display settings. Fedora 44 ships distro defaults in
`/usr/lib/plasmalogin/defaults.conf`; that is the supported image-time default
file for the wallpaper. Proper replaces that small Fedora default with its
equivalent Proper wallpaper default, while leaving `/etc/plasmalogin.conf`
available for administrator overrides. Fedora 44 does not consume the
previously assumed `plasmalogin.conf.d` fragment path for this setting.

The upstream Fedora installer does not currently export the live session's
chosen monitor layout as a PLM greeter layout in its KIWI description. For the
prototype, the visible, supported hand-off is the **Login Screen** page in
System Settings after the first account is created: choose the required display
layout there and apply it to PLM. This is intentionally not a bespoke greeter
patch.

Before checkpoint 1, the installed VM will be tested at normal orientation and
with a 90-degree virtual display rotation. The checkpoint evidence will show
the PLM layout action and the resulting greeter orientation.
