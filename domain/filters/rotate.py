from __future__ import annotations

from PIL import Image

from domain.filters import Filter


class Rotate(Filter):
    """Rotate an image."""

    ARGUMENTS = 1
    HELP = "Rotate an image. Argument: angle in degrees."

    def transform(self, image: Image, *args, **kwargs) -> Image:
        """Rotate image."""

        return image.rotate(int(args[0][0]))

    @classmethod
    def build_filter(cls) -> Filter:
        """Build the filter."""

        return cls()
