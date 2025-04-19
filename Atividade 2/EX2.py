import json

def carregar_estoque():
    try:
        with open("estoque.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open("estoque.json", "w") as file:
        json.dump(estoque, file)

def adicionar_produto(nome, quantidade, preco):
    estoque = carregar_estoque()
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar_estoque(estoque)
    print("Produto adicionado!")

def exibir_estoque():
    estoque = carregar_estoque()
    total = 0
    for produto in estoque:
        total += produto["quantidade"] * produto["preco"]
        print(f"{produto['nome']} - {produto['quantidade']} unidades - R${produto['preco']}")
    print(f"Valor total do estoque: R${total}")

adicionar_produto("Arroz", 10, 6)
adicionar_produto("Feijão", 5, 10)
adicionar_produto("Macarrão", 5, 15)
exibir_estoque()