from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(product_list):
        company = SimpleReport.get_company_with_the_most_products(product_list)
        oldest_date = SimpleReport.get_the_oldest_fabrication_date(
            product_list
        )
        closest_date = SimpleReport.get_the_closest_expiration_date(
            product_list
        )

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )

    @classmethod
    def get_company_with_the_most_products(cls, list):
        companies_list = [company["nome_da_empresa"] for company in list]
        counter_companies = Counter(companies_list)
        """ most_common_company -> retorna uma lista de tuplas com valor e
            a quantidade que esse valor aparece"""
        most_common_company = counter_companies.most_common()
        company, times = most_common_company[0]  # desempacotamento da 1ª tupla
        return company

    @classmethod
    def get_the_oldest_fabrication_date(cls, list):
        fabrication_date_list_str = [
            date["data_de_fabricacao"] for date in list
        ]
        fabrication_date_list = [
            datetime.strptime(date, "%Y-%m-%d").date()
            for date in fabrication_date_list_str
        ]
        oldest_date = min(fabrication_date_list)  # menor data de fabricação
        return oldest_date

    @classmethod
    def get_the_closest_expiration_date(cls, list):
        expiration_date_list_str = [date["data_de_validade"] for date in list]
        expiration_date_list = [
            datetime.strptime(date, "%Y-%m-%d").date()
            for date in expiration_date_list_str
        ]
        earliest_date = min(expiration_date_list)  # menor data de validade
        return earliest_date
