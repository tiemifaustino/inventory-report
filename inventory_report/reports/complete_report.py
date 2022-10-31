from collections import Counter

from inventory_report.reports.simple_report import SimpleReport

# from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(product_list):
        products = SimpleReport.generate(product_list)
        companies = CompleteReport.get_product_list_by_company(product_list)
        return (
            f"{products}\n"
            f"Produtos estocados por empresa:\n{companies}"
        )

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


print(
    CompleteReport.generate(
        product_list=[
            {
                "id": 1,
                "nome_do_produto": "MESA",
                "nome_da_empresa": "Forces of Nature",
                "data_de_fabricacao": "2022-05-04",
                "data_de_validade": "2023-02-09",
                "numero_de_serie": "FR48",
                "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
            },
            {
                "id": 2,
                "nome_do_produto": "CADEIRA",
                "nome_da_empresa": "Forces of Nature",
                "data_de_fabricacao": "2022-07-04",
                "data_de_validade": "2023-09-09",
                "numero_de_serie": "LD123",
                "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
            },
            {
                "id": 3,
                "nome_do_produto": "GARRAFA",
                "nome_da_empresa": "My company",
                "data_de_fabricacao": "2022-08-01",
                "data_de_validade": "2023-10-01",
                "numero_de_serie": "4152",
                "instrucoes_de_armazenamento": "Não amassar",
            }
        ]
    )
)
