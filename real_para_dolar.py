'''
Você está desenvolvendo um sistema de apoio para uma agência de viagens. 
Uma das funcionalidades mais solicitadas é um conversor de moedas. 
O usuário informa um valor em reais (R$) e o sistema precisa mostrar quanto 
isso representa em dólares (US$), usando uma taxa de câmbio definida pela empresa.

Sua tarefa é criar um algoritmo em linguagem python que use uma função para fazer 
essa conversão. A função deve receber o valor em reais e a taxa de câmbio como entrada, 
e retornar o valor convertido.
'''

def real_para_dolar():
  try:
    #insere os dados em reais R$
    real = float(input('Digite o valor em reais: '))
    dolar = float(input('Digite o valor em dolar: '))
    print(' ')

    #a fórmula para converter Real (R$) em Dolar (U$)
    dolar_conv = real/dolar
    
    print('------------------------------')
    print(f'R${real:.2f}')
    print(f'U${dolar_conv:.2f}')
    print('------------------------------')

  except ValueError:
    #captura o erro em caso de digitação de letras ou simbolos no lugar de número
    print('----------------------------------------------------------')
    print('  Dados incorretos. Por favor, digitar um valor numerico.')
    print('----------------------------------------------------------')

real_para_dolar()
