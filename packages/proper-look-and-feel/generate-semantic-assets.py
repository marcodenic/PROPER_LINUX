#!/usr/bin/python3
"""Generate cross-surface assets from Proper's canonical semantic tokens."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def inline_map(source: str, label: str, indent: str = "") -> dict[str, str]:
    match = re.search(rf"^{re.escape(indent + label)}:\s*\{{([^}}]+)\}}$", source, re.MULTILINE)
    if not match:
        raise ValueError(f"missing token map: {label}")
    values: dict[str, str] = {}
    for item in match.group(1).split(","):
        key, value = item.split(":", 1)
        values[key.strip()] = value.strip().strip("'")
    return values


def rgb_tuple(colour: str) -> tuple[int, int, int]:
    value = colour.removeprefix("#")
    if not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        raise ValueError(f"invalid colour token: {colour}")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))


def rgb(colour: str) -> str:
    return ",".join(str(channel) for channel in rgb_tuple(colour))


def mix(first: str, second: str, amount: float) -> str:
    left = rgb_tuple(first)
    right = rgb_tuple(second)
    channels = tuple(round(a * (1 - amount) + b * amount) for a, b in zip(left, right))
    return "#" + "".join(f"{channel:02x}" for channel in channels)


def colour_scheme(identifier: str, name: str, palette: dict[str, str], contrast: int,
                  material: dict[str, str]) -> str:
    foreground = {
        "ForegroundInactive": rgb(palette["muted"]),
        "ForegroundLink": rgb(palette["accent"]),
        "ForegroundNegative": rgb(palette["urgent"]),
        "ForegroundNeutral": rgb(palette["warning"]),
        "ForegroundNormal": rgb(palette["text"]),
        "ForegroundPositive": rgb(palette["positive"]),
        "ForegroundVisited": rgb(palette["visited"]),
    }

    def section(title: str, background: str, alternate: str) -> str:
        entries = {
            "BackgroundAlternate": rgb(alternate),
            "BackgroundNormal": rgb(background),
            **foreground,
        }
        return f"[{title}]\n" + "\n".join(f"{key}={value}" for key, value in entries.items())

    selection_foreground = rgb(palette["on_accent"])
    selection = {
        "BackgroundAlternate": rgb(mix(palette["selection"], palette["text"], 0.08)),
        "BackgroundNormal": rgb(palette["selection"]),
        "ForegroundActive": selection_foreground,
        "ForegroundInactive": rgb(mix(palette["on_accent"], palette["selection"], 0.18)),
        "ForegroundLink": selection_foreground,
        "ForegroundNegative": selection_foreground,
        "ForegroundNeutral": selection_foreground,
        "ForegroundNormal": selection_foreground,
        "ForegroundPositive": selection_foreground,
        "ForegroundVisited": selection_foreground,
    }
    effects = f"""[ColorEffects:Disabled]
Color={rgb(palette['muted'])}
ColorAmount=0
ColorEffect=0
ContrastAmount=0.65
ContrastEffect=1
IntensityAmount=0.1
IntensityEffect=2

