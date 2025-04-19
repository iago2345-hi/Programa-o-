import json

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as file:
        json.dump(tarefas, file)

def adicionar_tarefa(descricao):
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": descricao, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa Acrescentada!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i + 1}. {tarefa['descricao']} - {status}")

def concluir_tarefa(numero):
    tarefas = carregar_tarefas()
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa concluída com sucesso!")
    else:
        print("Número Errado.")

adicionar_tarefa("Estudar para o ENEM")
listar_tarefas()
concluir_tarefa(1)
listar_tarefas()