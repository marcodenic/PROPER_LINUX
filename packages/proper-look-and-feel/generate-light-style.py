#!/usr/bin/python3
"""Derive the light Plasma Style from the same Proper geometry and tokens."""
# SPDX-License-Identifier: GPL-3.0-or-later
import argparse
import importlib.util
import json
import re
import shutil
from pathlib import Path


def colour_map(tokens):
    spec = importlib.util.spec_from_file_location("semantic", Path(__file__).with_name("generate-semantic-assets.py"))
    semantic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(semantic)
    source = tokens.read_text()
    dark = semantic.inline_map(source, "dark", "  ")
    light = semantic.inline_map(source, "light", "  ")
    material = semantic.inline_map(source, "material")
    colours = {value: light[key] for key, value in dark.items()}
    colours.update({material["panel_tint"]: light["base"],
                    material["panel_dense"]: light["surface"],
                    material["panel_edge"]: light["muted"]})
    return colours


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tokens", type=Path)
    parser.add_argument("source", type=Path)
    parser.add_argument("colours", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    colours = colour_map(args.tokens)
    shutil.copytree(args.source, args.output, dirs_exist_ok=True)
    for asset in args.output.rglob("*.svg"):
        asset.write_text(re.sub(r"#[0-9a-fA-F]{6}\b", lambda m: colours.get(m[0].lower(), m[0]), asset.read_text()))
    shutil.copyfile(args.colours, args.output / "colors")
    metadata = json.loads((args.output / "metadata.json").read_text())
    metadata["KPlugin"].update(Id="proper-light", Name="Proper Light")
    (args.output / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    settings = args.output / "plasmarc"
    settings.write_text(settings.read_text().replace("contrast=0.72", "contrast=1.0").replace("intensity=0.82", "intensity=1.0").replace("saturation=1.15", "saturation=1.0"))


if __name__ == "__main__":
    main()
