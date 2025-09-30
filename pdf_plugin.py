from core.base import BasePlugin
from PyPDF2 import PdfReader, PdfWriter

class PdfPlugin(BasePlugin):
    @staticmethod
    def supported_output_formats():
        return ["pdf", "txt"]

    def can_handle(self, input_path, output_format):
        return input_path.lower().endswith(".pdf") and output_format in self.supported_output_formats()

    def convert(self, input_path, output_path, output_format, convert_metadata):
        if output_format == "txt":
            reader = PdfReader(input_path)
            text = "\n".join([page.extract_text() or "" for page in reader.pages])
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
        else:
            # TODO : Fusion, split, etc.
            pass