from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(product_list):
        products = SimpleReport.generate(product_list)
        companies = CompleteReport.get_product_list_by_company(product_list)
        return f"{products}\n" f"Produtos estocados por empresa:\n{companies}"

    @classmethod
    def get_product_list_by_company(cls, list):
        companies_list = [company["nome_da_empresa"] for company in list]
        counter_companies = Counter(companies_list)
        most_common_company = counter_companies.most_common()
        list_by_company = ""
        for common_company in most_common_company:
            company, times = common_company
            list_by_company += f"- {company}: {times}\n"
        return list_by_company
