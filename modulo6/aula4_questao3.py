frase = input("Digite uma frase: ")
vogais = sorted([letra for letra in frase if letra.lower() in 'aeiou'])
consoantes = [letra for letra in frase if letra.lower() not in 'aeiou ' and letra.isalpha()]
print("Vogais:", vogais)
print("Consoantes:", consoantes)
horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25
pagamentos = [ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora - 40) for hora in horas_trabalhadas]
print("Pagamentos:", pagamentos)
