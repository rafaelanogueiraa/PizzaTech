from pizzatech.precos import (
    calcular_desconto,
    calcular_total_bruto,
    calcular_total_final,
)


def test_total_bruto_soma_preco_vezes_quantidade():
    assert calcular_total_bruto([(40, 2), (25, 1)]) == 105


def test_total_sem_desconto_abaixo_de_100():
    assert calcular_total_final([(40, 1)]) == 40.0


def test_total_com_desconto_de_10_por_cento():
    assert calcular_total_final([(40, 2), (25, 1)]) == 94.5


def test_desconto_aplicado_no_limite_exato_de_100():
    assert calcular_total_final([(50, 2)]) == 90.0


def test_total_de_pedido_sem_itens_e_zero():
    assert calcular_total_final([]) == 0.0
    assert calcular_desconto(0) == 0.0