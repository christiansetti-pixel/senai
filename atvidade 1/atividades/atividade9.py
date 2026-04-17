P = 10
M = 12
G = 15


pequenas = int(input("Quantidade de camisetas PEQUENAS: "))
medias = int(input("Quantidade de camisetas MÉDIAS: "))
grandes = int(input("Quantidade de camisetas GRANDES: "))


if pequenas < 0 or medias < 0 or grandes < 0:
    print("Erro: não são permitidos valores negativos.")
else:
    total = pequenas * P + medias * M + grandes * G
    print(f"Valor arrecadado: R$ {total:.2f}")