from typing import Dict, Tuple, Type, Optional

from domain.filters import Filter


class CLIMessages:
    """Prints messages in CLI."""

    def __init__(self, filters: Dict[str, Tuple[Type[Filter], int, str]]):
        self._filters = filters

    def print_help(self, message: Optional[str] = None) -> None:
        if message is not None:
            print()
            print(message)
        print()
        print("Usage:")
        print("python filters.py input_file [--filter_name [filter_value [--filter_name [filter_value [...]]]]] output_file")
        for filter_class, _, help_text in self._filters.values():
            print(f"--{filter_class.__name__.lower()}: {help_text}")
        print()

    def print_success(self) -> None:
        print()
        print("Filters applied successfully")
        print()
