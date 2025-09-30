import logging
from core.plugins import plugins

class ConversionDispatcher:

    @staticmethod
    def convert(input_path, output_path, output_format, convert_metadata=False):
        # Parcours tous les plugins et lance le bon
        for plug in plugins:
            if plug.can_handle(input_path, output_format):
                logging.info(f"Conversion via plugin: {plug.__class__.__name__}")
                plug.convert(input_path, output_path, output_format, convert_metadata)
                return
        raise Exception(f"Aucun plugin ne gère la conversion de ce fichier vers {output_format}")

    @staticmethod
    def list_supported_formats():
        formats = {}
        for plug in plugins:
            for ext in plug.supported_output_formats():
                formats.setdefault(ext, []).append(plug.__class__.__name__)
        print("Formats supportés :")
        for ext, handlers in formats.items():
            print(f"  {ext}: via {', '.join(handlers)}")