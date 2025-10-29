'''
Faça um programa em estrutura while, no qual a pessoa digite qualquer número diferente de 0
e conte quantas vezes o 2 foi digitado e no final exibir na tela quantas vezes o 2  foi digitado.

'''

numero = int(input('Digite um número: '))
cont = 0

while numero != 0:
    if numero == 2:
        cont = cont + 1        
    numero = int(input('Digite um número: '))
print(f'O total de número 2 foi: {cont} vezes.')
