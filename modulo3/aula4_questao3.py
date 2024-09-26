print("Digite um ano")
n1 = int(input())
if ((n1%4) == 0 and not(n1%100 == 0)):  
    print("É bissexto")
elif (n1%400 == 0):
    print("É bissexto")
else:
    print("Não é bissexto")
