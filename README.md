# PizzaTech

Sistema de gerenciamento de pedidos de uma pizzaria fictícia, desenvolvido em **Python** como Trabalho Prático de Testes Automatizados da disciplina de Gestão da Qualidade de Software (UNIFENAS).

## Descrição

O PizzaTech permite que um atendente consulte o cardápio, monte um pedido, veja o total com desconto e finalize o pedido. A aplicação roda no terminal, sem interface gráfica e sem banco de dados, para manter o foco na lógica de negócio e nos testes automatizados.

## Objetivo

Desenvolver uma aplicação simples e organizada, com regras de negócio bem definidas, e verificá-la com testes unitários automatizados, seguindo o fluxo de trabalho Gitflow.

## Domínio da aplicação

Operação de pedidos de uma pizzaria: cardápio de pizzas, itens de pedido, cálculo de valores e finalização.

## Funcionalidades

- Cadastrar pizza no cardápio.
- Consultar o cardápio e buscar uma pizza pelo nome.
- Adicionar item ao pedido, com quantidade.
- Remover item do pedido.
- Calcular o total do pedido, com desconto.
- Finalizar o pedido.

## Regras de negócio

| Código | Regra |
|---|---|
| RN1 | A pizza precisa de nome não vazio e preço maior que zero. |
| RN2 | Não pode haver duas pizzas com o mesmo nome no cardápio. |
| RN3 | Só pizzas do cardápio podem entrar no pedido. |
| RN4 | A quantidade de cada item vai de 1 a 10. |
| RN5 | O total é a soma de preço x quantidade de cada item. |
| RN6 | Total bruto de R$ 100,00 ou mais recebe 10% de desconto. |
| RN7 | Não é possível finalizar um pedido vazio. |
| RN8 | Um pedido finalizado não pode mais ser alterado. |

## Fora do escopo

Pagamento real, delivery, banco de dados, interface gráfica e login.

## Tecnologias utilizadas

- Python 3.10 ou superior
- pytest (framework de testes)
- Git e GitHub (controle de versão, com Gitflow)
- Visual Studio Code

## Framework de testes

O projeto usa o **pytest**, escolhido por ser gratuito, simples de escrever e por mostrar de forma clara o que passou e o que falhou. Os testes ficam na pasta `tests/`, e a configuração está no arquivo `pytest.ini`.

## Estrutura do projeto

```
PizzaTech/
  pizzatech/
    __init__.py        versão do sistema
    pizza.py           classe Pizza (RN1)
    cardapio.py        classe Cardapio (RN2)
    pedido.py          classes ItemPedido e Pedido (RN3, RN4, RN7, RN8)
    precos.py          cálculo de total e desconto (RN5 e RN6)
    main.py            menu do terminal
  tests/
    test_pizza_cardapio.py
    test_precos.py
    test_pedido.py
    test_finalizar_pedido.py
  pytest.ini
  requirements.txt
  README.md
```

## Instalação

No PowerShell, em uma pasta de sua escolha:

```
git clone https://github.com/rafaelanogueiraa/PizzaTech.git
cd PizzaTech
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Depois da ativação, o início da linha do terminal mostra `(.venv)`.

## Como executar a aplicação

Com o ambiente virtual ativo, na pasta `PizzaTech`:

```
python -m pizzatech.main
```

O menu oferece: ver cardápio, adicionar item, remover item, ver pedido e total, finalizar pedido e sair. O cardápio de exemplo tem Margherita (R$ 40,00), Calabresa (R$ 45,00) e Portuguesa (R$ 50,00).

## Como executar os testes

Com o ambiente virtual ativo, na pasta `PizzaTech`:

```
python -m pytest -v
```

O resultado esperado é `21 passed`.

## Testes implementados

São 21 testes unitários, que cobrem entradas válidas, entradas inválidas, cálculos, retornos e tratamento de erros (`ValueError`).

| Arquivo | Testes | O que verifica |
|---|---|---|
| `test_pizza_cardapio.py` | 6 | Criação de pizza válida, recusa de nome vazio e de preço zero ou negativo, listagem do cardápio, recusa de nome repetido e busca por nome (RN1 e RN2). |
| `test_precos.py` | 5 | Total bruto, total sem desconto, desconto de 10% (R$ 105,00 vira R$ 94,50), desconto no limite exato de R$ 100,00 e total de pedido sem itens (RN5 e RN6). |
| `test_pedido.py` | 6 | Adição de item válido, recusa de pizza fora do cardápio, de quantidade fora do limite e de quantidade que não é número inteiro, remoção de item e recusa de remoção de item inexistente (RN3 e RN4). |
| `test_finalizar_pedido.py` | 4 | Finalização com itens, recusa de pedido vazio, bloqueio de alterações após finalizar e total com desconto (RN5, RN6, RN7 e RN8). |

## Fluxo de trabalho (Gitflow)

- `main`: versão estável, marcada com as tags `v1.0.0` e `v1.0.1`.
- `develop`: versão em desenvolvimento.
- `feature/*`: uma branch para cada funcionalidade ou conjunto de testes.
- `release/1.0.0`: preparação da primeira versão estável.
- `hotfix/quantidade-invalida`: correção de um defeito em que uma quantidade não numérica gerava `TypeError` em vez de `ValueError`.

## Equipe

Rafaela, Rodrigo, Leticia e Joane.