from typing import Optional


class IOException(Exception):
    """Base class for all IO exceptions."""

    MESSAGE: Optional[str] = None


class LoadError(IOException):
    MESSAGE = "Image could not be loaded. Check the name and try again."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class SaveError(IOException):
    MESSAGE = "Image could not be saved. Check the name and try again."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class NotPngImage(IOException):
    MESSAGE = "The file must be a png image."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class ExtensionNotAllowed(IOException):
    MESSAGE = "The extension is not allowed."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class NotTransparentImage(IOException):
    MESSAGE = "The file must have a transparent (alpha) channel."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)