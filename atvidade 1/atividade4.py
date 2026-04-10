import time

contador = 10

while contador >= 0:
    print("segagem iniciada:", contador, "segundos")
    time.sleep(1)  
    contador = contador - 1

print("secagem  concluído! A porta pode ser aberta .")