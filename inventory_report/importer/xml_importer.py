from inventory_report.importer.importer import Importer
from pathlib import Path
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_path_suffix = Path(path).suffix

        if file_path_suffix != ".xml":
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            read_file = file.read()
            xml_dict = xmltodict.parse(read_file)
            product_list = xml_dict["dataset"]["record"]
            return product_list
