# Fedora's livesys setup creates the temporary liveuser after image build.
# Keep only live-session launchers here. KDE and Plasma consume Proper's XDG
# defaults and Global Theme directly, so they must not be copied into HOME.
if [[ "$kiwi_profiles" == *"Live"* ]]; then
cat >> /var/lib/livesys/livesys-session-extra <<'EOF'
mkdir -p /home/liveuser/.config
install -d /home/liveuser/.config/vicinae
install -m 0644 /etc/skel/.config/vicinae/settings.json /home/liveuser/.config/vicinae/settings.json
install -m 0644 /usr/share/proper-linux/live/kwalletrc /home/liveuser/.config/kwalletrc
rm -f /home/liveuser/Desktop/liveinst.desktop /home/liveuser/Desktop/Install\ to\ Hard\ Drive.desktop
mkdir -p /home/liveuser/.config/autostart
install -m 0644 /usr/share/proper-linux/live/proper-welcome.desktop /home/liveuser/.config/autostart/proper-welcome.desktop
install -m 0644 /usr/share/proper-linux/live/liveinst-setup.desktop /home/liveuser/.config/autostart/liveinst-setup.desktop
mkdir -p /home/liveuser/Desktop
install -m 0755 /usr/share/proper-linux/live/proper-install.desktop /home/liveuser/Desktop/Install\ Proper\ Linux.desktop
install -m 0644 /usr/share/proper-linux/live/proper-live-wallpaper.desktop /home/liveuser/.config/autostart/proper-live-wallpaper.desktop
chown -R liveuser:liveuser /home/liveuser/.config /home/liveuser/Desktop
EOF
fi
