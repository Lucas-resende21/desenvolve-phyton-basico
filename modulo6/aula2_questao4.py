lista1 = input("Digite os números da primeira lista separados por espaço: ").split()
lista2 = input("Digite os números da segunda lista separados por espaço: ").split()
lista1 = [int(x) for x in lista1]
lista2 = [int(x) for x in lista2]
lista_intercalada = []
len_menor = min(len(lista1), len(lista2))
for i in range(len_menor):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
if len(lista1) > len(lista2):
    lista_intercalada.extend(lista1[len_menor:])
else:
    lista_intercalada.extend(lista2[len_menor:])
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista intercalada:", lista_intercalada)
