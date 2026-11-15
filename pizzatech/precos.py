LIMITE_DESCONTO = 100.0
PERCENTUAL_DESCONTO = 0.10


def calcular_total_bruto(itens):
    """Soma preço x quantidade. 'itens' é uma lista de pares (preco, quantidade)."""
    total = 0.0
    for preco, quantidade in itens:
        total += preco * quantidade
    return total


def calcular_desconto(total_bruto):
    """Retorna 10% de desconto se o total bruto for R$ 100,00 ou mais."""
    if total_bruto >= LIMITE_DESCONTO:
        return round(total_bruto * PERCENTUAL_DESCONTO, 2)
    return 0.0


def calcular_total_final(itens):
    """Retorna o total já com o desconto aplicado."""
    bruto = calcular_total_bruto(itens)
    return round(bruto - calcular_desconto(bruto), 2)