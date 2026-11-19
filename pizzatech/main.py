from pizzatech.cardapio import Cardapio
from pizzatech.pedido import Pedido
from pizzatech.pizza import Pizza


def montar_cardapio():
    cardapio = Cardapio()
    cardapio.cadastrar(Pizza("Margherita", 40.0))
    cardapio.cadastrar(Pizza("Calabresa", 45.0))
    cardapio.cadastrar(Pizza("Portuguesa", 50.0))
    return cardapio


def mostrar_cardapio(cardapio):
    print("\n--- Cardápio ---")
    for pizza in cardapio.listar():
        print(f"{pizza.nome}: R$ {pizza.preco:.2f}")


def mostrar_pedido(pedido):
    print("\n--- Pedido ---")
    if not pedido.itens:
        print("O pedido está vazio.")
    for item in pedido.itens:
        print(f"{item.quantidade}x {item.pizza.nome}")
    print(f"Total com desconto: R$ {pedido.calcular_total():.2f}")


def ler_pizza(cardapio):
    nome = input("Nome da pizza: ")
    pizza = cardapio.buscar(nome)
    if pizza is None:
        raise ValueError("A pizza não está no cardápio.")
    return pizza


def executar():
    cardapio = montar_cardapio()
    pedido = Pedido(cardapio)
    while True:
        print("\n1) Ver cardápio  2) Adicionar item  3) Remover item")
        print("4) Ver pedido e total  5) Finalizar pedido  0) Sair")
        opcao = input("Escolha: ").strip()
        try:
            if opcao == "1":
                mostrar_cardapio(cardapio)
            elif opcao == "2":
                pizza = ler_pizza(cardapio)
                pedido.adicionar_item(pizza, int(input("Quantidade: ")))
                print("Item adicionado.")
            elif opcao == "3":
                pedido.remover_item(ler_pizza(cardapio))
                print("Item removido.")
            elif opcao == "4":
                mostrar_pedido(pedido)
            elif opcao == "5":
                total = pedido.finalizar()
                print(f"Pedido finalizado! Total: R$ {total:.2f}")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    executar()