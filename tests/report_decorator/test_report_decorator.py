from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    simple_report_test = ColoredReport(SimpleReport).generate(
        [
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
            },
        ]
    )
    assert (
        "\033[32mData de fabricação mais antiga:\033[0m" in simple_report_test
    )
    assert (
        "\033[32mData de validade mais próxima:\033[0m" in simple_report_test
    )
    assert "\033[32mEmpresa com mais produtos:\033[0m" in simple_report_test
    assert "\033[36m2022-05-04\033[0m" in simple_report_test
    assert "\033[36m2023-02-09\033[0m" in simple_report_test
    assert "\033[31mForces of Nature\033[0m" in simple_report_test
