from core.base import BasePlugin
import moviepy.editor as mp

class VideoPlugin(BasePlugin):
    @staticmethod
    def supported_output_formats():
        return ["mp4", "avi", "mov", "webm", "gif", "mp3"]

    def can_handle(self, input_path, output_format):
        return input_path.lower().endswith(('.mp4', '.avi', '.mov', '.webm', '.mkv', '.flv')) \
               and output_format in self.supported_output_formats()

    def convert(self, input_path, output_path, output_format, convert_metadata):
        clip = mp.VideoFileClip(input_path)
        if output_format == "mp3":
            clip.audio.write_audiofile(output_path)
        else:
            clip.write_videofile(output_path)