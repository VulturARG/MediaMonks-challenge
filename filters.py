import sys
from typing import List, Tuple, Any

from PIL import Image

from domain.args_parser.args_parse import ArgParser
from domain.args_parser.exceptions import ParserException
from domain.filters import Filter
from domain.tools.exceptions import IOException
from domain.tools.filter_classes import FilterClasses
from domain.tools.cli_messages import CLIMessages
from domain.tools.image_io import ImageIO


class Main:
    """Read and process the arguments, and apply the filter to the image."""

    def __init__(
        self,
        filter_classes: FilterClasses,
        image_io: ImageIO,
        cli_args: List[str],
        cli_messages: CLIMessages,
        arg_parser: ArgParser,
    ) -> None:

        self._filter_classes = filter_classes
        self._image_io = image_io
        self._cli_args = cli_args
        self._cli_messages = cli_messages
        self._arg_parser = arg_parser

    def run(self) -> Tuple[Any, str]:
        """Run the program."""

        if len(self._cli_args) == 0:
            self._cli_messages.print_help()
            sys.exit(0)

        try:
            parser = self._arg_parser.parser(self._cli_args)
            io_image_names = parser[0]
            filters = parser[1]
            image = self._image_io.load_image(io_image_names[0])
        except (ParserException, IOException) as error:
            self._cli_messages.print_help(error.MESSAGE)
            sys.exit(0)

        image = self._filter_applier(image, filters)

        return image, io_image_names[1]

    def _filter_applier(
        self, image: Image, filters: List[Tuple[Filter, List[str]]]
    ) -> Image:
        """Apply the filters to the image."""

        for filter_type, arguments in filters:
            actual_filter = filter_type.build_filter()
            image = actual_filter.transform(image, arguments).convert("RGBA")

        return image


def main():
    """Read the filters from the CLI and inject all classes needed."""
    cli_args = sys.argv[1:]

    image_io = ImageIO()
    filter_classes = FilterClasses()
    filters = filter_classes.get_filters()
    arg_parser = ArgParser(filters)
    cli_messages = CLIMessages(filters)

    filters = Main(
        filter_classes=filter_classes,
        image_io=image_io,
        cli_args=cli_args,
        cli_messages=cli_messages,
        arg_parser=arg_parser,
    )
    image, image_output_name = filters.run()
    image_io.save_image(image, image_output_name)
    cli_messages.print_success()


if __name__ == "__main__":
    main()
