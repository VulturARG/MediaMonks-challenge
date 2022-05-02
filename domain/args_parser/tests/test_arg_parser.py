from unittest import TestCase
from unittest.mock import Mock

from domain.args_parser.args_parse import ArgParser
from domain.filters import Filter
from domain.args_parser.exceptions import (
    HelpRequired,
    FilterWrongInit,
    WrongArguments,
    FewArguments, WrongFilter
)
from domain.tools.exceptions import ExtensionNotAllowed
from domain.tools.filter_classes import FilterClasses


class ArgParserTestCase(TestCase):
    def setUp(self) -> None:
        self.mock_filter_classes = Mock(spec=FilterClasses)
        self.mock_filter = Mock(spec=Filter)
        self.mock_filter_classes.get_filters.return_value = {
            "grayscale": (self.mock_filter, 0),
            "rotate": (self.mock_filter, 1),
        }
        filters = self.mock_filter_classes.get_filters()
        self.arg_parser = ArgParser(filters)

    def test_help_required_h(self):
        cli_args = ["-h"]
        with self.assertRaises(HelpRequired):
            self.arg_parser.parser(cli_args)

    def test_help_required_help(self):
        cli_args = ["--help"]
        with self.assertRaises(HelpRequired):
            self.arg_parser.parser(cli_args)

    def test_few_arguments(self):
        cli_args = ["input.jpg", "output.jpg"]
        with self.assertRaises(FewArguments):
            self.arg_parser.parser(cli_args)

    def test_wrong_extension_input_name(self):
        cli_args = ["bad", "--optional", "output.jpg"]
        with self.assertRaises(ExtensionNotAllowed):
            self.arg_parser.parser(cli_args)

    def test_good_extension_names(self):
        expected = (("input.jpg", "output.jpg"), [(self.mock_filter, [])])

        cli_args = ["input.jpg", "--grayscale", "output.jpg"]
        actual = self.arg_parser.parser(cli_args)
        self.assertEqual(expected, actual)

    def test_wrong_output_name(self):
        cli_args = ["input.jpg", "--optional", "bad"]
        with self.assertRaises(ExtensionNotAllowed):
            self.arg_parser.parser(cli_args)

    def test_wrong_extension_output_name(self):
        cli_args = ["input.jpg", "--optional", "output.bad"]
        with self.assertRaises(ExtensionNotAllowed):
            self.arg_parser.parser(cli_args)

    def test_wrong_filter(self):
        cli_args = ["image.jpg", "--wrong_filter", "output.jpg"]
        with self.assertRaises(WrongFilter):
            self.arg_parser.parser(cli_args)

    def test_good_extension_output_name(self):
        expected = (("input.jpg", "output.jpg"), [(self.mock_filter, [])])

        cli_args = ["input.jpg", "--grayscale", "output.jpg"]
        actual = self.arg_parser.parser(cli_args)
        self.assertEqual(expected, actual)

    def test_bad_optional_argument(self):
        cli_args = ["image.jpg", "bad_optional", "output.jpg"]
        with self.assertRaises(FilterWrongInit):
            self.arg_parser.parser(cli_args)

    def test_good_optional_argument_without_argument(self):
        expected = (("image.jpg", "output.jpg"), [(self.mock_filter, [])])

        cli_args = ["image.jpg", "--grayscale", "output.jpg"]
        actual = self.arg_parser.parser(cli_args)
        self.assertEqual(expected, actual)

    def test_good_optional_argument_with_argument(self):
        expected = (("image.jpg", "output.jpg"), [(self.mock_filter, ["45"])])

        cli_args = ["image.jpg", "--rotate", "45", "output.jpg"]
        actual = self.arg_parser.parser(cli_args)
        self.assertEqual(expected, actual)

    def test_one_filter_bad_arguments(self):
        cli_args = ["image.jpg", "--grayscale", "45", "output.jpg"]
        with self.assertRaises(FilterWrongInit):
            self.arg_parser.parser(cli_args)

    def test_two_filters(self):
        expected = (
            ("image.jpg", "output.jpg"),
            [(self.mock_filter, []), (self.mock_filter, ["45"])]
        )

        cli_args = ["image.jpg", "--grayscale", "--rotate", "45", "output.jpg"]
        actual = self.arg_parser.parser(cli_args)
        self.assertEqual(expected, actual)

    def test_two_filters_bad_arguments(self):
        cli_args = ["image.jpg", "--rotate", "--grayscale", "45", "output.jpg"]
        with self.assertRaises(WrongArguments):
            self.arg_parser.parser(cli_args)
