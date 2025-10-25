'''
Converter ºC para ºF
'''

#insere os dados da temperatura em Celsius (ºC)
celsius = float(input('Digite a temperatura em Celsius: '))

#a fórmula para converter Celsius para Fahrenheit
fahrenheit = (celsius * (9/5)) + 32

print(f'{celsius:.1f}ºC é {fahrenheit:.1f}ºF')
