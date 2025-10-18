'''
Um determinado clube de futebol pretende classificar seus atletas em categoria. para isso, o clube contatou você para criar 
um programa  que executasse essa tabela. Baseada na tabela de categorias do clube, construa um programa que solicite a idade 
de um atleta e imprima sua categoria

De 05 a 10 anos -  infantil
De 11 a 15 anos - juvenil
De 16 a 20 anos - profissional
'''

if idade >= 5 and idade <= 10:
    print("Infantil")
if idade >= 11 and idade <= 15:
    print("Juvenil")
if idade >= 16 and idade <= 20:
    print("Júnior")
if idade >= 21 and idade <= 25:
    print("Profissional")
if idade > 5 and idade > 25:
    print("Dados incorretos")
