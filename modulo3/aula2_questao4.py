classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia(de 1 a 20): "))
resultado1 = classe == "guerreiro" and forca >=15 and magia <= 10
resultado2 = classe == "mago" and forca <=10 and magia >= 15
resultado3 = classe == "arqueiro" and forca >5 and magia > 5 and forca<16 and magia<16
final = resultado1 or resultado2 or resultado3
print(f"Pontos de atributo consistenstes com a classe escolhida: {final}")