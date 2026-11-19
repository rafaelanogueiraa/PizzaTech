import pytest

from pizzatech.cardapio import Cardapio
from pizzatech.pizza import Pizza


def test_pizza_valida_e_criada_com_nome_e_preco():
    pizza = Pizza("Margherita", 40)
    assert pizza.nome == "Margherita"
    assert pizza.preco == 40.0


def test_pizza_com_nome_vazio_e_recusada():
    with pytest.raises(ValueError):
        Pizza("", 40)


def test_pizza_com_preco_zero_ou_negativo_e_recusada():
    with pytest.raises(ValueError):
        Pizza("Margherita", 0)
    with pytest.raises(ValueError):
        Pizza("Margherita", -10)


def test_cardapio_lista_pizzas_cadastradas():
    cardapio = Cardapio()
    cardapio.cadastrar(Pizza("Margherita", 40))
    cardapio.cadastrar(Pizza("Calabresa", 45))
    nomes = [pizza.nome for pizza in cardapio.listar()]
    assert nomes == ["Margherita", "Calabresa"]


def test_cardapio_recusa_nome_repetido():
    cardapio = Cardapio()
    cardapio.cadastrar(Pizza("Margherita", 40))
    with pytest.raises(ValueError):
        cardapio.cadastrar(Pizza("margherita", 50))


def test_cardapio_busca_retorna_pizza_ou_none():
    cardapio = Cardapio()
    cardapio.cadastrar(Pizza("Margherita", 40))
    assert cardapio.buscar("margherita").preco == 40.0
    assert cardapio.buscar("Portuguesa") is None