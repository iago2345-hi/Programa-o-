compra_total = int(input("Qual o valor total das mercadorias compradas R$ : "))




if (compra_total <=500 ):
    print("Não há imposto!")
else:
    excedente = compra_total - 500
    imposto = excedente * 0.5
    print(f"O imposto aplicado é de R${imposto:.2f}.")

