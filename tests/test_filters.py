import unittest
from unittest.mock import Mock

from PIL import Image

from domain.args_parser.args_parse import ArgParser
from filters import Main
from domain.tools.filter_classes import FilterClasses
from domain.tools.cli_messages import CLIMessages
from domain.tools.image_io import ImageIO


class FiltersTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_image_io = Mock(spec=ImageIO)

        self.filter_classes = FilterClasses()
        filters = self.filter_classes.get_filters()
        self.arg_parser = ArgParser(filters)
        filters = self.filter_classes.get_filters()
        self.arg_parser = ArgParser(filters)
        self.cli_messages = CLIMessages(filters)

        with Image.open('tests/images/overlap_expected.png') as im:
            self._expected_overlap = im.convert("RGBA")

        with Image.open('tests/images/rotate_expected.png') as im:
            self._expected_rotate = im.convert("RGBA")

            with Image.open('tests/images/test_multi_filter.png') as im:
                self._test_multi_filter = im.convert("RGBA")

    def test_sepia_filter(self):
        expected = Image.new('RGBA', (1, 1), (185, 166, 128, 255))

        image = Image.new('RGB', (1, 1), (100, 127, 254))
        self.mock_image_io.load_image.return_value = image

        cli_args = ["input.jpg", "--sepia", "output.jpg"]
        filters = Main(
            filter_classes=self.filter_classes,
            image_io=self.mock_image_io,
            cli_args=cli_args,
            cli_messages=self.cli_messages,
            arg_parser=self.arg_parser
        )
        image, image_output_name = filters.run()

        self.assertEqual("output.jpg", image_output_name)
        self.assertEqual(expected, image)

    def test_grayscale_filter(self):
        expected = Image.new('RGBA', (1, 1), (133, 133, 133, 255))

        image = Image.new('RGB', (1, 1), (100, 127, 254))
        self.mock_image_io.load_image.return_value = image

        cli_args = ["input.jpg", "--grayscale", "output.jpg"]
        filters = Main(
            filter_classes=self.filter_classes,
            image_io=self.mock_image_io,
            cli_args=cli_args,
            cli_messages=self.cli_messages,
            arg_parser=self.arg_parser
        )
        image, image_output_name = filters.run()

        self.assertEqual("output.jpg", image_output_name)
        self.assertEqual(expected, image)

    def test_overlay_filter(self):

        image = Image.new('RGB', (500, 500), (100, 127, 254))
        self.mock_image_io.load_image.return_value = image

        cli_args = ["input.jpg", "--overlay", "python.png", "output.jpg"]
        filters = Main(
            filter_classes=self.filter_classes,
            image_io=self.mock_image_io,
            cli_args=cli_args,
            cli_messages=self.cli_messages,
            arg_parser=self.arg_parser
        )
        image, image_output_name = filters.run()

        self.assertEqual("output.jpg", image_output_name)
        self.assertEqual(self._expected_overlap, image)

    def test_rotate_filter(self):

        image = Image.new('RGB', (500, 500), (100, 127, 254))
        self.mock_image_io.load_image.return_value = image

        cli_args = ["input.jpg", "--rotate", "45", "output.jpg"]
        filters = Main(
            filter_classes=self.filter_classes,
            image_io=self.mock_image_io,
            cli_args=cli_args,
            cli_messages=self.cli_messages,
            arg_parser=self.arg_parser
        )
        image, image_output_name = filters.run()

        self.assertEqual("output.jpg", image_output_name)
        self.assertEqual(self._expected_rotate, image)

    def test_multi_filter(self):

        image = Image.new('RGB', (500, 500), (100, 127, 254))
        self.mock_image_io.load_image.return_value = image

        cli_args = [
            "input.jpg",
            "--sepia",
            "--rotate", "45",
            "--overlay", "python.png",
            "--rotate", "-90",
            "output.jpg"
        ]
        filters = Main(
            filter_classes=self.filter_classes,
            image_io=self.mock_image_io,
            cli_args=cli_args,
            cli_messages=self.cli_messages,
            arg_parser=self.arg_parser
        )
        image, image_output_name = filters.run()

        self.assertEqual("output.jpg", image_output_name)
        self.assertEqual(self._test_multi_filter, image)
