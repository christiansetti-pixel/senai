x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

diferenca_x = x2 - x1
diferenca_y = y2 - y1

distancia = (diferenca_x ** 2 + diferenca_y ** 2) ** 0.5

print("A diferença entre os pontos é:", distancia)
