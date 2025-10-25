'''
Você está desenvolvendo uma funcionalidade para um aplicativo de lanchonete.
O sistema precisa calcular o valor total de um pedido com base na quantidade de itens solicitados.

O cliente pode pedir:

Hambúrguer: R$ 12,00
Batata frita: R$ 7,00
Refrigerante: R$ 5,00
Sua tarefa é criar um algoritmo que armazene os dados necessários 
em variáveis e faça o cálculo do valor total com base nas quantidades informadas.
'''

print('Olá, seja bem-vindo!')
cliente = input ('Qual o seu nome? ')
print()
print(f'{cliente}, o preço dos lanches estão abaixo:')
print('----------------------------------------------')
print('Hamburguer -------- R$ 12,00')
print('Batata Frita -------R$ 7,00')
print('Refrigerante -------R$ 5,00')
print('----------------------------------------------')
print('')

hamburguer = 12
batata_frita = 7
refrigerante = 5

qte_hamburguer = int(input('Qual a quantidade de hamburguer desejado? '))
qte_batata_frita = int(input('Qual a quantidade de batata frita desejada? '))
qte_refrigerante = int(input('Qual a quantidade de refrigerante desejado? '))
print('')

total = (hamburguer * qte_hamburguer) + (batata_frita * qte_batata_frita) + (refrigerante + qte_refrigerante)

print(f'{cliente}, o total do pedido é R$ {total:.2f}')
