Name: proper-apps
Version: 0.1
Release: 3%{?dist}
Summary: Proper Linux curated application catalogue
License: GPL-3.0-or-later
BuildRequires: qt6-qtbase-devel
%description
Small catalogue front end delegating installs to Fedora, Flatpak, and official vendor paths.
%prep
cp %{_sourcedir}/main.cpp %{_sourcedir}/proper-apps.pro .
%build
qmake6 CONFIG+=release proper-apps.pro
make %{?_smp_mflags}
%install
install -Dpm 0755 proper-apps %{buildroot}%{_bindir}/proper-apps
install -Dpm 0644 %{_sourcedir}/proper-apps.desktop %{buildroot}%{_datadir}/applications/proper-apps.desktop
install -Dpm 0644 %{_sourcedir}/../../apps/catalogue-v1.json %{buildroot}%{_datadir}/proper-apps/catalogue-v1.json
%files
%{_bindir}/proper-apps
%{_datadir}/applications/proper-apps.desktop
%{_datadir}/proper-apps/catalogue-v1.json

%changelog
* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Refresh installed-state presentation and maintained provider catalogue.
* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 0.1-3
- Capture provider failures and present bounded technical diagnostics.
