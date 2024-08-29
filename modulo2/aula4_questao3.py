produto1 = input("Digite o nome do produto 1: ")
precop1 = float(input("Digite o preço unitário do produto 1: "))
quantp1 = int(input("Digite a quantidade do produto 1: "))
total = precop1*quantp1
produto1 = input("Digite o nome do produto 2: ")
precop1 = float(input("Digite o preço unitário do produto 2: "))
quantp1 = int(input("Digite a quantidade do produto 2: "))
total = total + precop1*quantp1
produto1 = input("Digite o nome do produto 3: ")
precop1 = float(input("Digite o preço unitário do produto 3: "))
quantp1 = int(input("Digite a quantidade do produto 3: "))
total = total + precop1*quantp1
print(f"Total: R${total:,.2f}")
