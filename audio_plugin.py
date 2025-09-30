from core.base import BasePlugin
from pydub import AudioSegment

class AudioPlugin(BasePlugin):
    @staticmethod
    def supported_output_formats():
        return ["mp3", "wav", "ogg", "flac", "aac", "m4a"]

    def can_handle(self, input_path, output_format):
        return input_path.lower().endswith(('.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a')) \
               and output_format in self.supported_output_formats()

    def convert(self, input_path, output_path, output_format, convert_metadata):
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format=output_format)
        # TODO: gérer les tags ID3, etc.