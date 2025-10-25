'''
Você está desenvolvendo o sistema de bilheteria para um cinema. 
Os clientes podem ter direito a meia-entrada em duas situações:

Se tiverem menos de 18 anos
ou 
Se forem estudantes
Sua tarefa é criar um algoritmo que avalie as informações do 
cliente e exiba uma mensagem indicando se ele tem ou não direito ao desconto.
'''

idade = int(input('Digite a sua idade: '))
estudante = input('É estudante? (sim/não): ')
print(' ')

if idade < 18 or estudante == 'sim' or estudante == 'Sim' or estudante == 's' or estudante == 'S':
    print('Você tem direito ao desconto.')
elif idade > 18 and estudante == 'não' or estudante == 'Não' or estudante == 'n' or estudante == 'N':
    print('Você não tem direito ao desconto.')
else:
    print('Dados incorretos. Tente novamente.')
