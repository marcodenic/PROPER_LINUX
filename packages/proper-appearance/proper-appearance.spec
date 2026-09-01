Name:           proper-appearance
Version:        0.1
Release:        5%{?dist}
Summary:        Proper Linux appearance, text sizing, and arrival sync
License:        GPL-3.0-or-later
BuildRequires:  qt6-qtbase-devel
Requires:       plasma-workspace
Requires:       polkit
Requires:       proper-look-and-feel >= 0.1-21
Requires:       /usr/bin/kwriteconfig6

%description
A restrained visual control for three curated desktop styles, coordinated
text-size presets, and the five Proper Linux wallpapers. Wallpaper selections
can explicitly synchronise Plasma Login Manager after authentication.

%prep
cp %{_sourcedir}/proper-appearance.cpp %{_sourcedir}/proper-appearance.pro .

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
