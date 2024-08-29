valor = int(input("Escreva uma quantia em reais: "))
quant100 = valor // 100
print(f"{quant100} nota(s) de R$100,00")
resto = valor % 100
quant50 = resto // 50
print(f"{quant50} nota(s) de R$50,00")
resto = resto % 50
quant20 = resto // 20
print(f"{quant20} nota(s) de R$20,00")
resto = resto % 20
quant10 = resto // 10
print(f"{quant10} nota(s) de R$10,00")
resto = resto % 10
quant5 = resto // 5
print(f"{quant5} nota(s) de R$5,00")
resto = resto % 5
quant2 = resto // 2
print(f"{quant2} nota(s) de R$2,00")
resto = resto % 2
quant1 = resto // 1
print(f"{quant1} nota(s) de R$1,00")
resto = resto % 1

