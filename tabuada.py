'''
Crie um programa que solicite ao susário um número e exiba a tabuada
desse número de 1 a 10
'''

numero = int(input('Digite '))
for i in range (1,11):
    print(f'{numero} * {i} = {numero * i}')
