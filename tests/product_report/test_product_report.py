from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        2,
        "Ração Golden - gatos castrados frango",
        "PremieR Pet",
        "02-05-2022",
        "02-05-2024",
        "123456",
        "em local seco, fresco e arejado, ao abrigo da luz",
    )
    assert (
        str(product) == "O produto Ração Golden - gatos castrados frango"
        " fabricado em 02-05-2022"
        " por PremieR Pet com validade"
        " até 02-05-2024"
        " precisa ser armazenado em local seco, fresco e arejado,"
        " ao abrigo da luz."
    )
