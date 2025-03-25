numero = int(input("Digite um número inteiro maior que 1: "))


if numero <= 1:
    print("O número precisa ser maior que 1. Tente novamente.")
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
       
    if primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
