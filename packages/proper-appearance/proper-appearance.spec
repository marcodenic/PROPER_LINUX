Name:           proper-appearance
Version:        0.1
Release:        12%{?dist}
Summary:        Proper Linux appearance, text sizing, and arrival sync
License:        GPL-3.0-or-later
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-kwindowsystem-devel
Requires:       plasma-workspace
Requires:       polkit
Requires:       proper-look-and-feel >= 0.1-62
Requires:       /usr/bin/kwriteconfig6

%description
A restrained visual control for three curated desktop styles, coordinated
text-size presets, and the thirteen Proper Linux wallpapers. Wallpaper selections
can explicitly synchronise Plasma Login Manager after authentication.

%prep
cp %{_sourcedir}/proper-appearance.cpp %{_sourcedir}/proper-appearance.pro .

cp %{_sourcedir}/../proper-look-and-feel/proper-material-window.h .

%build
qmake6 CONFIG+=release proper-appearance.pro
make %{?_smp_mflags}

%install
install -Dpm 0755 proper-appearance %{buildroot}%{_bindir}/proper-appearance
install -Dpm 0644 %{_sourcedir}/proper-appearance.desktop %{buildroot}%{_datadir}/applications/proper-appearance.desktop
install -Dpm 0755 %{_sourcedir}/proper-set-login-wallpaper %{buildroot}%{_libexecdir}/proper-set-login-wallpaper

%files
%{_bindir}/proper-appearance
%{_libexecdir}/proper-set-login-wallpaper
%{_datadir}/applications/proper-appearance.desktop

%changelog
* Sat Sep 05 2026 Proper Linux <proper@example.invalid> - 0.1-12
- Separate appearance tasks and keep Apply actions visible beside the gallery

* Sat Sep 05 2026 Proper Linux <proper@example.invalid> - 0.1-11
- Describe Alpine Light’s matching frosted shell accurately

* Thu Sep 03 2026 Proper Linux <proper@example.invalid> - 0.1-10
- Render every desktop-style preview from the installed semantic palette

* Wed Sep 02 2026 Proper Linux <proper@example.invalid> - 0.1-9
- Add Salt-Flat Station to the wallpaper gallery and authenticated login sync
- Require the artwork package that contains the thirteenth wallpaper

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-8
- Add the PM-approved Highland Blue Hour and Highland Sunrise photographs
- Keep both available for desktop, lock-screen, and authenticated login sync

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-7
- Add all five reviewed landscape and rally concepts to the Appearance gallery
- Keep every wallpaper available for desktop, lock-screen, and authenticated login sync
- Replace the Light preset's abstract background with the approved Alpine Morning photograph

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-6
- Materialise the selected Plasma colour scheme so Light and Midnight cannot inherit stale palette groups
- Notify the live desktop of font changes and update Appearance immediately

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-5
- Make every text-size preset preserve Inter across Plasma, KWin, and GTK
- Continue changing only Ghostty size so its JetBrains Mono family is retained

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-4
- Use the shared token-generated Proper widget style and first-party icon

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-3
- Add preview-first desktop styles and coordinated Plasma, GTK, and Ghostty text sizes
- Keep content surfaces opaque while the Proper shell and terminal own translucency

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Give the wallpaper gallery a restrained Proper Dark presentation

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-1
- Add the curated wallpaper gallery and explicit login wallpaper sync
