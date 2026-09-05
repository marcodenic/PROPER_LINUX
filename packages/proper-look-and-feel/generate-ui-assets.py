#!/usr/bin/python3
"""Generate first-party UI styles from Proper's canonical design tokens."""

from __future__ import annotations

import argparse
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


def rgb(colour: str) -> tuple[int, int, int]:
    value = colour.removeprefix("#")
    if not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        raise ValueError(f"invalid colour token: {colour}")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))


def rgba(colour: str, alpha: float) -> str:
    red, green, blue = rgb(colour)
    return f"rgba({red}, {green}, {blue}, {alpha:.3f})"


def widget_qss(palette: dict[str, str], radius: dict[str, str], spacing: dict[str, str], typography: dict[str, str]) -> str:
    base = palette["base"]
    surface = palette["surface"]
    text = palette["text"]
    muted = palette["muted"]
    accent = palette["accent"]
    urgent = palette["urgent"]
    control_radius = int(radius["control"])
    popup_radius = radius["popup"]
    unit = int(spacing["unit"])
    ui_font = typography["ui"]
    # Qt style sheets accept one family name here. Qt/fontconfig supplies the
    # configured Noto Sans fallback when Inter has no glyph for a character.
    qss_font = f'"{ui_font}"'

    return f"""/* Generated from tokens.yaml; do not edit. */
QWidget#properRoot {{ background: {base}; color: {text}; font-family: {qss_font}; }}
QWidget#properRoot QWidget {{ font-family: {qss_font}; }}
QWidget#properRoot QLabel {{ color: {text}; }}
QWidget#properRoot QLabel#subtitle,
QWidget#properRoot QLabel#countLabel,
QWidget#properRoot QLabel#cardDescription,
QWidget#properRoot QLabel#sectionCopy,
QWidget#properRoot QLabel#status,
QWidget#properRoot QLabel#guideCopy,
QWidget#properRoot QLabel#guideFooter {{ color: {muted}; }}
QWidget#properRoot QLabel#guideEyebrow,
QWidget#properRoot QLabel#guideSectionLabel {{ color: {accent}; font-size: 10px; font-weight: 700; letter-spacing: 1px; }}
QWidget#properRoot QLabel#guideCardTitle {{ color: {text}; font-size: 15px; font-weight: 650; }}
QWidget#properRoot QLabel#shortcutAction {{ color: {muted}; font-size: 12px; }}
QWidget#properRoot QLabel#keyJoin {{ color: {muted}; font-size: 10px; }}
QWidget#properRoot QLabel#keycap {{
    color: {text}; background: {rgba(muted, 0.100)}; border: 1px solid {rgba(muted, 0.300)};
    border-bottom: 2px solid {rgba(muted, 0.380)}; border-radius: 6px;
    min-width: 18px; min-height: 18px; padding: 1px 5px; font-family: "{typography['mono']}"; font-size: 10px; font-weight: 650;
}}
QWidget#properRoot QLabel#principlePill {{
    color: {muted}; background: {rgba(accent, 0.065)}; border: 1px solid {rgba(accent, 0.170)};
    border-radius: {control_radius}px; padding: 7px 8px; font-size: 9px; font-weight: 700;
}}
QWidget#properRoot QFrame#guideHero {{
    background: {rgba(accent, 0.055)}; border: 1px solid {rgba(accent, 0.180)}; border-radius: {popup_radius}px;
}}
QWidget#properRoot QFrame#guideCard,
QWidget#properRoot QFrame#shortcutPanel {{
    background: {surface}; border: 1px solid {rgba(muted, 0.160)}; border-radius: {popup_radius}px;
}}
QWidget#properRoot QFrame#guideCard:hover {{ border-color: {rgba(accent, 0.360)}; background: {rgba(accent, 0.055)}; }}
QWidget#properRoot QLabel#guideIcon {{
    background: {rgba(accent, 0.095)}; border: 1px solid {rgba(accent, 0.170)}; border-radius: 12px;
}}
QWidget#properRoot QFrame#shortcutHint,
QWidget#properRoot QFrame#shortcutLine {{ background: transparent; border: 0; }}
QDialog, QMessageBox {{ background: {base}; color: {text}; font-family: {qss_font}; }}
QDialog QLabel, QMessageBox QLabel {{ color: {text}; }}
QWidget#properRoot QLabel#cardTitle {{ font-size: 16px; font-weight: 650; }}
QWidget#properRoot QLabel#sectionTitle {{ font-size: 19px; font-weight: 650; }}
QWidget#properRoot QLabel#categoryPill {{
    color: {muted}; background: {rgba(accent, 0.100)};
    border: 1px solid {rgba(accent, 0.220)}; border-radius: {control_radius}px;
    padding: 3px 7px; font-size: 9px; font-weight: 700;
}}
QWidget#properRoot QLineEdit,
QWidget#properRoot QComboBox {{
    background: {surface}; color: {text}; border: 1px solid {rgba(muted, 0.240)};
    border-radius: {control_radius}px;
    selection-background-color: {accent}; selection-color: {base};
}}
QWidget#properRoot QLineEdit {{ padding: {unit * 2}px {unit * 3}px; }}
QWidget#properRoot QComboBox {{ padding: {unit * 2}px 40px {unit * 2}px {unit * 3}px; }}
QWidget#properRoot QLineEdit:focus,
QWidget#properRoot QComboBox:focus {{ border: 2px solid {accent}; }}
QWidget#properRoot QComboBox::drop-down {{
    subcontrol-origin: border; subcontrol-position: top right; width: 32px;
    border: 0; border-left: 1px solid {rgba(muted, 0.180)};
    border-top-right-radius: {control_radius - 1}px;
    border-bottom-right-radius: {control_radius - 1}px;
    background: {rgba(muted, 0.070)};
}}
QWidget#properRoot QComboBox::drop-down:hover {{ background: {rgba(accent, 0.120)}; }}
QWidget#properRoot QComboBox::down-arrow {{ width: 10px; height: 7px; }}
QWidget#properRoot QComboBox QAbstractItemView {{
    background: {surface}; color: {text}; selection-background-color: {rgba(accent, 0.260)};
}}
QWidget#properRoot QToolButton {{
    background: {surface}; color: {text}; border: 1px solid {rgba(muted, 0.180)};
    border-radius: {popup_radius}px; padding: {unit * 2}px; font-size: 14px;
}}
QWidget#properRoot QToolButton:hover {{
    background: {rgba(accent, 0.120)}; border-color: {rgba(accent, 0.440)};
}}
QWidget#properRoot QToolButton:checked {{
    background: {rgba(accent, 0.160)}; border: 2px solid {accent}; color: {text};
}}
QWidget#properRoot QToolButton#navButton {{
    color: {muted}; background: transparent; border: 0; border-radius: {control_radius}px;
    padding: {unit * 2}px {unit * 4}px; font-weight: 600;
}}
QWidget#properRoot QToolButton#navButton:hover {{ background: {rgba(accent, 0.080)}; color: {text}; }}
QWidget#properRoot QToolButton#navButton:checked {{ background: {rgba(accent, 0.160)}; color: {text}; }}
QWidget#properRoot QToolButton#quietButton {{ color: {muted}; background: transparent; border: 0; padding: 6px 2px; }}
QWidget#properRoot QToolButton#quietButton:hover {{ color: {text}; text-decoration: underline; }}
QWidget#properRoot QToolButton#textPreset {{ min-height: 54px; text-align: left; padding: 8px 14px; }}
QWidget#properRoot QFrame#appCard {{
    background: {surface}; border: 1px solid {rgba(muted, 0.170)}; border-radius: {popup_radius}px;
}}
QWidget#properRoot QFrame#appCard:hover {{ background: {rgba(accent, 0.075)}; border-color: {rgba(accent, 0.300)}; }}
QWidget#properRoot QPushButton {{
    background: {rgba(muted, 0.120)}; color: {text}; border: 1px solid {rgba(muted, 0.200)};
    border-radius: {control_radius}px; min-height: 38px; padding: 0 {unit * 4}px; font-weight: 600;
}}
QWidget#properRoot QPushButton:hover {{ background: {rgba(accent, 0.160)}; border-color: {rgba(accent, 0.420)}; }}
QWidget#properRoot QPushButton:focus {{ border: 2px solid {accent}; }}
QWidget#properRoot QPushButton#primary,
QWidget#properRoot QPushButton#primaryButton {{ background: {accent}; color: {base}; border-color: {accent}; }}
QWidget#properRoot QPushButton#primary:hover,
QWidget#properRoot QPushButton#primaryButton:hover {{ background: {rgba(accent, 0.860)}; }}
QWidget#properRoot QPushButton#secondaryButton {{ background: {rgba(muted, 0.120)}; color: {text}; }}
QWidget#properRoot QPushButton#cardAction {{ min-width: 58px; min-height: 30px; padding: 0 12px; }}
QWidget#properRoot QPushButton:disabled {{ color: {rgba(muted, 0.650)}; background: {rgba(surface, 0.700)}; }}
QWidget#properRoot QScrollArea,
QWidget#properRoot QScrollArea > QWidget > QWidget {{ background: transparent; border: 0; }}
QWidget#properRoot QScrollBar:vertical {{ background: transparent; width: 10px; margin: 2px; }}
QWidget#properRoot QScrollBar::handle:vertical {{ background: {rgba(muted, 0.300)}; min-height: 34px; border-radius: 4px; }}
QWidget#properRoot QScrollBar::handle:vertical:hover {{ background: {rgba(accent, 0.450)}; }}
QWidget#properRoot QScrollBar::add-line:vertical,
QWidget#properRoot QScrollBar::sub-line:vertical {{ height: 0; }}
QWidget#properRoot QScrollBar::add-page:vertical,
QWidget#properRoot QScrollBar::sub-page:vertical {{ background: transparent; }}
QWidget#properRoot QProgressBar {{ border: 0; border-radius: 3px; background: {rgba(muted, 0.180)}; min-height: 6px; max-height: 6px; }}
QWidget#properRoot QProgressBar::chunk {{ border-radius: 3px; background: {accent}; }}
QWidget#properRoot QLabel#banner {{ background: {rgba(accent, 0.110)}; color: {text}; border: 1px solid {rgba(accent, 0.300)}; border-radius: {control_radius}px; padding: 10px 13px; }}
QWidget#properRoot QLabel#errorBanner {{ background: {rgba(urgent, 0.110)}; color: {text}; border: 1px solid {rgba(urgent, 0.400)}; border-radius: {control_radius}px; padding: 10px 13px; }}
QWidget#properRoot QTextBrowser {{ background: {surface}; color: {text}; border: 1px solid {rgba(muted, 0.200)}; border-radius: {control_radius}px; padding: 8px; }}
"""


