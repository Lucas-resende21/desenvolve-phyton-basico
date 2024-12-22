frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador = 0
indices = []
for i, letra in enumerate(frase):
    if letra in vogais:
        contador += 1
        indices.append(i)
print(f"{contador} vogais")
print(f"Índices {indices}")
