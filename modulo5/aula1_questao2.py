import random
import math
n = int(input("Digite a quantidade de valores aleatórios a serem gerados: "))
soma_valores = sum(random.randint(0, 100) for _ in range(n))
raiz_quadrada = math.sqrt(soma_valores)
print("A soma dos valores gerados é:", soma_valores)
print("A raiz quadrada da soma é:", raiz_quadrada)