def welcome_qss(palette: dict[str, str], radius: dict[str, str], typography: dict[str, str]) -> str:
    base = palette["base"]
    surface = palette["surface"]
    text = palette["text"]
    muted = palette["muted"]
    accent = palette["accent"]
    control_radius = int(radius["control"])
    ui_font = typography["ui"]
    # Keep the Qt family declaration valid; glyph fallback remains a system
    # fontconfig responsibility and resolves through Noto Sans in the image.
    qss_font = f'"{ui_font}"'
    return f"""/* Generated from tokens.yaml; do not edit. */
QWidget#properWelcome {{ color: {text}; background: transparent; font-family: {qss_font}; }}
QWidget#properWelcome QLabel#eyebrow {{ color: {muted}; font-size: 11px; font-weight: 700; letter-spacing: 2px; }}
QWidget#properWelcome QLabel#headline {{ color: {text}; font-size: 35px; font-weight: 650; }}
QWidget#properWelcome QLabel#body {{ color: {muted}; font-size: 15px; }}
QWidget#properWelcome QFrame#shortcutLine {{ background: transparent; border: 0; }}
QWidget#properWelcome QLabel#shortcutAction {{ color: {muted}; font-size: 11px; }}
QWidget#properWelcome QLabel#keyJoin {{ color: {muted}; font-size: 10px; }}
QWidget#properWelcome QLabel#keycap {{ color: {text}; background: {rgba(surface, 0.920)}; border: 1px solid {rgba(muted, 0.330)}; border-bottom: 2px solid {rgba(muted, 0.420)}; border-radius: 6px; min-width: 18px; min-height: 18px; padding: 1px 5px; font-family: "{typography['mono']}"; font-size: 10px; font-weight: 650; }}
QWidget#properWelcome QPushButton {{ min-height: 54px; min-width: 176px; padding: 0 24px; border-radius: {control_radius + 3}px; border: 1px solid {rgba(muted, 0.220)}; background: {rgba(surface, 0.760)}; color: {text}; font-family: {qss_font}; font-size: 14px; font-weight: 600; }}
QWidget#properWelcome QPushButton:hover {{ background: {rgba(accent, 0.150)}; border-color: {rgba(accent, 0.450)}; }}
QWidget#properWelcome QPushButton:focus {{ border: 2px solid {accent}; }}
QWidget#properWelcome QPushButton#primary {{ background: {accent}; color: {base}; border-color: {accent}; }}
"""


