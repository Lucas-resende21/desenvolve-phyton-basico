frase = input("Digite uma frase: ")
frase_modificada = "".join("*" if letra.lower() in "aeiou" else letra for letra in frase)
print(f"Frase modificada: {frase_modificada}")
