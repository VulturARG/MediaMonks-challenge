from PIL import Image

from domain.tools.exceptions import LoadError, SaveError


class ImageIO:
    """Image input/output class."""

    def load_image(self, image_name: str) -> Image:
        try:
            return Image.open(image_name)
        except FileNotFoundError:
            raise LoadError()

    def save_image(self, image: Image, image_name: str) -> None:
        try:
            extension = image_name.split('.')[-1].upper()
            extension = "JPEG" if extension == "JPG" else extension
            if extension == "JPEG":
                image = image.convert("RGB")
            image.save(image_name, extension)
        except KeyError:
            raise SaveError()