[ColorEffects:Inactive]
ChangeSelectionColor=true
Color={rgb(palette['muted'])}
ColorAmount=0.025
ColorEffect=2
ContrastAmount=0.1
ContrastEffect=2
Enable=false
IntensityAmount=0
IntensityEffect=0"""
    dark_header = identifier != "ProperLight"
    header_background = material["panel_tint"] if dark_header else palette["surface_alt"]
    header_alternate = material["panel_dense"] if dark_header else palette["surface"]
    sections = [
        section("Colors:Button", palette["surface_alt"], mix(palette["surface_alt"], palette["text"], 0.05)),
        section("Colors:Complementary", palette["base"], palette["view_alt"]),
        section("Colors:Header", header_background, header_alternate),
        section("Colors:Header][Inactive", header_alternate, palette["view_alt"]),
        "[Colors:Selection]\n" + "\n".join(f"{key}={value}" for key, value in selection.items()),
        section("Colors:Tooltip", palette["surface"], palette["surface_alt"]),
        section("Colors:View", palette["view"], palette["view_alt"]),
        section("Colors:Window", palette["surface"], palette["surface_alt"]),
    ]
    return "\n\n".join([
        effects,
        *sections,
        f"[General]\nColorScheme={identifier}\nName={name}\nshadeSortColumn=true",
        f"[KDE]\ncontrast={contrast}",
        "[WM]\n"
        f"activeBackground={rgb(palette['surface_alt'])}\n"
        f"activeBlend={rgb(palette['text'])}\n"
        f"activeForeground={rgb(palette['text'])}\n"
        f"inactiveBackground={rgb(palette['surface'])}\n"
        f"inactiveBlend={rgb(palette['muted'])}\n"
        f"inactiveForeground={rgb(palette['muted'])}",
    ]) + "\n"


def qml_tokens(palette: dict[str, str], radius: dict[str, str], spacing: dict[str, str],
               animation: dict[str, str], typography: dict[str, str],
               welcome: dict[str, str]) -> str:
    properties = "\n".join(
        f'    readonly property color {key}: "{value}"'
        for key, value in palette.items()
    )
    return f'''// Generated from tokens.yaml; do not edit.
// SPDX-License-Identifier: GPL-2.0-or-later
import QtQuick

QtObject {{
{properties}
    readonly property int controlRadius: {radius["control"]}
    readonly property int spacingUnit: {spacing["unit"]}
    readonly property int spacingItem: {spacing["item"]}
    readonly property int spacingSection: {spacing["section"]}
    readonly property int animationFast: {animation["fast"]}
    readonly property int animationNormal: {animation["normal"]}
    readonly property string uiFont: "{typography["ui"]}"
    readonly property color arrivalBase: "{welcome["base"]}"
    readonly property color arrivalWordmark: "{welcome["wordmark"]}"

    function alpha(colour, value) {{
        return Qt.rgba(colour.r, colour.g, colour.b, value)
    }}
}}
'''


def installer_css(palette: dict[str, str]) -> str:
    return f'''/* Generated from tokens.yaml; do not edit. */
@define-color proper_background {palette["base"]};
@define-color proper_surface {palette["surface"]};
@define-color proper_foreground {palette["text"]};
@define-color proper_accent {palette["accent"]};

.logo-sidebar {{
    background-image: none;
    background-color: @proper_background;
}}

.logo {{
    background-image: url('/usr/share/proper-linux/identity/proper-wordmark.svg');
    background-position: 50% 28px;
    background-repeat: no-repeat;
    background-size: 220px auto;
    background-color: transparent;
}}

.product-logo {{
    background-image: none;
    background-color: transparent;
}}

AnacondaSpokeWindow #nav-box {{
    background-color: @proper_background;
    background-image: none;
    color: @proper_foreground;
}}

AnacondaSpokeWindow #nav-box GtkButton:checked {{
    border-color: @proper_accent;
}}
'''


def vicinae_theme(name: str, variant: str, palette: dict[str, str],
                  material: dict[str, str], opacity: dict[str, str]) -> str:
    """Render Vicinae's supported TOML theme from Proper's semantic tokens."""
    background = material["panel_tint"] if variant == "dark" else palette["base"]
    border = mix(background, material["panel_edge"], float(opacity["panel_edge"]))
    return f'''# Generated from tokens.yaml; do not edit.
[meta]
version = 1
name = "{name}"
description = "Proper Horizon launcher surfaces"
variant = "{variant}"
inherits = "vicinae-{variant}"

[colors.core]
background = "{background}"
foreground = "{palette["text"]}"
secondary_background = "{palette["surface_alt"]}"
border = "{border}"
accent = "{palette["accent"]}"
accent_foreground = "{palette["on_accent"]}"

[colors.main_window]
border = "{border}"

[colors.main_window.footer]
background = "{palette["surface_alt"]}"

[colors.text]
default = "{palette["text"]}"
muted = "{palette["muted"]}"
danger = "{palette["urgent"]}"
success = "{palette["positive"]}"
placeholder = "{palette["muted"]}"

[colors.text.links]
default = "{palette["accent"]}"
visited = "{palette["visited"]}"

[colors.text.selection]
background = "{palette["selection"]}"
foreground = "{palette["on_accent"]}"

[colors.input]
background = "{palette["view_alt"]}"
border = "{border}"
border_focus = "{palette["accent"]}"
border_error = "{palette["urgent"]}"

[colors.list.item.hover]
background = "{palette["view_alt"]}"
foreground = "{palette["text"]}"

[colors.list.item.selection]
background = "{palette["selection"]}"
foreground = "{palette["text"]}"
secondary_background = "{palette["surface_alt"]}"
secondary_foreground = "{palette["muted"]}"

[colors.grid.item]
background = "{palette["surface_alt"]}"
selection_outline = "{palette["accent"]}"
hover_outline = "{palette["muted"]}"

[colors.accents]
blue = "{palette["accent"]}"
green = "{palette["positive"]}"
magenta = "{palette["visited"]}"
orange = "{palette["warning"]}"
purple = "{palette["visited"]}"
red = "{palette["urgent"]}"
yellow = "{palette["warning"]}"
cyan = "{palette["accent"]}"
'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tokens", type=Path)
    parser.add_argument("output", type=Path)
    arguments = parser.parse_args()

    source = arguments.tokens.read_text(encoding="utf-8")
    palettes = {name: inline_map(source, name, "  ") for name in ("light", "dark", "midnight")}
    radius = inline_map(source, "radius")
    spacing = inline_map(source, "spacing")
    animation = inline_map(source, "animation")
    typography = inline_map(source, "typography")
    welcome = inline_map(source, "welcome")
    contrast = inline_map(source, "contrast")
    material = inline_map(source, "material")
    opacity = inline_map(source, "opacity")

    required = {"base", "surface", "surface_alt", "view", "view_alt", "text", "muted", "accent", "selection", "on_accent", "positive", "warning", "urgent", "visited", "border"}
    for name, palette in palettes.items():
        missing = required - palette.keys()
        if missing:
            raise ValueError(f"{name} palette is missing: {', '.join(sorted(missing))}")

    arguments.output.mkdir(parents=True, exist_ok=True)
    (arguments.output / "Proper.colors").write_text(
        colour_scheme("Proper", "Proper", palettes["dark"], int(contrast["kde"]), material), encoding="utf-8"
    )
    (arguments.output / "ProperLight.colors").write_text(
        colour_scheme("ProperLight", "Proper Light", palettes["light"], int(contrast["kde"]), material), encoding="utf-8"
    )
    (arguments.output / "ProperMidnight.colors").write_text(
        colour_scheme("ProperMidnight", "Proper Midnight", palettes["midnight"], int(contrast["kde_midnight"]), material), encoding="utf-8"
    )
    (arguments.output / "ProperTokens.qml").write_text(
        qml_tokens(palettes["dark"], radius, spacing, animation, typography, welcome), encoding="utf-8"
    )
    (arguments.output / "proper-anaconda.css").write_text(installer_css(palettes["dark"]), encoding="utf-8")
    (arguments.output / "proper-dark.toml").write_text(
        vicinae_theme("Proper Horizon", "dark", palettes["dark"], material, opacity), encoding="utf-8"
    )
    (arguments.output / "proper-light.toml").write_text(
        vicinae_theme("Proper Horizon Light", "light", palettes["light"], material, opacity), encoding="utf-8"
    )
    (arguments.output / "proper-palette.json").write_text(
        json.dumps({"version": 2, "colour": palettes, "welcome": welcome}, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
