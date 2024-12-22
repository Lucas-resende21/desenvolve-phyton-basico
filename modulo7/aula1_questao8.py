def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = cpf.replace(".", "").replace("-", "")

    # Verifica se tem 11 dígitos ou é uma sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10

    # Verifica se os dígitos calculados conferem com os dígitos fornecidos
    return cpf[9] == str(primeiro_digito) and cpf[10] == str(segundo_digito)

# Solicita um CPF ao usuário
cpf = input("Digite um CPF (XXX.XXX.XXX-XX): ")

# Valida o CPF e exibe o resultado
if validar_cpf(cpf):
    print("Válido")
else:
    print("Inválido")