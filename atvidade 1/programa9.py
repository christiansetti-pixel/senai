nome = input("digite seu nome:")
idade = int(input("digite a sua idade:"))
while True: 
    if idade > 120 or  idade < o:
        print(" opps algo deu errado digite nova mente ")
        idade = int(input("digite a sua idade:"))
    else:
        break
dias_de_vida = idade * 365
print(f"olá {nome}, você já viveu cerca de: {dias_de_vida}")