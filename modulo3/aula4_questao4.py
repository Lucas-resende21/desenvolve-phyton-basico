distancia = int(input("Digite a distância da entrega em km: "))
peso = int(input("Digite o peso do pacote em kg: "))
if distancia <= 100:
    taxa = 1.0
elif 101 <= distancia <= 300:
    taxa = 1.5
else:
    taxa = 2.0
valor_frete = taxa * peso
if peso > 10:
    valor_frete += 10
print(f"O valor total do frete é: R${valor_frete:.2f}")
