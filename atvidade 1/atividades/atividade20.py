qtd_blusas = int(input("digite a qtd_blusas necessárias: "))
metro_totais = qtd_blusas * 120
novelos = metro_totais // 125  

if metro_totais % 125 > 0:
   novelos += 1 

print(f"Total de novelos necessários: {novelos}")