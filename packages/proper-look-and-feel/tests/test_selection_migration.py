"""Only exact former defaults may be changed, never a user's custom palette."""
import importlib.machinery
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = importlib.machinery.SourceFileLoader('repair', str(ROOT / 'proper-selection-default-repair')).load_module()
SIGNATURES = json.loads((ROOT / 'selection-migration.json').read_text())


class SelectionMigrationTest(unittest.TestCase):
    def test_old_defaults_are_repaired(self):
        for name, palette in SIGNATURES.items():
            self.assertEqual(MODULE.replacement_for(name, palette['old'], SIGNATURES), palette['new'])

    def test_one_custom_colour_preserves_entire_selection(self):
        custom = dict(SIGNATURES['Proper']['old'], ForegroundNormal='255,0,0')
        self.assertIsNone(MODULE.replacement_for('Proper', custom, SIGNATURES))

    def test_other_theme_and_already_repaired_are_untouched(self):
        self.assertIsNone(MODULE.replacement_for('Custom', SIGNATURES['Proper']['old'], SIGNATURES))
        self.assertIsNone(MODULE.replacement_for('Proper', SIGNATURES['Proper']['new'], SIGNATURES))


if __name__ == '__main__':
    unittest.main()
