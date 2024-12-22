from collections import Counter
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
objetivo_counter = Counter(palavra_objetivo.lower())
palavras = frase.split()
anagramas = []
for palavra in palavras:
    if Counter(palavra.lower()) == objetivo_counter:
        anagramas.append(palavra)
print(f"Anagramas: {anagramas}")
