from __future__ import annotations

from PIL import Image, ImageOps

from domain.filters.filter import Filter


class Grayscale(Filter):
    """Transform image to gray scale."""

    ARGUMENTS = 0
    HELP = "Transform image to gray scale. No arguments."

    def transform(self, image: Image, *args, **kwargs) -> Image:
        """
        Transform the image to gray scale.

        Args:
            image: The image to transform.
            *args: Arguments for the transformation.
            **kwargs: Keyword arguments for the transformation.

        Returns:
            The transformed image.
        """

        return ImageOps.grayscale(image)

    @classmethod
    def build_filter(cls) -> Filter:
        """Build the filter."""

        return cls()
