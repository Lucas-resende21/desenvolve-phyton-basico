def main():
    print("Digite pelo menos 4 números inteiros. Digite 'sair' para finalizar a entrada.")
    
    numeros = []
    
    while True:
        entrada = input("Digite um número (ou 'sair' para finalizar): ")
        
        if entrada.lower() == 'sair':
            if len(numeros) < 4:
                print("Você precisa inserir pelo menos 4 números.")
                continue
            break
        
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    

    print("\nLista original:", numeros)
    print("Os 3 primeiros elementos:", numeros[:3])
    print("Os 2 últimos elementos:", numeros[-2:])
    print("Lista invertida:", numeros[::-1])
    print("Elementos de índice par:", numeros[::2])
    print("Elementos de índice ímpar:", numeros[1::2])

if __name__ == "__main__":
    main()
