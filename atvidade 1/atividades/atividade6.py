peso = float(input("digite o peso do prato :"))
peso_por_KG = 12
while True:
        if peso <= 0 or peso > 10:
            print("peso invalido : por favor digite um valor valido digite um valor entre 0 e 10 ")
            peso = float(input("digite o peso:"))
        else:
              break
total = peso * peso_por_KG
print("o valor a ser pago é:", total)
    