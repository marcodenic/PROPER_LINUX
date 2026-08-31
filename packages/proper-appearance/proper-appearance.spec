Name:           proper-appearance
Version:        0.1
Release:        2%{?dist}
Summary:        Proper Linux wallpaper gallery and arrival sync
License:        GPL-3.0-or-later
BuildRequires:  qt6-qtbase-devel
Requires:       plasma-workspace
Requires:       polkit
Requires:       proper-look-and-feel >= 0.1-6

%description
A restrained visual gallery for the five curated Proper Linux wallpapers.
Selections apply to the Plasma desktop and lock screen, with an explicit,
authenticated option to synchronise Plasma Login Manager.

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
* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Give the wallpaper gallery a restrained Proper Dark presentation

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-1
- Add the curated wallpaper gallery and explicit login wallpaper sync
