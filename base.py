from abc import ABC, abstractmethod

class BasePlugin(ABC):
    @staticmethod
    @abstractmethod
    def supported_output_formats():
        """Liste les formats de sortie gérés par ce plugin"""
        pass

    @abstractmethod
    def can_handle(self, input_path, output_format):
        """Retourne True si ce plugin gère la conversion de ce fichier vers ce format"""
        pass

    @abstractmethod
    def convert(self, input_path, output_path, output_format, convert_metadata):
        """Effectue la conversion"""
        pass