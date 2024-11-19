import random
from collections import Counter
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
interseccao = sorted(set(lista1) & set(lista2))
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista de interseção (ordenada):", interseccao)
print("\nFrequência dos elementos em cada lista:")
print("Lista 1:", dict(contagem_lista1))
print("Lista 2:", dict(contagem_lista2))
