from pizzatech.precos import calcular_total_final


class ItemPedido:
    """Uma pizza e a quantidade pedida dela."""

    def __init__(self, pizza, quantidade):
        self.pizza = pizza
        self.quantidade = quantidade


class Pedido:
    """Pedido montado a partir das pizzas do cardápio."""

    QUANTIDADE_MINIMA = 1
    QUANTIDADE_MAXIMA = 10

    def __init__(self, cardapio):
        self.cardapio = cardapio
        self.itens = []
        self.finalizado = False
        self.total_final = None

    def _verificar_nao_finalizado(self):
        if self.finalizado:
            raise ValueError("Um pedido finalizado não pode ser alterado.")

    def _buscar_item(self, pizza):
        for item in self.itens:
            if item.pizza.nome.lower() == pizza.nome.lower():
                return item
        return None


    def adicionar_item(self, pizza, quantidade):
        self._verificar_nao_finalizado()
        if not self.cardapio.contem(pizza):
            raise ValueError("A pizza não está no cardápio.")
        if not isinstance(quantidade, int):
            raise ValueError("A quantidade deve ser um número inteiro.")
        if not isinstance(quantidade, int):
            raise ValueError("A quantidade deve ser um número inteiro.")

        item = self._buscar_item(pizza)

        quantidade_final = quantidade + (item.quantidade if item else 0)
        if (
            not isinstance(quantidade, int)
            or quantidade < self.QUANTIDADE_MINIMA
            or quantidade_final > self.QUANTIDADE_MAXIMA
        ):
            raise ValueError("A quantidade de cada item deve ser de 1 a 10.")

        if item:
            item.quantidade = quantidade_final
        else:
            self.itens.append(ItemPedido(pizza, quantidade))

    def remover_item(self, pizza):
        self._verificar_nao_finalizado()
        item = self._buscar_item(pizza)
        if item is None:
            raise ValueError("O item não está no pedido.")
        self.itens.remove(item)

    def calcular_total(self):
        pares = [(item.pizza.preco, item.quantidade) for item in self.itens]
        return calcular_total_final(pares)

    def finalizar(self):
        self._verificar_nao_finalizado()
        if not self.itens:
            raise ValueError("Não é possível finalizar um pedido vazio.")
        self.total_final = self.calcular_total()
        self.finalizado = True
        return self.total_final