'''
Converter ºC para ºF
'''

def celsius_para_fahrenheit():
  try:
    #insere os dados da temperatura em Celsius (ºC)
    celsius = float(input('Digite a temperatura em Celsius: '))

    #a fórmula para converter Celsius para Fahrenheit
    fahrenheit = (celsius * (9/5)) + 32
      
    print(f'{celsius:.1f}ºC é {fahrenheit:.1f}ºF')

  except ValueError:
    #captura o erro em caso de digitação de letras ou simbolos no lugar de número
    print('Dados incorretos. Por favor, digitar um valor numerico.')

celsius_para_fahrenheit()
