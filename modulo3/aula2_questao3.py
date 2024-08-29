idade = int(input("Digite sua idade: "))
numJogos = bool(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
numWins = int(input("Quantos jogos já venceu? "))
teste = (idade > 15 and idade < 19) and numJogos and numWins > 0
print(f"Apto para ingressar no clube de jogos de tabuleiro:{teste}")