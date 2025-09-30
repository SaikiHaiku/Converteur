from core.base import BasePlugin
import chardet

class TextPlugin(BasePlugin):
    @staticmethod
    def supported_output_formats():
        return ["txt", "md", "rtf", "pdf", "docx", "csv"]

    def can_handle(self, input_path, output_format):
        return output_format in self.supported_output_formats() and input_path.lower().endswith(
            (".txt", ".md", ".rtf", ".csv", ".docx", ".pdf")
        )

    def convert(self, input_path, output_path, output_format, convert_metadata):
        # Exemple basique : TXT <-> autres textes
        with open(input_path, 'rb') as f:
            raw = f.read()
        encoding = chardet.detect(raw)['encoding']
        text = raw.decode(encoding)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        # TODO: Ajouter conversion vers PDF, DOCX, etc.