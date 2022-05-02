from unittest import TestCase

from PIL import Image

from domain.filters import Sepia


class SepiaTestCase(TestCase):
    def test_normalize_color_greater_255(self):
        sepia = Sepia()
        normalized = sepia._normalize_color(300)
        self.assertEqual(255, normalized)

    def test_normalize_color_lower_0(self):
        sepia = Sepia()
        normalized = sepia._normalize_color(-5)
        self.assertEqual(0, normalized)

    def test_normalize_color_between_0_and_255(self):
        sepia = Sepia()
        normalized = sepia._normalize_color(5)
        self.assertEqual(5, normalized)

    def test_normalize_rgb(self):
        sepia = Sepia()
        actual = sepia._normalize_rgb(-5, 5, 555)
        self.assertEqual((0, 5, 255), actual)

    def test_get_sepia_pixel(self):
        expected = (185, 166, 128)

        sepia = Sepia()
        actual = sepia._get_sepia_pixel(100, 127, 254)
        self.assertEqual(expected, actual)

    def test_transform_image_rgb_to_sepia_color(self):
        expected = Image.new('RGB', (1, 1), (185, 166, 128))

        image = Image.new('RGB', (1, 1), (100, 127, 254))
        sepia = Sepia()
        actual = sepia.transform(image)
        self.assertEqual(expected, actual)

    def test_transform_image_rgba_to_sepia_color(self):
        expected = Image.new('RGBA', (1, 1), (185, 166, 128, 0))

        image = Image.new('RGBA', (1, 1), (100, 127, 254, 0))
        sepia = Sepia()
        actual = sepia.transform(image)
        self.assertEqual(expected, actual)
