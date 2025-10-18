'''
Faça um programa que calcula e exibe o salário reajustado de um funcionário. Utilize o elif em sua resposta.

salário abaixo de R$ 1.412,00 - percentual de 45%
salário entre de R$ 1.412,00 e R$ 2000,00 - percentual de 25%
salário acima de R$ 2.000,00 - percentual de 45%
'''

salario = float(input("Qual é o seu salário? R$ "))

if salario < 1412.00:
    salario = salario * 1.45
    print(f"Aumento de 45%: R$ {salario:.2f}")
elif salario >= 1412.00 and salario < 2000.00 :
    salario = salario * 1.25
    print(f"Aumento de 25%: R$ {salario:.2f}")
else:
    salario = salario * 1.15
    print(f"Aumento de 15%: R$ {salario:.2f}")
