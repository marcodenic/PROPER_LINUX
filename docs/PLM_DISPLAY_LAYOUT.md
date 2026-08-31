# Plasma Login Manager display layout

Proper Linux uses Fedora KDE 44's Plasma Login Manager (PLM), not SDDM.

The desktop defaults are deliberately small configuration fragments rather
than a copied reference home directory. Fedora's `livesys` service creates its
temporary live account from `/etc/skel`, so the same fragment also gives the
live desktop its shipped wallpaper without modifying an existing user.

PLM deliberately keeps greeter settings separate from an ordinary user profile:
it runs as the `plasmalogin` system user. Fedora 44 ships distro defaults in
`/usr/lib/plasmalogin/defaults.conf`. A 6.7.4 source audit also confirms the
normal configuration cascade loads `/etc/plasmalogin.conf` and sorted fragments
under `/etc/plasmalogin.conf.d`; a changed wallpaper applies when the greeter
process is next started, not to an already-running wallpaper process.

Proper's image default remains in the packaged distro-default file. The
`proper-appearance` “Use everywhere” action writes a separate administrator
fragment through an authenticated, fixed-ID helper. This keeps the supported
override order intact and never replaces an arbitrary path supplied by a user.

PLM 6.7.4 does not provide an external composition theme. Its QML files are
compiled into `/usr/libexec/plasma-login-greeter`, which loads `Main.qml` from a
`qrc:` URL. Proper therefore rebuilds Fedora's exact, checksum-verified source
RPM with one small patch: include `ProperMain.qml` in that resource module and
select it as the entry point. Authentication, users, sessions, state, power
actions, daemon integration, and package ownership stay upstream. This patch
must be reviewed, rebuilt, and retested on every PLM version change.

The Fedora installer does not currently export the live session's monitor
layout to the installed PLM greeter. The visible supported hand-off remains the
**Login Screen** page in System Settings: choose the required display layout and
apply it to PLM. Installed validation covers normal orientation and a 90-degree
virtual display rotation so that no user must authenticate against a sideways
screen.
