import csv
import json
import xmltodict


from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from pathlib import Path


class Inventory:
    @staticmethod
    def import_data(path, type):
        product_list = Inventory.verify_suffix(path)

        if type == "simples":
            return SimpleReport.generate(product_list)
        if type == "completo":
            return CompleteReport.generate(product_list)

    @classmethod
    def verify_suffix(cls, path):
        product_list = []
        file_path_suffix = Path(path).suffix

        with open(path) as file:
            if file_path_suffix == ".csv":
                read_file = csv.DictReader(file)
                product_list = [product for product in read_file]
            if file_path_suffix == ".json":
                read_file = file.read()
                product_list = json.loads(read_file)
            if file_path_suffix == ".xml":
                read_file = file.read()
                xml_dict = xmltodict.parse(read_file)
                product_list = xml_dict["dataset"]["record"]
        return product_list


"""
Source:
Extensão de arquivo em python
- Link: https://acervolima.com/como-obter-extensao-de-arquivo-em-python/
"""
