import random
lista = [random.randint(-10, 10) for _ in range(20)]
def encontrar_intervalo_negativos(lista):
    max_negativos = 0
    intervalo_inicial = 0
    intervalo_final = 0
    
    for i in range(len(lista)):
        for j in range(i + 1, len(lista) + 1):
            intervalo = lista[i:j]
            quantidade_negativos = sum(1 for x in intervalo if x < 0)
            if quantidade_negativos > max_negativos:
                max_negativos = quantidade_negativos
                intervalo_inicial, intervalo_final = i, j
    return intervalo_inicial, intervalo_final
inicio, fim = encontrar_intervalo_negativos(lista)
print("Lista original:", lista)
print(f"Intervalo encontrado com mais negativos: {lista[inicio:fim]}")
del lista[inicio:fim]
print("Lista após deleção:", lista)
