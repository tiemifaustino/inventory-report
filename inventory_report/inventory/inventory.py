import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from pathlib import Path


class Inventory:
    @staticmethod
    def import_data(path, type):
        product_list = []
        file_path_suffix = Path(path).suffix

        if file_path_suffix == ".csv":
            with open(path) as file:
                read_file = csv.DictReader(file)
                product_list = [product for product in read_file]
        if file_path_suffix == ".json":
            with open(path) as file:
                read_file = file.read()
                product_list = json.loads(read_file)

        if type == "simples":
            return SimpleReport.generate(product_list)
        if type == "completo":
            return CompleteReport.generate(product_list)
