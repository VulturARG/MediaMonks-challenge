from __future__ import annotations

from abc import ABC, abstractmethod

from PIL import Image


class Filter(ABC):
    """Abstract class for filters."""

    ARGUMENTS = 0
    HELP = ""

    @abstractmethod
    def transform(self, image: Image, *args, **kwargs) -> Image:
        """
        Transform the image.

        Args:
            image: The image to transform.
            *args: Arguments for the transformation.
            **kwargs: Keyword arguments for the transformation.

        Returns:
            The transformed image.
        """

    @classmethod
    @abstractmethod
    def build_filter(cls) -> Filter:
        """Build the filter."""
