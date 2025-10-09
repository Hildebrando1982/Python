'''
Crie um programa que leia 3 notas e calcular sua média.
Se a média for maior que 5, exiba aprovado e a média final
caos contrario, exiba reprovado e a média final
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 5:
    print('Aprovado. Média:', round(media, 2))
else:
    print('Reprovado. Média:', round(media, 2))
