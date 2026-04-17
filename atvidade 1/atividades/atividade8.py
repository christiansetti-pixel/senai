numero1 = input(" 1ª nota (peso 1):")
numero2 = input(" 2ª nota (peso 1):")
numero3 = input(" 3ª nota (peso 1):")

if float(numero1) < 0 or float(numero2) < 0 or float(numero3) < 0:
    print("Erro: não são permitidos valores negativos.")
else:
    media = (float(numero1) * 1 + float(numero2) * 2 + float(numero3) * 3) / (1 + 2 + 3)
print(f"media ponderada: {media:.2f}")