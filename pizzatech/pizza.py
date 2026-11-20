class Pizza:
    """Representa uma pizza do cardápio."""

    def __init__(self, nome, preco):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome da pizza não pode ser vazio.")
        if not isinstance(preco, (int, float)) or preco <= 0:
            raise ValueError("O preço da pizza deve ser maior que zero.")
        self.nome = nome.strip()
        self.preco = float(preco)