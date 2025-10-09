'''Faça um algoritmo que exiba o salário reajustado de um funcionário o percentual é o seguinte:
menor ou igual a 1000, o reajuste é de 35%
maior que 1000, o reajuste é de 15%'''


salario = float(input('Digite o seu salário: '))


if salario <= 1000.00:
    #Aqui é o calculo do salário reajustado, quando a condição é menor que 1000
    salario = salario * 1.35
    print('Seu salário reajustado é: ', round (salario, 2))
else:
    #Aqui é o calculo do salário reajustado, quando a condição é maior que 1000
    salario = salario * 1.15 
    print('Seu salário reajustado é: ', round (salario, 2)) 
    #a função round neste caso é para o resultado aparecer com duas casas decimais.
