from inventory_report.importer.importer import Importer
from pathlib import Path
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_path_suffix = Path(path).suffix

        if file_path_suffix != ".csv":
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            read_file = csv.DictReader(file)
            product_list = [product for product in read_file]
            return product_list
