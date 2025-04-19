usuarios = {"Iago": {"senha": "iago@etepd", "saldo": 10000}}

def login(usuario, senha):
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        return usuario
    print("Usuário ou senha incorretos.")
    return None

def depositar(usuario, valor):
    usuarios[usuario]["saldo"] += valor
    print(f"Depósito realizado! Novo saldo: R${usuarios[usuario]['saldo']}")

def sacar(usuario, valor):
    if usuarios[usuario]["saldo"] >= valor:
        usuarios[usuario]["saldo"] -= valor
        print(f"Saque realizado! Novo saldo: R${usuarios[usuario]['saldo']}")
    else:
        print("Saldo insuficiente.")

usuario_logado = login("Iago", "iago@etepd")
if usuario_logado:
    depositar(usuario_logado, 50)
    sacar(usuario_logado, 30)