even_numbers = [x for x in range(20, 51) if x % 2 == 0]
squares = [x**2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
divisible_by_7 = [x for x in range(1, 101) if x % 7 == 0]
parity = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print("Números pares entre 20 e 50:", even_numbers)
print("Quadrados da lista [1, 2, 3, 4, 5, 6, 7, 8, 9]:", squares)
print("Números entre 1 e 100 divisíveis por 7:", divisible_by_7)
print("Paridade dos valores em range(0, 30, 3):", parity)
