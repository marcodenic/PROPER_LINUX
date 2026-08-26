# Fedora's livesys setup creates the temporary liveuser after image build.
# Seed only Proper's two default fragments after the KDE live hook has run;
# installed accounts continue to receive the same files from /etc/skel.
if [[ "$kiwi_profiles" == *"Live"* ]]; then
cat >> /var/lib/livesys/livesys-session-extra <<'EOF'
mkdir -p /home/liveuser/.config
install -m 0644 /etc/skel/.config/kdeglobals /home/liveuser/.config/kdeglobals
install -m 0644 /etc/skel/.config/plasma-org.kde.plasma.desktop-appletsrc /home/liveuser/.config/plasma-org.kde.plasma.desktop-appletsrc
install -m 0644 /etc/skel/.config/plasmashellrc /home/liveuser/.config/plasmashellrc
install -m 0644 /etc/skel/.config/kglobalshortcutsrc /home/liveuser/.config/kglobalshortcutsrc
install -d /home/liveuser/.config/vicinae
install -m 0644 /etc/skel/.config/vicinae/vicinae.toml /home/liveuser/.config/vicinae/vicinae.toml
rm -f /home/liveuser/Desktop/liveinst.desktop /home/liveuser/Desktop/Install\ to\ Hard\ Drive.desktop
mkdir -p /home/liveuser/.config/autostart
cat > /home/liveuser/.config/autostart/proper-live-wallpaper.desktop <<'DESKTOP'
[Desktop Entry]
Type=Application
Name=Proper live wallpaper
Exec=/usr/bin/plasma-apply-wallpaperimage /usr/share/wallpapers/ProperHorizon/contents/images/1920x1080.png
OnlyShowIn=KDE;
X-KDE-autostart-after=panel
DESKTOP
EOF
fi
