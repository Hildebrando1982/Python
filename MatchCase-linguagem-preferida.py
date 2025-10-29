'''
Faça um programa no qual escolha o nome da linguagem preferida.
Python : Você pode se tornar um cientista de dados.
PHP : Você pode se tornar um desenvolvedor backend.
Solidity : Você pode se tornar um desenvolvedor blackchain.
Java: Você pode se tornar um desenvolvedor de aplicativos mobile.
Outra Linguagem: A linguagem não importa, o que importa é resolver problemas.
'''

linguagem = input('Qual a sua linguagem preferida?:  ').lower()

match linguagem:
    case 'python':
        print('Você pode se tornar um cientista de dados.')
    case 'php':
        print('Você pode se tornar um desenvolvedor backend.')
    case 'solidity':
        print('Você pode se tornar um desenvolvedor blackchain.')
    case 'java':
        print('Você pode se tornar um desenvolvedor de aplicativos mobile.')
    case _:
        print('A linguagem não importa, o que importa é resolver problemas')
