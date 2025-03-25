quantidade_turmas = int(input("Digite a quantidade de turmas: "))
alunos_por_turma = []


for i in range(1, quantidade_turmas + 1):
    alunos = int(input(f"Digite a quantidade de alunos na turma {i}: "))
    alunos_por_turma.append(alunos)
   
    if alunos > 40:
        print(f"Atenção: A turma {i} tem mais de 40 alunos.")


media_alunos = sum(alunos_por_turma) / quantidade_turmas


print(f"A média de alunos por turma é: {media_alunos:.2f}")


