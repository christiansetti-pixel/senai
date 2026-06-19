print("--- RPG BATTLE SYSTEM: ESTAMINA CONTROL ---")
estamina_atual = 100

while True:
    print(f"\nSua Estamina Atual: {estamina_atual}/100")
    print("[1] Atacar (-30) | [2] Usar Poção (+40) | [3] Sair")
    opcao = input("Escolha uma ação: ")

    if opcao == "1":
        print("Você realizou um ataque devastador!")
        estamina_atual = estamina_atual - 30

        if estamina_atual <= 0:
            estamina_atual = 0
            print("Você está sem estamina!")

    elif opcao == "2":
        print("Você bebeu uma poção de energia!")
        estamina_atual = estamina_atual + 40

        if estamina_atual > 100:
            estamina_atual = 100
            print("Sua estamina já está cheia!")

    elif opcao == "3":
        print("Fim de jogo.")
        break