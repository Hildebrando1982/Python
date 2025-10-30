'''
Faça um programa em estrutura while, insira uma idade e
conte nas seguintes situações:
contar quando for maior que 15
contar quando for menor ou igual a 15
e exibir natela
'''
idade = int(input('Digite um número: ')) 
cont_maior_15 = 0
cont_menor_igual_15 = 0

while idade >= 0:
    if idade > 15:
        cont_maior_15 = cont_maior_15 + 1
        idade = int(input('Digite um número: '))
    else:
        cont_menor_igual_15 = cont_menor_igual_15 + 1
        idade = int(input('Digite um número: '))
print('Você digitou um número negativo')
print(f'Pessoas acima de 15 anos: {cont_maior_15}')
print(f'Pessoas abaixo de 15 anos: {cont_menor_igual_15}')
