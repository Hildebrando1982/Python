'''
Você está desenvolvendo um sistema para informar se a pessoa tem direito ao ingresso
pagando meia entrada ou inteira.

Sua tarefa é criar um algoritmo em linguagem python que use uma função para fazer 
essa conversão. 
idade < 18
estudante = True
idade >= 60
'''

def desconto():
  try:
    #insere idade e se é estudante
    idade = float(input('Digite a sua idade: '))
    estudante = input('Estudante? (sim/não): ').lower()
    print(' ')

    if idade < 18 or idade >= 60 or estudante == 'sim' or estudante == 's':
      print('Você tem direito a 50% de desconto.')
    else:
      print('Você deve pagar o valor inteiro do ingresso')
    

  except ValueError:
    #captura o erro em caso de digitação de letras ou simbolos no lugar de número
    print('----------------------------------------------------------')
    print('  Dados incorretos. Por favor, digitar um valor numerico.')
    print('----------------------------------------------------------')

desconto()
