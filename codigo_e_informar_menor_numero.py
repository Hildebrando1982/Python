'''
Faça um programa que receba dois números e execute as operações listadas a seguir, de acordo com a escolha do usuário:

código 1 ou 2 - informar o menor número
código 3 ou 4 - informar o menor número
outros códigos - relatar erro de código
'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
codigo = int(input ("Digite o código: "))

if codigo == 1  or codigo == 2:
    if n1 > n2:
        print(n1)
    else:
        print(n2)
elif codigo == 3  or codigo == 4:
    if n1<n2:
        print(n3)
    else:
        print(n4)
else:
    print("Código Inválido.")
