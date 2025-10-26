'''
Você foi contratado por uma cafeteria que deseja automatizar o atendimento no balcão. 
O sistema deve permitir que o atendente registre os pedidos de cada cliente, calcule 
o valor total e aplique um desconto de 10% para clientes cadastrados.

O processo deve funcionar da seguinte forma:

O atendente informa quantos itens o cliente vai pedir.
Para cada item, o sistema solicita o nome e o preço.
Ao final, o sistema pergunta se o cliente é cadastrado.
Se for, aplica o desconto e exibe o valor com desconto.
Caso contrário, exibe o valor cheio.
O desafio consiste em criar um algoritmo que represente essa lógica de forma completa.
'''

def cafeteria():
    try:
        #total igual a 0
        total = 0.0 
        
        #armazena a quantidade de itens pedidos
        qte_itens = int(input('Quantos itens o cliente deseja pedir? '))

        for i in range(qte_itens):
            nome = input(f'Nome do item {i+1}: ')
            valor = float(input(f'Digite o preço de {nome}: R$ '))
            total+= valor
        
        #mostra o valor total
        print(f'Valor total: R${total:.2f}')

        #pergunta se o cliente é cadastrado
        cliente = input('O cliente é cadastrado? (s/n): ').strip().lower()
        
        #se o cliente é cadastrado aplica-se o desconto de 10%
        if cliente == 's' or cliente == 'sim':
            desconto = total * 0.10
            desc_total = total - desconto
            print(f'Desconto aplicado: R${desconto:.2f}')
            print(f'Valor final com 10% de desconto: R${desc_total:.2f}')
        
        #se o cliente n~qo for cadastrado, aplica-se o total sem o desconto de 10%
        else:
            print(f'Valor final: R${total:.2f}')
        
        print(' ')
        print('-----FIM DO PROGRAMA-----')

    #Caso o cliente digite uma letra ao inves de número, receberá uma mensagem de erro
    except ValueError:
        print('Você digitou um valor incorreto.')
        print('Por favor, digite um valor numerico.')

cafeteria()
