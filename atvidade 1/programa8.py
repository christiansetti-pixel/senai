nome = input("digite seu nome:")
idade = int(input("digite a sua idade:"))

if idade > 120:
    print(" opps algo deu errado digite nova mente ")
else:

dias_de_vida = idade * 365
print(f"olá {nome} ",dias_de_vida,"de sua vida")
