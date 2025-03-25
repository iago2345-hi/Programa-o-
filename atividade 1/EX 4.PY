dias = int(input("Digite o número de dias que o carro foi alugado: "))
km = float(input("Digite o número total de quilômetros rodados: "))


pago = dias * 90


if km > 100:
    km_extra = km - 100
    custo_extra = km_extra * 12
else:
    custo_extra = 0




custo_total = pago + custo_extra


print(f"O custo total foi de : {custo_total} R$")


