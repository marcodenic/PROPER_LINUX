# Ghostty presentation

Proper seeds `ghostty.conf` into new users' Ghostty configuration through
`/etc/skel`. Package updates preserve existing user choices. The installed
review VM was changed explicitly following product-manager approval.

The approved material uses 50% background opacity and native compositor blur.
Text remains sharp; the compositor blurs the scene behind the terminal.
Ghostty 1.3.1 ignores numeric blur intensity under Plasma: `true` requests
KWin's shared strength. Do not claim a terminal-specific radius or lower the
shared desktop blur to adjust Ghostty alone. If compositor blur is disabled,
Ghostty retains its configured transparency without blur.

The existing `ghostty-ext-background-effect.patch` supplies the protocol
integration for the shipped Plasma version. This default change needs no
additional terminal or compositor patch. Native configuration reference:
https://ghostty.org/docs/config/reference#background-blur
