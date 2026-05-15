import time
distancia = 100

any  or   0 
while distancia >= 0:
    print(f"distancia: {distancia} cm")
    if distancia > 10:
        print(" BIP!")
    elif 1 >= distancia <= 10:
        print(" Bip!")
        print(" BIP!")
        print(" Bip!")
        print("(perigo!)")
    else: 
        print("você vai bater")
        print("COLISAO!")
    distancia -=10
    print(""  * 20)
    print("você bateu!")
    time.sleep(1)