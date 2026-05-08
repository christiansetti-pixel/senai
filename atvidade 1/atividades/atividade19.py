qtd_frangos = int(input("digite a quantidade de frangos:"))

custo_chip = 4.0
custo_alimento = 3.50

gasto_por_frangos = custo_chip + (2 * custo_alimento)
gasto_total = qtd_frangos * gasto_por_frangos
print("A quantia de frangos na fazenda é: ", qtd_frangos)
print(f"para colocar a quantia desejada de aneis será preciso gastar: {gasto_total}")