A'''
Você está desenvolvendo o sistema de bilheteria para um cinema. 
Os clientes podem ter direito a meia-entrada em duas situações:

Se tiverem menos de 18 anos
ou 
Se forem estudantes
Sua tarefa é criar um algoritmo que avalie as informações do 
cliente e exiba uma mensagem indicando se ele tem ou não direito ao desconto.
'''

idade = int(input('Digite a sua idade: '))
estudante_input = input('É estudante? (sim/não): ')
ingresso = 40

print('\n')

# Normaliza a resposta do usuário para minúsculas
estudante = estudante_input.lower()

# Verifica se a pessoa tem direito a meia-entrada
if idade < 18 or estudante == 'sim' or estudante == 's':
    print('Você tem direito ao desconto.')
    print(f'Total a pagar: R$ {ingresso / 2:.2f}')
# Verifica se a pessoa não tem direito (maior de 18 E não estudante)
elif idade >= 18 and (estudante == 'não' or estudante == 'nao' or estudante == 'n'):
    print('Você não tem direito ao desconto.')
    print(f'Total a pagar R$ {ingresso:.2f}')
# Caso a entrada para estudante seja inválida
else:
    print('Dados incorretos. Tente novamente.')
