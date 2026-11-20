class Cardapio:
    """Guarda as pizzas disponíveis para pedido."""

    def __init__(self):
        self._pizzas = {}

    def cadastrar(self, pizza):
        chave = pizza.nome.lower()
        if chave in self._pizzas:
            raise ValueError("Já existe uma pizza com esse nome no cardápio.")
        self._pizzas[chave] = pizza

    def listar(self):
        return list(self._pizzas.values())

    def buscar(self, nome):
        return self._pizzas.get(nome.strip().lower())

    def contem(self, pizza):
        return pizza.nome.lower() in self._pizzas