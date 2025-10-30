'''
Faça um programa que leia o código e a quantidade.
1- Caderno - R$12,00
2- Régua - R$2.50
3- Borracha - R$0,25
4- Mochila - R$50,00
No final exibir o valor total
O programa se encerrará quano o zero for digitado
'''

cod = -3

while cod != 0:

    cod = int(input('Digite o código: '))
    qte = int (input('Digite a quantidade: '))

    if cod == 1:
        total = float(12 * qte)
        print(f'Caderno - R$12,00. Total R$ {total:.2f}')
    elif cod == 2:
        total = float(2.5 * qte)
        print(f'Régua - R$2.50. Total R$ {total:.2f}')
    elif cod == 3:
        total = float(0.25 * qte)
        print(f'Borracha - R$0,25. Total R$ {total:.2f}')
    elif cod == 4:
        total = float(50 * qte)
        print(f'Mochila - R$50,00. Total R$ {total:.2f}')
    else:
        print('Código inválido. Tente Novamente')
print('Fim da Transação')
