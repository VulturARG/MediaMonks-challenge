from unittest import TestCase

from PIL import Image

from domain.tools.exceptions import LoadError, SaveError
from domain.tools.image_io import ImageIO


class ImageIOTestCase(TestCase):
    def setUp(self) -> None:
        self.image_io = ImageIO()

    def test_load_wrong_image_name(self):
        with self.assertRaises(LoadError):
            self.image_io.load_image("wrong_image_name")

    def test_save_jpg_image(self):
        image = Image.new('RGB', (1, 1), (100, 127, 254))
        image_name = "test_image.jpg"
        self.image_io.save_image(image, image_name)

    def test_save_png_image(self):
        image = Image.new('RGB', (1, 1), (100, 127, 254))
        image_name = "test_image.png"
        self.image_io.save_image(image, image_name)

    def test_save_png_image_with_alpha_channel(self):
        image = Image.new('RGBA', (1, 1), (100, 127, 254, 0))
        image_name = "test_image.png"
        self.image_io.save_image(image, image_name)

    def test_save_wrong_extension(self):
        image = Image.new('RGBA', (1, 1), (100, 127, 254, 0))
        image_name = "test_image.aaa"
        with self.assertRaises(SaveError):
            self.image_io.save_image(image, image_name)
