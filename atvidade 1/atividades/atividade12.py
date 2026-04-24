salario = float(input("digite o seu salário atual:"))

x = salario * 0.15 
aumento = salario + x 
imposto = aumento * 0.08 
salario_final = aumento - imposto
print("o seu salário sem aumento era:",salario)
print(f"o seu salário com aumento ficou:",aumento)
print(f"o seu salário final ficou:",salario_final)