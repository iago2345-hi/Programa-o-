assentos = {"A1": False, "A2": False, "B1": False, "B2": False}

def exibir_assentos():
    for assento, reservado in assentos.items():
        status = "✅ Reservado" if reservado else "🟢 Disponível"
        print(f"{assento}: {status}")

def reservar_assento(assento):
    if assento in assentos and not assentos[assento]:
        assentos[assento] = True
        print(f"Assento {assento} reservado!")
    else:
        print("Assento inválido ou já ocupado.")

exibir_assentos()
reservar_assento("A1")
exibir_assentos()