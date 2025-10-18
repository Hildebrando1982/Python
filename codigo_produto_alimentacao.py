'''
Faça um programa utilizando um if aninhado que escreve o nome de um produto através do código digitado pelo usuário
Se o usuário digitar 1, o programa deverá escrever Pizza
Se o usuário digitar 2, o programa deverá escrever Hambuguer
Se o usuário digitar 3, o programa deverá escrever Refrigerante
Se o usuário digitar 4, o programa deverá escrever Batata Frita
'''

codigo = int(input("Digite o código do produto: "))

if codigo == 1:
    print ("Pizza")
elif codigo == 2:
    print ("Hamburguer")
elif codigo == 3:
    print ("Refrigerante")
elif codigo == 4:
    print ("Batata Frita")
else:
    print ("Código Inválido")
