from typing import List, Dict, Tuple

from domain.filters import Filter
from domain.args_parser.exceptions import (
    HelpRequired,
    FewArguments,
    FilterWrongInit,
    WrongFilter,
    WrongArguments
)
from domain.tools.exceptions import ExtensionNotAllowed


class ArgParser:
    """Parse arguments from command line"""
    MINIMUM_ARGUMENT = 3
    HELP_CALL = ["-h", "--help"]
    ALLOWED_EXTENSIONS = ["jpg", "tiff"]

    def __init__(self, filters: Dict) -> None:
        self._filters = filters

    def parser(self, cli_args: List[str]) -> Tuple[Tuple[str, str], List[Tuple[Filter, List[str]]]]:

        if cli_args[0].lower() in self.HELP_CALL:
            raise HelpRequired()

        if len(cli_args) < self.MINIMUM_ARGUMENT:
            raise FewArguments()

        io_image_names = (cli_args[0], cli_args[-1])
        self._verify_image_names(io_image_names)

        filters_command = self._get_filters_from_cli(cli_args[1:-1])
        return io_image_names, filters_command

    def _verify_image_names(self, io_names: Tuple[str, str]) -> None:
        for name in io_names:
            extension = name.split(".")[-1]
            if extension not in self.ALLOWED_EXTENSIONS:
                raise ExtensionNotAllowed()

    def _get_filters_from_cli(self, args: List[str]) -> List[Tuple[Filter, List[str]]]:
        filters = []
        index = 0
        while index < len(args):
            if not args[index].startswith("--"):
                raise FilterWrongInit()

            arg = args[index].replace("--", "").lower()
            if not arg in self._filters:
                raise WrongFilter()

            max_arguments = self._filters[arg][1]
            arguments = []
            for filter_arg in args[index + 1: index + max_arguments + 1]:
                if filter_arg.startswith("--"):
                    raise WrongArguments()
                arguments.append(filter_arg)

            filters.append((self._filters[arg][0], arguments))
            index += 1 + max_arguments

        return filters
