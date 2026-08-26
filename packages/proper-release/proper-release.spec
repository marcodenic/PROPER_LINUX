Name:           proper-release
Version:        0.1
Release:        1%{?dist}
Summary:        Proper Linux release identity and metadata
License:        GPL-3.0-or-later
BuildArch:      noarch

%description
Release metadata for Proper Linux, an independent Fedora KDE derivative.

%install
install -Dpm 0644 %{_sourcedir}/proper-release.conf %{buildroot}%{_sysconfdir}/proper-linux/release.conf

%files
%config(noreplace) %{_sysconfdir}/proper-linux/release.conf
