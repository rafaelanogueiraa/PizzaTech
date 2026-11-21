import pytest

from pizzatech.cardapio import Cardapio
from pizzatech.pedido import Pedido
from pizzatech.pizza import Pizza


@pytest.fixture
def margherita():
    return Pizza("Margherita", 40)


@pytest.fixture
def pedido(margherita):
    cardapio = Cardapio()
    cardapio.cadastrar(margherita)
    return Pedido(cardapio)


def test_adicionar_item_valido(pedido, margherita):
    pedido.adicionar_item(margherita, 2)
    assert len(pedido.itens) == 1
    assert pedido.itens[0].quantidade == 2


def test_adicionar_pizza_fora_do_cardapio_e_recusado(pedido):
    with pytest.raises(ValueError):
        pedido.adicionar_item(Pizza("Portuguesa", 50), 1)


def test_quantidade_fora_do_limite_e_recusada(pedido, margherita):
    with pytest.raises(ValueError):
        pedido.adicionar_item(margherita, 0)
    with pytest.raises(ValueError):
        pedido.adicionar_item(margherita, 11)


def test_remover_item_existente(pedido, margherita):
    pedido.adicionar_item(margherita, 2)
    pedido.remover_item(margherita)
    assert pedido.itens == []


def test_remover_item_que_nao_esta_no_pedido_e_recusado(pedido, margherita):
    with pytest.raises(ValueError):
        pedido.remover_item(margherita)


def test_quantidade_nao_inteira_e_recusada(pedido, margherita):
    with pytest.raises(ValueError):
        pedido.adicionar_item(margherita, "dois")
