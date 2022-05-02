from __future__ import annotations

from typing import Tuple

from PIL import Image

from domain.filters import Filter


class Sepia(Filter):
    """Transforms the colors of an image to sepia tones."""

    ARGUMENTS = 0
    HELP = "Transforms the colors of an image to sepia tones. No arguments."

    def transform(self, image: Image, *args, **kwargs) -> Image:
        """
        Transform the image to sepia tones.

        :param image: The image to transform.
        :return: The transformed image.
        """

        width, height = image.size
        pixels = image.load()
        for py in range(height):
            for px in range(width):
                rgba = image.getpixel((px, py))
                transformed_pixels = self._get_sepia_pixel(rgba[0], rgba[1], rgba[2])
                if len(rgba) == 4:
                    pixels[px, py] = (
                        transformed_pixels[0],
                        transformed_pixels[1],
                        transformed_pixels[2],
                        rgba[3]
                    )
                else:
                    pixels[px, py] = transformed_pixels
        return image

    def _get_sepia_pixel(self, red: int, green: int, blue: int) -> Tuple[int, int, int]:
        """Transform a colored pixel to sepia."""

        sepia_red = round(0.393 * red + 0.769 * green + 0.189 * blue)
        sepia_green = round(0.349 * red + 0.686 * green + 0.173 * blue)
        sepia_blue = round(0.272 * red + 0.534 * green + 0.131 * blue)

        return self._normalize_rgb(sepia_red, sepia_green, sepia_blue)

    def _normalize_color(self, color: int) -> int:
        """0 <= Color <= 255."""

        color = 0 if color < 0 else color
        color = 255 if color > 255 else color
        return color

    def _normalize_rgb(self, red: int, green: int, blue: int) -> Tuple[int, int, int]:
        """Ensure rgb values are correct."""

        red = self._normalize_color(red)
        green = self._normalize_color(green)
        blue = self._normalize_color(blue)
        return red, green, blue

    @classmethod
    def build_filter(cls) -> Filter:
        """Build the filter."""

        return cls()
