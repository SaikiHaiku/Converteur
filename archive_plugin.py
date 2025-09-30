from core.base import BasePlugin
import shutil
import os

class ArchivePlugin(BasePlugin):
    @staticmethod
    def supported_output_formats():
        return ["zip", "tar", "gztar", "bztar", "xztar"]

    def can_handle(self, input_path, output_format):
        return os.path.isdir(input_path) and output_format in self.supported_output_formats()

    def convert(self, input_path, output_path, output_format, convert_metadata):
        # Utilise shutil.make_archive
        base, _ = os.path.splitext(output_path)
        shutil.make_archive(base, output_format, root_dir=input_path)