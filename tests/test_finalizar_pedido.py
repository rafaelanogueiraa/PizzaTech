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


def test_finalizar_pedido_com_itens(pedido, margherita):
    pedido.adicionar_item(margherita, 1)
    total = pedido.finalizar()
    assert total == 40.0
    assert pedido.finalizado is True


def test_finalizar_pedido_vazio_e_recusado(pedido):
    with pytest.raises(ValueError):
        pedido.finalizar()


def test_pedido_finalizado_nao_aceita_alteracoes(pedido, margherita):
    pedido.adicionar_item(margherita, 1)
    pedido.finalizar()
    with pytest.raises(ValueError):
        pedido.adicionar_item(margherita, 1)
    with pytest.raises(ValueError):
        pedido.remover_item(margherita)


def test_total_do_pedido_aplica_desconto(pedido, margherita):
    pedido.adicionar_item(margherita, 3)
    assert pedido.calcular_total() == 108.0