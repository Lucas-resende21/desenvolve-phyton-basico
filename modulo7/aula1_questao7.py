import random
from collections import Counter
def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_cript = []
    for nome in nomes:
        nome_cript = "".join(
            chr(((ord(c) - 33 + chave) % 94) + 33) for c in nome
        )
        nomes_cript.append(nome_cript)

    return nomes_cript, chave
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
objetivo_counter = Counter(palavra_objetivo.lower())
palavras = frase.split()
anagramas = []
for palavra in palavras:
    if Counter(palavra.lower()) == objetivo_counter:
        anagramas.append(palavra)
print(f"Anagramas: {anagramas}")
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)
print(f"Nomes criptografados: {nomes_cript}")
print(f"Chave de criptografia: {chave_aleatoria}")
