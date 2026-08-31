Name:           proper-welcome
Version:        0.1
Release:        1%{?dist}
Summary:        Proper Linux live-session welcome
License:        GPL-3.0-or-later
BuildArch:      x86_64
BuildRequires:  qt6-qtbase-devel
Requires:       anaconda-live
Requires:       proper-branding

%description
A focused, pointer-accessible live-session choice between exploring the Proper
desktop and launching Fedora's maintained Anaconda installer.

%prep
cp %{_sourcedir}/main.cpp %{_sourcedir}/proper-welcome.pro .

%build
qmake6 CONFIG+=release proper-welcome.pro
make %{?_smp_mflags}

%install
install -Dpm 0755 proper-welcome %{buildroot}%{_bindir}/proper-welcome
install -Dpm 0644 %{_sourcedir}/proper-welcome.desktop %{buildroot}%{_datadir}/proper-linux/live/proper-welcome.desktop
install -Dpm 0644 %{_sourcedir}/proper-install.desktop %{buildroot}%{_datadir}/proper-linux/live/proper-install.desktop

%files
%{_bindir}/proper-welcome
%{_datadir}/proper-linux/live/proper-welcome.desktop
%{_datadir}/proper-linux/live/proper-install.desktop

%changelog
* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-1
- Add the approved full-screen Try Proper or Install Proper arrival choice
- Keep the installer launch delegated to Fedora's maintained liveinst entrypoint
