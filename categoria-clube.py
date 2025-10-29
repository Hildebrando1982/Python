'''
Insira uma idade e classifique de acordo com a categoria.
5 a 10 = infantil
11 a 15 = juvenil
16 a 20 = júnior
21 a 25 = profissional
'''
idade = int(input('Digite a sua idade: '))

if idade >= 5 and idade <= 10:
    print('Infantil')
elif idade >= 11 and idade <= 15:
    print('Juvenil')
elif idade >= 16 and idade <= 20:
    print('Júnior')
elif idade >= 21 and idade <= 25:
    print('Profissional')
else:
    print('Idade não contemplada na categoria!')
