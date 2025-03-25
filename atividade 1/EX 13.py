salario_inicial = float(input("Digite o salário inicial: R$"))
aumento_percentual = float(input("Digite o aumento percentual inicial (em %): "))
anos = int(input("Digite o número de anos: "))


salario_atual = salario_inicial
for ano in range(anos):
    salario_atual += salario_atual * (aumento_percentual / 100)
    aumento_percentual *= 2  
   
print(f"O salário atual após {anos} anos é: R${salario_atual:.2f}")