def web_css(dark: dict[str, str], light: dict[str, str], radius: dict[str, str], typography: dict[str, str]) -> str:
    def variables(palette: dict[str, str]) -> str:
        return " ".join(f"--proper-{key}: {value};" for key, value in palette.items())
    return f"""/* Generated from tokens.yaml; do not edit. */
:root {{ color-scheme: light dark; font-family: {typography['ui']}, \"{typography['fallback']}\", sans-serif; {variables(dark)} }}
@media (prefers-color-scheme: light) {{ :root {{ {variables(light)} }} }}
body {{ margin: 0; background: var(--proper-base); color: var(--proper-text); }}
main {{ max-width: 900px; margin: 0 auto; padding: 64px 28px 96px; }}
h1 {{ margin: 0; font-size: clamp(2rem, 6vw, 4.2rem); letter-spacing: -.055em; }}
.lede {{ max-width: 680px; color: var(--proper-muted); font-size: 1.08rem; line-height: 1.6; }}
input {{ box-sizing: border-box; width: 100%; margin: 30px 0 18px; padding: 15px 18px; border: 1px solid color-mix(in srgb, var(--proper-muted) 36%, transparent); border-radius: {radius['popup']}px; background: var(--proper-surface); color: inherit; font: inherit; outline: none; }}
input:focus {{ border-color: var(--proper-accent); box-shadow: 0 0 0 3px color-mix(in srgb, var(--proper-accent) 22%, transparent); }}
section {{ margin-top: 34px; }}
h2 {{ color: var(--proper-muted); font-size: .86rem; letter-spacing: .12em; text-transform: uppercase; }}
.row {{ display: grid; grid-template-columns: minmax(190px, .8fr) 1.8fr; gap: 24px; padding: 15px 2px; border-bottom: 1px solid color-mix(in srgb, var(--proper-muted) 20%, transparent); align-items: center; }}
kbd {{ display: inline-block; padding: 5px 9px; border: 1px solid color-mix(in srgb, var(--proper-muted) 42%, transparent); border-bottom-width: 2px; border-radius: {radius['control']}px; background: var(--proper-surface); color: var(--proper-text); font: 600 .88rem \"{typography['mono']}\", monospace; }}
.action {{ color: var(--proper-text); line-height: 1.45; }}
.empty {{ display: none; padding: 36px 0; color: var(--proper-muted); }}
footer {{ margin-top: 48px; color: var(--proper-muted); line-height: 1.6; }}
@media (max-width: 620px) {{ main {{ padding-top: 40px; }} .row {{ grid-template-columns: 1fr; gap: 8px; }} }}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tokens", type=Path)
    parser.add_argument("output", type=Path)
    arguments = parser.parse_args()

    source = arguments.tokens.read_text(encoding="utf-8")
    dark = inline_map(source, "dark", "  ")
    light = inline_map(source, "light", "  ")
    radius = inline_map(source, "radius")
    spacing = inline_map(source, "spacing")
    typography = inline_map(source, "typography")
    arguments.output.mkdir(parents=True, exist_ok=True)
    (arguments.output / "proper-widgets-dark.qss").write_text(widget_qss(dark, radius, spacing, typography), encoding="utf-8")
    (arguments.output / "proper-widgets-light.qss").write_text(widget_qss(light, radius, spacing, typography), encoding="utf-8")
    (arguments.output / "proper-welcome.qss").write_text(welcome_qss(dark, radius, typography), encoding="utf-8")
    (arguments.output / "proper-web.css").write_text(web_css(dark, light, radius, typography), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
