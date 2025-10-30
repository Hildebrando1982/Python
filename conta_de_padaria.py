'''
Faça um programa que receba o valor total de uma compra e o valor do pagamento
e exiba o valor do troco
'''
valor_total = float(input('Digite o valor total: R$'))
valor_pagamento = float(input('Digite o valor do pagamento: R$'))

troco = valor_pagamento - valor_total

print(f'Troco: R$ {troco:.2f}')
