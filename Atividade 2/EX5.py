import json

def carregar_contatos():
    try:
        with open("contatos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_contatos(contatos):
    with open("contatos.json", "w") as file:
        json.dump(contatos, file)

def adicionar_contato(nome, telefone, email):
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)
    print("Contato adicionado!")

def buscar_contato(nome):
    contatos = carregar_contatos()
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
            return
    print("Contato não encontrado.")

adicionar_contato("Iago", "66666-66666", "Iagoleonam@email.com")
buscar_contato("Iago")