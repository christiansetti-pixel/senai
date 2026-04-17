preço_Pequeno = 10
preço_Medio = 12
preço_Grande = 15


quantidade_Pequeno = int(input("Quantidade de camisetas PEQUENAS: "))
quantidade_Medio= int(input("Quantidade de camisetas MÉDIAS: "))
quantidade_Grande = int(input("Quantidade de camisetas GRANDES: "))

valor_arrecadado = (quantidade_Pequeno * preço_Pequeno) + (quantidade_Medio * preço_Medio) + (quantidade_Grande * preço_Grande)
print("Valor total foi: ", valor_arrecadado)