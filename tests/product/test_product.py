from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        2,
        "Ração Golden - gatos castrados frango",
        "PremieR Pet",
        "2022-05-02",
        "2024-05-02",
        "123456",
        "Conservar em local seco, fresco e arejado, ao abrigo da luz",
    )
    assert product.id == 2
    assert product.nome_do_produto == "Ração Golden - gatos castrados frango"
    assert product.nome_da_empresa == "PremieR Pet"
    assert product.data_de_fabricacao == "2022-05-02"
    assert product.data_de_validade == "2024-05-02"
    assert product.numero_de_serie == "123456"
    assert (
        product.instrucoes_de_armazenamento
        == "Conservar em local seco, fresco e arejado, ao abrigo da luz"
    )
