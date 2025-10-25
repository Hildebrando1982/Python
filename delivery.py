'''
Você está desenvolvendo um sistema para uma empresa de delivery.
 O valor da taxa de entrega depende da distância até o cliente e se o pedido foi feito em um dia de chuva.

As regras são:

Para entregas até 5 km, a taxa é R$ 5,00.
Entre 5 e 10 km, a taxa é R$ 8,00.
Acima de 10 km, a taxa é R$ 10,00.
Se estiver chovendo, acrescenta R$ 2,00 à taxa padrão.
O desafio desta atividade é criar um algoritmo em python que informe o valor final da entrega.

'''

distancia = float(input('Qual a distância em km? '))
chovendo = input('Está chovendo? (sim/não): ').lower()
taxa = 0

if distancia <= 5:
    taxa = 5.00
elif distancia <= 10:
    taxa = 8.00
else:
    taxa = 10.00

if chovendo == 'sim' or chovendo == 's':
    taxa = taxa + 2

print(f'Total a pagar R$ {taxa:.2f}')
