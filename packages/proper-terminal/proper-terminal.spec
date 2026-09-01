Name: proper-terminal
Version: 1.3.1
Release: 4%{?dist}
Summary: Ghostty terminal and Proper developer essentials
License: MIT
URL: https://ghostty.org/
Source0: https://release.files.ghostty.org/1.3.1/ghostty-1.3.1.tar.gz
Source1: ghostty.conf
Source2: proper-terminal.desktop
Source3: proper-terminal-dolphin.desktop
Source4: https://ziglang.org/download/0.15.2/zig-x86_64-linux-0.15.2.tar.xz
Source5: https://ziglang.org/download/0.15.2/zig-x86_64-linux-0.15.2.tar.xz.minisig
Source6: https://release.files.ghostty.org/1.3.1/ghostty-1.3.1.tar.gz.minisig
Patch0: ghostty-ext-background-effect.patch
BuildRequires: gcc
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: gtk4-layer-shell-devel
BuildRequires: pkgconf
BuildRequires: gettext
BuildRequires: git-core
BuildRequires: minisign
BuildRequires: pandoc
BuildRequires: oniguruma-devel
Requires: btop
Requires: git
Requires: ripgrep
Requires: fd-find
Requires: fzf
Requires: jetbrains-mono-fonts
Requires: wl-clipboard
BuildArch: x86_64
%global debug_package %{nil}
%description
Pinned upstream Ghostty with Proper's terminal defaults and Dolphin integration.
%prep
%setup -q -n ghostty-%{version}
minisign -Vm %{SOURCE4} -x %{SOURCE5} -P RWSGOq2NVecA2UPNdBUZykf1CCb147pkmdtYxgb3Ti+JO/wCYvhbAb/U
minisign -Vm %{SOURCE0} -x %{SOURCE6} -P RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV
%patch -P 0 -p1
%build
tar -xf %{SOURCE4}
zig_bin="$PWD/zig-x86_64-linux-0.15.2/zig"
export PATH="$(dirname "$zig_bin"):$PATH"
export ZIG_GLOBAL_CACHE_DIR="$PWD/zig-global-cache"
./nix/build-support/fetch-zig-cache.sh
DESTDIR="$PWD/ghostty-root" "$zig_bin" build --prefix /usr --system "$ZIG_GLOBAL_CACHE_DIR/p" -Doptimize=ReleaseFast -Dcpu=baseline
%install
cp -a ghostty-root/usr/. %{buildroot}%{_prefix}/
# Ghostty 1.3.1's default install step also emits its experimental VT SDK.
# Proper ships the terminal application, not a development surface with no
# in-product consumer, so keep that SDK out of the lean desktop package.
rm -r %{buildroot}%{_includedir}/ghostty
rm %{buildroot}%{_prefix}/lib/libghostty-vt.so
rm %{buildroot}%{_prefix}/lib/libghostty-vt.so.0
rm %{buildroot}%{_prefix}/lib/libghostty-vt.so.0.1.0
rm %{buildroot}%{_datadir}/pkgconfig/libghostty-vt.pc
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/skel/.config/ghostty/config
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/ghostty/config
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/proper-terminal.desktop
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_datadir}/kio/servicemenus/proper-terminal-dolphin.desktop
%files
%{_bindir}/ghostty
%{_datadir}/
%{_userunitdir}/app-com.mitchellh.ghostty.service
%config(noreplace) %{_sysconfdir}/skel/.config/ghostty/config
%config(noreplace) %{_sysconfdir}/xdg/ghostty/config
%changelog
* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 1.3.1-4
- Make the desktop clearly visible through Ghostty at 50 percent opacity
- Disable terminal blur so the wallpaper remains legible behind the window

* Tue Sep 01 2026 Proper Linux <proper@example.invalid> - 1.3.1-3
- Require the Fedora JetBrains Mono package used by the terminal configuration

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 1.3.1-2
- Rebuild the finalized ext-background-effect protocol backport
- Increase restrained terminal translucency to a visibly distinct 88 percent

* Mon Aug 31 2026 Proper Linux <proper@example.invalid> - 1.3.1-1
- Update to the signed Ghostty 1.3.1 release and Zig 0.15.2 toolchain
- Add restrained 92 percent background opacity aligned to Proper Horizon tokens
- Backport Ghostty's ext-background-effect protocol for blur on Plasma 6.7

* Sun Aug 30 2026 Proper Linux <proper@example.invalid> - 1.2.3-7
- Remove the retained dropdown prototype and keep ordinary Ghostty launching

* Wed Aug 26 2026 Proper Linux <maintainers@properlinux.example> - 1.2.3-6
- Give the retained dropdown enough columns and rows for btop and normal shell use.

* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 1.2.3-5
- Explicitly load and start the retained KWin script through its scripting service.

* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 1.2.3-4
- Use Plasma 6 windowList for retained dropdown matching.

* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 1.2.3-3
- Enable the packaged KWin dropdown script for each Plasma user session.

* Wed Aug 26 2026 Proper Linux <proper@example.invalid> - 1.2.3-2
- Ship the supported KWin retained-dropdown integration.

* Tue Aug 25 2026 Proper Linux <proper@example.invalid> - 1.2.3-1
- Pin official Ghostty 1.2.3 source release and Proper configuration
