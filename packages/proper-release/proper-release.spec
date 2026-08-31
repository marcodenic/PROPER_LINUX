Name:           proper-release
Version:        0.1
Release:        2%{?dist}
Summary:        Proper Linux release identity and metadata
License:        GPL-3.0-or-later
BuildArch:      noarch
Requires:       fedora-release-common = 44-18
Requires:       fedora-release-kde-desktop = 44-18
Provides:       fedora-release-identity = 44-18
Provides:       fedora-release-identity-kde = 44-18
Provides:       fedora-release-identity-kde-desktop = 44-18
Obsoletes:      fedora-release-identity-kde-desktop <= 44-18

%description
Release metadata for Proper Linux, an independent Fedora KDE derivative.

%install
install -Dpm 0644 %{_sourcedir}/proper-release.conf %{buildroot}%{_sysconfdir}/proper-linux/release.conf
install -Dpm 0644 %{_sourcedir}/os-release %{buildroot}%{_prefix}/lib/os-release
install -Dpm 0644 %{_sourcedir}/proper-anaconda.conf %{buildroot}%{_sysconfdir}/anaconda/profile.d/proper.conf
install -Dpm 0644 %{_sourcedir}/80-proper-desktop.preset %{buildroot}%{_prefix}/lib/systemd/system-preset/80-proper-desktop.preset
install -Dpm 0644 %{_sourcedir}/81-desktop.preset %{buildroot}%{_prefix}/lib/systemd/system-preset/81-desktop.preset
install -Dpm 0644 %{_sourcedir}/plasma-desktop.conf %{buildroot}%{_sysconfdir}/dnf/protected.d/plasma-desktop.conf
install -Dpm 0644 %{_sourcedir}/org.properlinux.ProperLinux-0.1.swidtag \
  %{buildroot}%{_prefix}/lib/swidtag/properlinux.org/org.properlinux.ProperLinux-0.1.swidtag

%files
%config(noreplace) %{_sysconfdir}/proper-linux/release.conf
%{_prefix}/lib/os-release
%{_sysconfdir}/anaconda/profile.d/proper.conf
%{_prefix}/lib/systemd/system-preset/80-proper-desktop.preset
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%config(noreplace) %{_sysconfdir}/dnf/protected.d/plasma-desktop.conf
%{_prefix}/lib/swidtag/properlinux.org/org.properlinux.ProperLinux-0.1.swidtag

%changelog
* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Replace Fedora's KDE edition identity with the Proper Linux product identity
- Inherit Fedora KDE's installer policy through a Proper Anaconda profile
- Preserve Fedora 44 repositories, package macros, and service presets
