import time
distancia = 100

any  or   0 
while distancia >= 0:
    print(f"distancia: {distancia} cm")
    if distancia > 10:
        print(" BIP!")
    elif 1 >= distancia <= 10:
        print(" BIP!")
        print(" BIP!")
        print(" BIP!")
        print("(perigo!)")
    else: 
        print("COLISAO!, você vai beter!")
    distancia -=10
    print(" "  * 20)
    print("você bateu!")
    time.sleep(1)