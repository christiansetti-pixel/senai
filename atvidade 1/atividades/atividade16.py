qtd_sanduiche = int(input("digite a quantidade de sanduiches a fazer:"))
peso_quaijo = 50
peso_presunto = 50
peso_carne = 100

total_queijo = (qtd_sanduiche * 2 * peso_quaijo) / 1000
total_presunto = (qtd_sanduiche * 1 * peso_presunto) / 1000
total_carne = (qtd_sanduiche * 1 * peso_carne) / 1000

print(f"para produzir{qtd_sanduiche} sanduiches, você pecisa de :")
print(f"- queijo:  {total_queijo} kg de queijo")
print(f"-  presunto: {total_presunto} kg de presunto")
print(f"- carne: {total_carne} kg de carne")