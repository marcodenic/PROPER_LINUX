"""Render the title material: it must remain translucent and have a blur mask."""
import os
from pathlib import Path
import sys
import unittest

os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
from PySide6.QtCore import QRectF
from PySide6.QtGui import QImage, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QApplication

APP = QApplication.instance() or QApplication([])
ROOT = Path(sys.argv.pop())


def pixel(renderer, element):
    image = QImage(32, 32, QImage.Format.Format_ARGB32_Premultiplied)
    image.fill(0)
    painter = QPainter(image)
    renderer.render(painter, element, QRectF(0, 0, 32, 32))
    painter.end()
    return image.pixelColor(16, 16)


class WindowMaterialTest(unittest.TestCase):
    def test_translucent_material_has_solid_blur_mask(self):
        for variant in ('dark', 'light', 'midnight'):
            with self.subTest(variant=variant):
                renderer = QSvgRenderer(str(ROOT / ('proper-' + variant) / 'decoration.svg'))
                self.assertTrue(renderer.isValid())
                self.assertAlmostEqual(pixel(renderer, 'decoration-center').alphaF(), .66, delta=2 / 255)
                self.assertEqual(pixel(renderer, 'mask-center').alpha(), 255)
                self.assertEqual(renderer.boundsOnElement('decoration-topleft').size(),
                                 renderer.boundsOnElement('mask-topleft').size())


if __name__ == '__main__':
    unittest.main()
