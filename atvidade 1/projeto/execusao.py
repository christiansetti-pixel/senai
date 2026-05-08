distancia = 100

maior or igaul a 0 
while distancia >= 0:
    print(f"distancia: {distancia} cm")
    if distancia > 10:
        print(" BIP!")
    elif 1 >= distancia <= 10:
        print(" BIP! BIP! BIP! ( PERIGO )")
    else: 
        print("COLISAO!")
    distancia -=10
    print("-"  * 20)
    