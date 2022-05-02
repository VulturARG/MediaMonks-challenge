from __future__ import annotations

from PIL import Image

from domain.filters import Filter
from domain.tools.exceptions import NotPngImage, NotTransparentImage
from domain.tools.image_io import ImageIO


class Overlay(Filter):
    """Overlay one image over another."""

    ARGUMENTS = 1
    HELP = "Overlay an image. Must be an image with alpha channel. Argument: image name to overlay."

    def transform(self, image: Image, *args, **kwargs) -> Image:
        """
        Overlay one image over another.

        Args:
            image (Image): The image to transform.
            *args: The arguments to pass to the filter.
            **kwargs: The keyword arguments to pass to the filter.

        Returns:
            Image: The transformed image.
        """

        image = image.convert("RGBA")
        image_io = ImageIO()
        overlay_image_name = args[0][0]
        extension = overlay_image_name.split(".")[-1]
        if extension != "png":
            raise NotPngImage()

        image_overlay = image_io.load_image(overlay_image_name)
        if not self._has_transparency(image_overlay):
            raise NotTransparentImage()

        image_overlay = image_overlay.convert("RGBA")
        image.paste(image_overlay, (0, 0), image_overlay)
        return image

    def _has_transparency(self, img: Image) -> bool:
        """Check if the image has transparency."""

        if img.info.get("transparency", None) is not None:
            return True
        if img.mode == "P":
            transparent = img.info.get("transparency", -1)
            for _, index in img.getcolors():
                if index == transparent:
                    return True
        elif img.mode == "RGBA":
            extrema = img.getextrema()
            if extrema[3][0] < 255:
                return True

        return False

    @classmethod
    def build_filter(cls) -> Filter:
        """Build the filter."""

        return cls()
