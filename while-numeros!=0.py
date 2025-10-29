'''
Faça um programa que leia números diferntes de 0 usando a estrutura while e exibir na tela
Se escrever 0 escrever fim.
'''

numero = int(input('Digite um número: ')) 

while numero != 0:
    print(numero)
    numero = int(input('Digite um número: ')) 

print('--- Fim ---')
