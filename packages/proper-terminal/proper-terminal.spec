Name: proper-terminal
Version: 1.2.3
Release: 7%{?dist}
Summary: Ghostty terminal and Proper developer essentials
License: MIT
URL: https://ghostty.org/
Source0: https://release.files.ghostty.org/1.2.3/ghostty-1.2.3.tar.gz
Source1: ghostty.conf
Source2: proper-terminal.desktop
Source3: proper-terminal-dolphin.desktop
Source4: https://ziglang.org/download/0.14.1/zig-x86_64-linux-0.14.1.tar.xz
Source5: https://ziglang.org/download/0.14.1/zig-x86_64-linux-0.14.1.tar.xz.minisig
Source6: https://release.files.ghostty.org/1.2.3/ghostty-1.2.3.tar.gz.minisig
BuildRequires: gcc
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: gtk4-layer-shell-devel
BuildRequires: pkgconf
BuildRequires: gettext
BuildRequires: minisign
BuildRequires: pandoc
BuildRequires: oniguruma-devel
Requires: btop
Requires: git
Requires: ripgrep
Requires: fd-find
Requires: fzf
Requires: wl-clipboard
BuildArch: x86_64
%global debug_package %{nil}
%description
Pinned upstream Ghostty with Proper's terminal defaults and Dolphin integration.
%prep
%setup -q -n ghostty-%{version}
minisign -Vm %{SOURCE4} -x %{SOURCE5} -P RWSGOq2NVecA2UPNdBUZykf1CCb147pkmdtYxgb3Ti+JO/wCYvhbAb/U
minisign -Vm %{SOURCE0} -x %{SOURCE6} -P RWQlAjJC23149WL2sEpT/l0QKy7hMIFhYdQOFy0Z7z7PbneUgvlsnYcV
%build
tar -xf %{SOURCE4}
zig_bin="$PWD/zig-x86_64-linux-0.14.1/zig"
export PATH="$(dirname "$zig_bin"):$PATH"
export ZIG_GLOBAL_CACHE_DIR="$PWD/zig-global-cache"
sed -i '/codeberg.org\/atman\/zg/d; /github.com\/TUSF\/zigimg/d' build.zig.zon.txt
sed -i 's|https://github.com/mbadolato/iTerm2-Color-Schemes/releases/download/release-20251002-142451-4a5043e/ghostty-themes.tgz|https://github.com/mbadolato/iTerm2-Color-Schemes/releases/download/release-20260525-155808-7335c0a/ghostty-themes.tgz|' build.zig.zon.txt build.zig.zon
sed -i 's|N-V-__8AALIsAwDyo88G5mGJGN2lSVmmFMx4YePfUvp_2o3Y|N-V-__8AAGi9AwC7QV7hLqjN6iBkXA2y5dxw285nkSLlVB7I|' build.zig.zon
sed -i 's|git+https://github.com/rockorager/libvaxis#1f41c121e8fc153d9ce8c6eb64b2bbab68ad7d23|https://github.com/rockorager/libvaxis/archive/1f41c121e8fc153d9ce8c6eb64b2bbab68ad7d23.tar.gz|' build.zig.zon.txt build.zig.zon
./nix/build-support/fetch-zig-cache.sh
"$zig_bin" fetch 'git+https://github.com/TUSF/zigimg#31268548fe3276c0e95f318a6c0d2ab10565b58d' >/dev/null
"$zig_bin" fetch 'git+https://codeberg.org/atman/zg#4a002763419a34d61dcbb1f415821b83b9bf8ddc' >/dev/null
DESTDIR="$PWD/ghostty-root" "$zig_bin" build --prefix /usr --system "$ZIG_GLOBAL_CACHE_DIR/p" -Doptimize=ReleaseFast -Dcpu=baseline
%install
cp -a ghostty-root/usr/. %{buildroot}%{_prefix}/
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
