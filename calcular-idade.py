'''
Crie um prograna que insira a idade
se for até 12 anos:  criança
se for 13 a 17 anos: adolescente
se for 18 a 59 anos: adulto
60 anos ou mais : idoso
'''

idade = int(input('Digite a sua idade: '))

if idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 17:
    print('Adolescente')
elif idade >= 18 and idade <= 59:
    print('Adulto')
else: 
    print('Idoso')
