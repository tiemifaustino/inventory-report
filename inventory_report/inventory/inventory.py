import csv

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        with open(path) as file:
            read_file = csv.DictReader(file)
            product_list = [product for product in read_file]

        if type == "simples":
            return SimpleReport.generate(product_list)
        if type == "completo":
            return CompleteReport.generate(product_list)
