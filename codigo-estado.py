'''
Insira um código e classifique de acordo com a categoria.
1 ou 2 = sul
3 ou 4 = sudeste
5 ou 6 = norte
7 ou 8 = nordeste
9 ou 10 = centro-oeste
'''
codigo = int(input('Digite o código (1 a 10): '))

if codigo == 1 or codigo == 2:
    print('Sul')
elif codigo == 3 or codigo == 4:
    print('Sudeste')
elif codigo == 5 or codigo == 6:
    print('Norte')
elif codigo == 7 or codigo == 8:
    print('Nordeste')
elif codigo == 9 or codigo == 10:
    print('Centro-Oeste')
else:
    print('Número incorreto. Tente Novamente!')
