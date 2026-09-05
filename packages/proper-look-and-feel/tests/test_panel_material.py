"""Render real Qt SVG slices to catch fractional bounds and alpha seams."""
import os
from pathlib import Path
import sys
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from PySide6.QtCore import QRectF
from PySide6.QtGui import QImage, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QApplication

APP = QApplication.instance() or QApplication([])
ASSETS = Path(sys.argv.pop()) if len(sys.argv) > 1 else Path(__file__).parents[1] / "proper" / "widgets"


def render(renderer, element, width, height):
    image = QImage(width, height, QImage.Format.Format_ARGB32_Premultiplied)
    image.fill(0)
    painter = QPainter(image)
    renderer.render(painter, element, QRectF(0, 0, width, height))
    painter.end()
    return image


class PanelMaterialTest(unittest.TestCase):
    def test_corner_bounds_match_their_masks(self):
        for asset in ASSETS.glob("*background.svg"):
            renderer = QSvgRenderer(str(asset))
            for corner in ("topleft", "topright", "bottomleft", "bottomright"):
                with self.subTest(asset=asset.name, corner=corner):
                    self.assertEqual(renderer.boundsOnElement(corner).size(),
                                     renderer.boundsOnElement("mask-" + corner).size())

    def test_corner_fill_meets_straight_edges_without_alpha_seams(self):
        for asset in ASSETS.glob("*background.svg"):
            renderer = QSvgRenderer(str(asset))
            corner = render(renderer, "topleft", 16, 16)
            top = render(renderer, "top", 36, 16)
            left = render(renderer, "left", 16, 36)
            for offset in range(2, 15):
                with self.subTest(asset=asset.name, offset=offset):
                    self.assertEqual(corner.pixelColor(15, offset), top.pixelColor(18, offset))
                    self.assertEqual(corner.pixelColor(offset, 15), left.pixelColor(offset, 18))


if __name__ == "__main__":
    unittest.main()
