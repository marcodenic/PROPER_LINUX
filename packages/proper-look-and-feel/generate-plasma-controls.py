#!/usr/bin/python3
"""Generate the supported Plasma Style controls used by system applets.

The applet QML remains upstream.  These assets only change the public Plasma
Style elements consumed by PlasmaComponents: list/view states, buttons,
line edits, switches, sliders, tabs, and separators.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


STYLE = """  <style id="current-color-scheme" type="text/css">
    .ColorScheme-Text { color: #f1f4f8; }
    .ColorScheme-Background { color: #181d25; }
    .ColorScheme-Highlight { color: #91b4ff; }
    .ColorScheme-ViewText { color: #f1f4f8; }
    .ColorScheme-ViewBackground { color: #151a22; }
    .ColorScheme-ViewHover { color: #91b4ff; }
    .ColorScheme-ViewFocus { color: #91b4ff; }
    .ColorScheme-ButtonText { color: #f1f4f8; }
    .ColorScheme-ButtonBackground { color: #232933; }
    .ColorScheme-ButtonHover { color: #91b4ff; }
    .ColorScheme-ButtonFocus { color: #91b4ff; }
    .ColorScheme-Frame { color: #a8b2c2; }
  </style>"""


def inline_map(source: str, label: str) -> dict[str, str]:
    match = re.search(rf"^{re.escape(label)}:\s*\{{([^}}]+)\}}$", source, re.MULTILINE)
    if not match:
        raise ValueError(f"missing token map: {label}")
    values: dict[str, str] = {}
    for item in match.group(1).split(","):
        key, value = item.split(":", 1)
        values[key.strip()] = value.strip().strip("'")
    return values


def document(width: int, height: int, body: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-FileCopyrightText: 2026 Proper Linux contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
{STYLE}
{body}
</svg>
"""


def rounded_frame(prefix: str, x: int, y: int, radius: int, center: int,
                  css_class: str, opacity: float, hints: bool = False) -> str:
    total = radius * 2 + center
    right = x + radius + center
    bottom = y + radius + center
    fill = f'class="{css_class}" fill="currentColor" fill-opacity="{opacity:.3f}"'
    corner = radius - 1
    elements = [
        f'  <rect id="{prefix}-center" x="{x + radius}" y="{y + radius}" width="{center}" height="{center}" {fill}/>',
        f'  <rect id="{prefix}-top" x="{x + radius}" y="{y}" width="{center}" height="{radius}" {fill}/>',
        f'  <rect id="{prefix}-bottom" x="{x + radius}" y="{bottom}" width="{center}" height="{radius}" {fill}/>',
        f'  <rect id="{prefix}-left" x="{x}" y="{y + radius}" width="{radius}" height="{center}" {fill}/>',
        f'  <rect id="{prefix}-right" x="{right}" y="{y + radius}" width="{radius}" height="{center}" {fill}/>',
        f'  <path id="{prefix}-topleft" d="M {x + radius} {y} V {y + radius} H {x} v-1 C {x} {y + radius * 0.45:.2f} {x + radius * 0.45:.2f} {y} {x + corner} {y} Z" {fill}/>',
        f'  <path id="{prefix}-topright" d="M {right} {y} V {y + radius} H {x + total} v-1 C {x + total} {y + radius * 0.45:.2f} {x + total - radius * 0.45:.2f} {y} {x + total - corner} {y} Z" {fill}/>',
        f'  <path id="{prefix}-bottomleft" d="M {x + radius} {y + total} V {bottom} H {x} v1 C {x} {y + total - radius * 0.45:.2f} {x + radius * 0.45:.2f} {y + total} {x + corner} {y + total} Z" {fill}/>',
        f'  <path id="{prefix}-bottomright" d="M {right} {y + total} V {bottom} H {x + total} v1 C {x + total} {y + total - radius * 0.45:.2f} {x + total - radius * 0.45:.2f} {y + total} {x + total - corner} {y + total} Z" {fill}/>',
    ]
    if hints:
        margin = max(3, radius - 2)
        elements.extend([
            f'  <rect id="{prefix}-hint-top-margin" x="{x + radius + center // 2}" y="{y}" width="1" height="{margin}" fill="#ff00ff"/>',
            f'  <rect id="{prefix}-hint-bottom-margin" x="{x + radius + center // 2}" y="{y + total - margin}" width="1" height="{margin}" fill="#ff00ff"/>',
            f'  <rect id="{prefix}-hint-left-margin" x="{x}" y="{y + radius + center // 2}" width="{margin}" height="1" fill="#ff00ff"/>',
            f'  <rect id="{prefix}-hint-right-margin" x="{x + total - margin}" y="{y + radius + center // 2}" width="{margin}" height="1" fill="#ff00ff"/>',
        ])
    return "\n".join(elements)


def frame_grid(states: list[tuple[str, str, float, bool]], radius: int = 9,
               center: int = 20, columns: int = 4) -> tuple[str, int, int]:
    size = radius * 2 + center
    gap = 12
    blocks: list[str] = []
    for index, (prefix, css_class, opacity, hints) in enumerate(states):
        x = (index % columns) * (size + gap)
        y = (index // columns) * (size + gap)
        blocks.append(rounded_frame(prefix, x, y, radius, center, css_class, opacity, hints))
    rows = (len(states) + columns - 1) // columns
    return "\n".join(blocks), columns * (size + gap), rows * (size + gap)


def listitem() -> str:
    states = [
        ("normal", "ColorScheme-ViewBackground", 0.001, True),
        ("hover", "ColorScheme-ViewHover", 0.090, False),
        ("pressed", "ColorScheme-ViewFocus", 0.150, True),
        ("section", "ColorScheme-ViewBackground", 0.001, True),
    ]
    frames, width, height = frame_grid(states)
    extras = f"""
  <rect id="separator" x="4" y="{height + 2}" width="32" height="1" class="ColorScheme-Frame" fill="currentColor" fill-opacity="0.120"/>
  <rect id="hint-tile-center" x="42" y="{height + 2}" width="1" height="1" fill="#ff6600"/>
"""
    return document(width, height + 8, frames + extras)


def viewitem() -> str:
    states = [
        ("normal", "ColorScheme-ViewBackground", 0.001, False),
        ("hover", "ColorScheme-ViewHover", 0.080, False),
        ("selected", "ColorScheme-ViewFocus", 0.140, False),
        ("selected+hover", "ColorScheme-ViewFocus", 0.190, False),
    ]
    frames, width, height = frame_grid(states)
    return document(width, height + 4, frames + f'\n  <rect id="hint-tile-center" x="2" y="{height + 1}" width="1" height="1" fill="#ff6600"/>')


def button() -> str:
    states = [
        ("normal", "ColorScheme-ButtonBackground", 0.720, True),
        ("hover", "ColorScheme-ButtonHover", 0.120, True),
        ("pressed", "ColorScheme-ButtonFocus", 0.210, True),
        ("focus", "ColorScheme-ButtonFocus", 0.150, True),
        ("toolbutton-hover", "ColorScheme-ButtonHover", 0.100, True),
        ("toolbutton-pressed", "ColorScheme-ButtonFocus", 0.190, True),
        ("toolbutton-focus", "ColorScheme-ButtonFocus", 0.130, True),
    ]
    frames, width, height = frame_grid(states)
    mask = rounded_frame("mask-normal", width + 4, 0, 9, 20,
                         "ColorScheme-Background", 1.0, False)
    shadow = rounded_frame("shadow", width + 54, 0, 9, 20,
                           "ColorScheme-Background", 0.001, True)
    extras = '\n  <rect id="normal-hint-compose-over-border" x="2" y="2" width="1" height="1" fill="#ff6600"/>'
    return document(width + 100, height + 4, frames + "\n" + mask + "\n" + shadow + extras)


def lineedit() -> str:
    states = [
        ("base", "ColorScheme-ButtonBackground", 0.680, True),
        ("hover", "ColorScheme-ButtonHover", 0.090, True),
        ("focus", "ColorScheme-ButtonFocus", 0.140, True),
        ("focusframe", "ColorScheme-ButtonFocus", 0.200, True),
    ]
    frames, width, height = frame_grid(states)
    extras = f'\n  <rect id="hint-focus-over-base" x="2" y="{height + 1}" width="1" height="1" fill="#ff6600"/>\n  <rect id="hint-tile-center" x="5" y="{height + 1}" width="1" height="1" fill="#ff6600"/>'
    return document(width, height + 5, frames + extras)


def horizontal_frame(prefix: str, x: int, y: int, css_class: str, opacity: float) -> str:
    fill = f'class="{css_class}" fill="currentColor" fill-opacity="{opacity:.3f}"'
    return "\n".join([
        f'  <rect id="{prefix}-center" x="{x + 3}" y="{y + 1}" width="24" height="4" {fill}/>',
        f'  <rect id="{prefix}-left" x="{x}" y="{y + 1}" width="3" height="4" rx="2" {fill}/>',
        f'  <rect id="{prefix}-right" x="{x + 27}" y="{y + 1}" width="3" height="4" rx="2" {fill}/>',
        f'  <rect id="{prefix}-top" x="{x + 3}" y="{y}" width="24" height="1" {fill}/>',
        f'  <rect id="{prefix}-bottom" x="{x + 3}" y="{y + 5}" width="24" height="1" {fill}/>',
        f'  <rect id="{prefix}-topleft" x="{x}" y="{y}" width="3" height="1" rx="1" {fill}/>',
        f'  <rect id="{prefix}-topright" x="{x + 27}" y="{y}" width="3" height="1" rx="1" {fill}/>',
        f'  <rect id="{prefix}-bottomleft" x="{x}" y="{y + 5}" width="3" height="1" rx="1" {fill}/>',
        f'  <rect id="{prefix}-bottomright" x="{x + 27}" y="{y + 5}" width="3" height="1" rx="1" {fill}/>',
    ])


def slider() -> str:
    parts = [
        horizontal_frame("groove", 0, 4, "ColorScheme-Frame", 0.240),
        horizontal_frame("groove-highlight", 38, 4, "ColorScheme-Highlight", 0.900),
    ]
    handle_states = [
        ("horizontal-slider-shadow", 8, "ColorScheme-Background", 0.420, 18),
        ("horizontal-slider-handle", 30, "ColorScheme-Highlight", 0.950, 16),
        ("horizontal-slider-hover", 52, "ColorScheme-Highlight", 1.000, 18),
        ("horizontal-slider-focus", 76, "ColorScheme-Highlight", 0.260, 20),
        ("vertical-slider-shadow", 102, "ColorScheme-Background", 0.420, 18),
        ("vertical-slider-handle", 124, "ColorScheme-Highlight", 0.950, 16),
        ("vertical-slider-hover", 146, "ColorScheme-Highlight", 1.000, 18),
        ("vertical-slider-focus", 170, "ColorScheme-Highlight", 0.260, 20),
    ]
    for element_id, x, css_class, opacity, size in handle_states:
        parts.append(f'  <circle id="{element_id}" cx="{x + 10}" cy="35" r="{size / 2:.1f}" class="{css_class}" fill="currentColor" fill-opacity="{opacity:.3f}"/>')
    parts.extend([
        '  <rect id="hint-handle-size" x="202" y="25" width="20" height="20" fill="#ff00ff" fill-opacity="0.001"/>',
        '  <rect id="hint-tile-center" x="224" y="25" width="1" height="1" fill="#ff6600"/>',
        '  <circle id="shadow" cx="236" cy="35" r="10" fill="#000000" fill-opacity="0.001"/>',
    ])
    return document(248, 50, "\n".join(parts))


def switch() -> str:
    parts = [
        # Plasma's Switch expects Breeze-compatible 38x16 bar and 22x22
        # handle geometry. Keeping those contracts avoids compressed handles
        # and misaligned labels in Networks and Airplane Mode.
        '  <rect id="inactive-left" x="0" y="0" width="8" height="16" rx="8" class="ColorScheme-Frame" fill="currentColor" fill-opacity="0.240"/>',
        '  <rect id="inactive-center" x="8" y="0" width="22" height="16" class="ColorScheme-Frame" fill="currentColor" fill-opacity="0.240"/>',
        '  <rect id="inactive-right" x="30" y="0" width="8" height="16" rx="8" class="ColorScheme-Frame" fill="currentColor" fill-opacity="0.240"/>',
        '  <rect id="active-left" x="44" y="0" width="8" height="16" rx="8" class="ColorScheme-Highlight" fill="currentColor" fill-opacity="0.900"/>',
        '  <rect id="active-center" x="52" y="0" width="22" height="16" class="ColorScheme-Highlight" fill="currentColor" fill-opacity="0.900"/>',
        '  <rect id="active-right" x="74" y="0" width="8" height="16" rx="8" class="ColorScheme-Highlight" fill="currentColor" fill-opacity="0.900"/>',
        '  <circle id="handle-shadow" cx="13" cy="39" r="13" fill="#000000" fill-opacity="0.220"/>',
        '  <circle id="handle" cx="43" cy="39" r="11" class="ColorScheme-ButtonText" fill="currentColor" fill-opacity="0.980"/>',
        '  <circle id="handle-hover" cx="69" cy="39" r="11" class="ColorScheme-ButtonFocus" fill="currentColor"/>',
        '  <circle id="handle-focus" cx="97" cy="39" r="13" class="ColorScheme-Highlight" fill="currentColor" fill-opacity="0.260"/>',
        '  <circle id="handle-pressed" cx="125" cy="39" r="11" class="ColorScheme-ButtonText" fill="currentColor" fill-opacity="0.880"/>',
        '  <rect id="hint-bar-size" x="142" y="31" width="38" height="16" fill="#ff00ff" fill-opacity="0.001"/>',
        '  <rect id="hint-stretch-borders" x="184" y="31" width="4" height="4" fill="#ff6600"/>',
    ]
    return document(192, 56, "\n".join(parts))


def tab_frame(prefix: str, x: int, y: int, edge: str) -> str:
    size = 34
    elements = rounded_frame(prefix, x, y, 5, 24, "ColorScheme-Background", 0.001, True)
    positions = {
        "bottom": (x + 5, y + size - 2, 24, 2),
        "top": (x + 5, y, 24, 2),
        "left": (x, y + 5, 2, 24),
        "right": (x + size - 2, y + 5, 2, 24),
    }
    px, py, width, height = positions[edge]
    elements += f'\n  <rect x="{px}" y="{py}" width="{width}" height="{height}" rx="1" class="ColorScheme-Highlight" fill="currentColor" fill-opacity="0.950"/>'
    return elements


def tabbar() -> str:
    parts = [
        tab_frame("north-active-tab", 0, 0, "bottom"),
        tab_frame("south-active-tab", 46, 0, "top"),
        tab_frame("east-active-tab", 92, 0, "left"),
        tab_frame("west-active-tab", 138, 0, "right"),
        '  <rect id="hint-tile-center" x="178" y="2" width="1" height="1" fill="#ff6600"/>',
    ]
    return document(184, 38, "\n".join(parts))


def line() -> str:
    body = """  <rect id="horizontal-line" x="0" y="0" width="24" height="1" class="ColorScheme-Frame" fill="currentColor" fill-opacity="0.120"/>
  <rect id="vertical-line" x="26" y="0" width="1" height="24" class="ColorScheme-Frame" fill="currentColor" fill-opacity="0.120"/>"""
    return document(28, 24, body)


GENERATORS = {
    "button.svg": button,
    "line.svg": line,
    "lineedit.svg": lineedit,
    "listitem.svg": listitem,
    "slider.svg": slider,
    "switch.svg": switch,
    "tabbar.svg": tabbar,
    "viewitem.svg": viewitem,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tokens", type=Path)
    parser.add_argument("output", type=Path)
    arguments = parser.parse_args()

    source = arguments.tokens.read_text(encoding="utf-8")
    radius = inline_map(source, "radius")
    if int(radius["control"]) != 9:
        raise ValueError("control SVGs are reviewed for the 9px Proper radius")

    arguments.output.mkdir(parents=True, exist_ok=True)
    for filename, generator in GENERATORS.items():
        (arguments.output / filename).write_text(generator(), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
