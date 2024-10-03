n = int(input("Digite o número de participantes: "))
total = 0
i = n
while (i > 0):
    idade = int(input("Digite a idade do participante: "))
    total = total + idade
    i = i-1
media = total / n
print(media)