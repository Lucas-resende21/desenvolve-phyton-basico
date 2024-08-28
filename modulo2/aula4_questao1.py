#Lê o comprimento do terreno do teclado, transforma em int e armazena em comprimento.
comprimento = int(input("Insira o comprimento do terreno: "))
#Lê a largura do terreno do teclado, transforma em int e armazena em largura.
largura = int(input("Insira a largura do terreno: "))
#Lê o preço do metro quadrado do teclado, transforma em float e armazena em preço.
preco = float(input("Insira o preço do metro quadrado na região: "))
print(f"O terreno possui {largura*comprimento}m2 e custa R${largura*comprimento*preco}")