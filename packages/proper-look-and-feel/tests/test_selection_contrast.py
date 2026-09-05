"""Selected labels must stay readable independently of accent-button text."""
import configparser
from pathlib import Path
import sys
import unittest

ROOT = Path(sys.argv.pop())


def luminance(rgb):
    channels = [int(value) / 255 for value in rgb.split(',')]
    linear = [value / 12.92 if value <= 0.04045 else ((value + .055) / 1.055) ** 2.4 for value in channels]
    return sum(value * weight for value, weight in zip(linear, (.2126, .7152, .0722)))


class SelectionContrastTest(unittest.TestCase):
    def test_selected_normal_text_meets_aa(self):
        for name in ('Proper', 'ProperLight', 'ProperMidnight'):
            with self.subTest(scheme=name):
                scheme = configparser.ConfigParser()
                scheme.read(ROOT / (name + '.colors'))
                colors = scheme['Colors:Selection']
                levels = sorted(luminance(colors[key]) for key in ('BackgroundNormal', 'ForegroundNormal'))
                self.assertGreaterEqual((levels[1] + .05) / (levels[0] + .05), 4.5)


if __name__ == '__main__':
    unittest.main()
