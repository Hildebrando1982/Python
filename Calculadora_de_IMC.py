#Calculadora simples de IMC
#Desenvolvido por Hildebrando Marques


nome = input('Digite o seu nome: ')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

print(' ')
print('Olá', nome,)
print('Seu peso é', peso)
print('Sua altura é', altura)
print('Seu IMC é', imc)
print(' ')

if (imc < 18.5):
    print('IMC considerado muito baixo')
    print('Risco a sua saúde. Consulte um médico e um nutricionista')

elif (imc > 18.5) and (imc<=24.9):
    print('Você está com o peso normal')
    print('Mantenha seu peso com prática de atividade física e boa alimentação')

elif (imc > 24.9) and (imc <= 29.9):
    print('Você esta com sobrepeso')
    print('Risco a sua saúde. Consulte um médico e um nutricionista')

else:
    print('Você esta com obesidade')
    print('Risco a sua saúde. Consulte urgente um médico e um nutricionista')
    
print(' ')
