'''
Crie um programa que inserindo a quantidade de gols do jogo Náutico e Sport.
Exibir a vitória do time que tiver mais gols e exibir empate em caso de empate.
'''


gol_Nautico = input('Gols do Náutico: ')
gol_Sport = input('Gols do Sport: ')

if gol_Nautico > gol_Sport:
    print('Vitória do Náutico')
elif gol_Nautico == gol_Sport:
    print('Empate')
else:
    print('vitória do Sport')
