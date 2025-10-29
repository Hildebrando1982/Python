'''
Insira 2 números.
Escolha a operação + - * /
Use o Match Case
'''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
op = input('Digite a operação (+, -, *, /): ')

match op:
    case '+':
        print(n1+n2)
    case '-':
        print(n1-n2)
    case '*':
        print(n1*n2)
    case '/':
        print(n1/n2)
    case _:
        print('Caracter inválido. Tente novamente.')
