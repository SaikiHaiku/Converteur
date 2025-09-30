from core.base import BasePlugin
import pandas as pd

class SpreadsheetPlugin(BasePlugin):
    @staticmethod
    def supported_output_formats():
        return ["csv", "xlsx", "ods", "json"]

    def can_handle(self, input_path, output_format):
        return input_path.lower().endswith(('.csv', '.xlsx', '.ods')) \
               and output_format in self.supported_output_formats()

    def convert(self, input_path, output_path, output_format, convert_metadata):
        df = pd.read_excel(input_path) if input_path.endswith('.xlsx') else pd.read_csv(input_path)
        if output_format == "csv":
            df.to_csv(output_path, index=False)
        elif output_format == "xlsx":
            df.to_excel(output_path, index=False)
        elif output_format == "json":
            df.to_json(output_path, orient="records")
        # TODO: ODS, métadonnées tableur