from core.base import BasePlugin
from PIL import Image
import os

class ImagePlugin(BasePlugin):
    @staticmethod
    def supported_output_formats():
        return ["png", "jpg", "jpeg", "bmp", "tiff", "gif", "webp", "pdf"]

    def can_handle(self, input_path, output_format):
        return (input_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif', '.webp'))
                and output_format in self.supported_output_formats())

    def convert(self, input_path, output_path, output_format, convert_metadata):
        img = Image.open(input_path)
        if output_format == "pdf":
            img.save(output_path, "PDF")
        else:
            img.save(output_path, output_format.upper())
        # TODO: gestion avancée des métadonnées (EXIF, etc.)