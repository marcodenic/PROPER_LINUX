Name:           proper-branding
Version:        0.1
Release:        3%{?dist}
Summary:        Proper Linux identity, installer, and boot artwork
License:        CC-BY-SA-4.0 AND GPL-3.0-or-later
BuildArch:      noarch
BuildRequires:  ImageMagick
Requires:       plymouth-theme-spinner
Requires:       plymouth-plugin-two-step
Requires:       rsms-inter-fonts = 4.1-3%{?dist}

%description
Canonical grid-built Proper Linux marks and their supported integrations for
the desktop icon theme, Anaconda, Cockpit Web UI, and Plymouth.

%build
bash %{_sourcedir}/generate-plymouth-assets.sh %{_sourcedir} %{_builddir}/proper-plymouth

%install
identity=%{buildroot}%{_datadir}/proper-linux/identity
install -d "$identity"
install -pm 0644 %{_sourcedir}/proper-wordmark.svg "$identity/proper-wordmark.svg"
install -pm 0644 %{_sourcedir}/proper-wordmark-dark.svg "$identity/proper-wordmark-dark.svg"
install -pm 0644 %{_sourcedir}/proper-logo-icon.svg "$identity/proper-logo-icon.svg"

install -Dpm 0644 %{_sourcedir}/proper-logo-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/proper-logo-icon.svg
install -Dpm 0644 %{_sourcedir}/proper-logo-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.properlinux.Installer.svg
for icon in proper-apps proper-appearance proper-shortcuts proper-agent; do
    install -Dpm 0644 "%{_sourcedir}/$icon.svg" "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/$icon.svg"
done
install -Dpm 0644 %{_sourcedir}/proper-anaconda.css %{buildroot}%{_datadir}/anaconda/pixmaps/proper.css

cockpit=%{buildroot}%{_datadir}/cockpit/branding/proper
install -d "$cockpit"
install -pm 0644 %{_sourcedir}/cockpit-branding.css "$cockpit/branding.css"
install -pm 0644 %{_sourcedir}/proper-wordmark.svg "$cockpit/logo.svg"

plymouth=%{buildroot}%{_datadir}/plymouth/themes/proper
install -d "$plymouth"
install -pm 0644 %{_sourcedir}/proper.plymouth "$plymouth/proper.plymouth"
install -pm 0644 %{_builddir}/proper-plymouth/*.png "$plymouth/"
for helper in bullet.png capslock.png entry.png keyboard.png keymap-render.png lock.png; do
    ln -s "../spinner/$helper" "$plymouth/$helper"
done

%post
if command -v plymouth-set-default-theme >/dev/null 2>&1; then
    plymouth-set-default-theme proper >/dev/null 2>&1 || :
fi

%files
%{_datadir}/proper-linux/identity/
%{_datadir}/icons/hicolor/scalable/apps/proper-logo-icon.svg
%{_datadir}/icons/hicolor/scalable/apps/org.properlinux.Installer.svg
%{_datadir}/icons/hicolor/scalable/apps/proper-apps.svg
%{_datadir}/icons/hicolor/scalable/apps/proper-appearance.svg
%{_datadir}/icons/hicolor/scalable/apps/proper-shortcuts.svg
%{_datadir}/icons/hicolor/scalable/apps/proper-agent.svg
%{_datadir}/anaconda/pixmaps/proper.css
%{_datadir}/cockpit/branding/proper/
%{_datadir}/plymouth/themes/proper/

%changelog
* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-3
- Use the packaged Inter family for restrained boot-theme text

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 0.1-2
- Add a coherent icon family for Proper Apps, Appearance, Shortcuts, and Coding Agent

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 0.1-1
- Introduce the approved five-by-five grid wordmark and compact P mark
- Brand Anaconda's supported GTK and Cockpit extension points
- Add a restrained Proper Plymouth theme with a five-cell progress pulse
