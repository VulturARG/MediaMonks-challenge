from typing import Optional


class ParserException(Exception):
    """Base class for all exceptions."""

    MESSAGE: Optional[str] = None


class HelpRequired(ParserException):
    MESSAGE = None

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class FewArguments(ParserException):
    MESSAGE = "Too few arguments."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class FilterWrongInit(ParserException):
    MESSAGE = "Filter must start with --."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class WrongFilter(ParserException):
    MESSAGE = "Filter error name."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class WrongArguments(ParserException):
    MESSAGE = "Arguments cannot start with --."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)

