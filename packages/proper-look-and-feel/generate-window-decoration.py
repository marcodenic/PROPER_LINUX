#!/usr/bin/python3
"""Original borderless, blurred title bars for KDE Aurorae 6.7's SVG engine."""
# SPDX-License-Identifier: GPL-3.0-or-later
import argparse
import importlib.util
from pathlib import Path


def frame(prefix, colour, opacity):
    shapes = {
        'center': '<rect x="8" y="8" width="32" height="32"/>',
        'top': '<rect x="8" width="32" height="8"/>',
        'bottom': '<rect x="8" y="40" width="32" height="8"/>',
        'left': '<rect y="8" width="8" height="32"/>',
        'right': '<rect x="40" y="8" width="8" height="32"/>',
        'topleft': '<path d="M8 0A8 8 0 0 0 0 8H8Z"/>',
        'topright': '<path d="M40 0A8 8 0 0 1 48 8H40Z"/>',
        'bottomleft': '<path d="M0 40A8 8 0 0 0 8 48V40Z"/>',
        'bottomright': '<path d="M48 40A8 8 0 0 1 40 48V40Z"/>',
    }
    return '\n'.join(f'<g id="{prefix}-{name}" fill="{colour}" opacity="{opacity}">{shape}</g>' for name, shape in shapes.items())


def svg(content):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">\n' + content + '\n</svg>\n'


def button(path, colour):
    states = {'active': 0, 'inactive': 0, 'hover': .12, 'hover-inactive': .12, 'pressed': .22}
    return svg('\n'.join(
        f'<g id="{state}-center"><rect width="28" height="24" rx="6" fill="{colour}" fill-opacity="{opacity}"/>'
        f'<path d="{path}" fill="none" stroke="{colour}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></g>'
        for state, opacity in states.items()))


def write_theme(output, palette, name):
    target = output / name
    target.mkdir(parents=True, exist_ok=True)
    (target / 'decoration.svg').write_text(svg(frame('decoration', palette['base'], .66) + frame('mask', '#ffffff', 1)))
    paths = {'minimize': 'M9 15H19', 'maximize': 'M9 7H19V17H9Z', 'restore': 'M11 7H20V15M8 10H17V19H8Z',
             'close': 'M9 7L19 17M19 7L9 17', 'menu': 'M9 8H19M9 12H19M9 16H19',
             'appmenu': 'M9 8H19M9 12H19M9 16H19', 'alldesktops': 'M9 7H19V17H9ZM14 7V17M9 12H19',
             'keepabove': 'M9 14L14 9L19 14M9 7H19', 'keepbelow': 'M9 10L14 15L19 10M9 17H19',
             'shade': 'M9 15L14 10L19 15', 'help': 'M11 9C11 5 18 5 18 9C18 12 14 11 14 14M14 18V18.1'}
    for key, path in paths.items():
        (target / (key + '.svg')).write_text(button(path, palette['text']))
    (target / (name + 'rc')).write_text(f'''[General]
ActiveTextColor={palette['text']}
InactiveTextColor={palette['muted']}
TitleAlignment=Center
Animation=120
[Layout]
BorderLeft=0
BorderRight=0
BorderBottom=0
BorderTop=0
TitleHeight=24
TitleEdgeTop=4
TitleEdgeBottom=4
TitleEdgeLeft=6
TitleEdgeRight=6
TitleEdgeTopMaximized=4
TitleEdgeBottomMaximized=4
TitleEdgeLeftMaximized=6
TitleEdgeRightMaximized=6
TitleBorderLeft=8
TitleBorderRight=8
ButtonWidth=28
ButtonHeight=24
ButtonSpacing=2
PaddingLeft=0
PaddingRight=0
PaddingTop=0
PaddingBottom=0
''')
    (target / 'metadata.desktop').write_text(f'[Desktop Entry]\nName={name.replace("-", " ").title()}\nX-KDE-PluginInfo-Name={name}\nX-KDE-PluginInfo-License=GPL-3.0-or-later\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('tokens', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('semantic', Path(__file__).with_name('generate-semantic-assets.py'))
    semantic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(semantic)
    source = args.tokens.read_text()
    for variant in ('dark', 'light', 'midnight'):
        write_theme(args.output, semantic.inline_map(source, variant, '  '), 'proper-' + variant)


if __name__ == '__main__':
    main()
