from inventory_report.importer.importer import Importer
from pathlib import Path
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_path_suffix = Path(path).suffix

        if file_path_suffix != ".json":
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            read_file = file.read()
            product_list = json.loads(read_file)
            return product_list
