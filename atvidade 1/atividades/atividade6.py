peso_prato = float(input("digite o valor do prato em KG :"))
valor_pagar = peso_prato * 12.0
while True:
        if peso_prato <= 0 or peso_prato > 10:
            print("peso invalido : por favor digite um valor valido digite um valor entre 0 e 10 ")
            peso_prato = float(input("digite o peso:"))
        else:
              break
total = peso_prato * valor_pagar 
print("o valor a ser pago é: ", total)
    