import random
numero_aleatorio = random.randint(1, 10)
print("Tente adivinhar o número entre 1 e 10!")
while True:
    palpite = int(input("Digite seu palpite: "))
    if palpite < numero_aleatorio:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_aleatorio:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você acertou o número.")
        break  
