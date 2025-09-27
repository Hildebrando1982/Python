import math # Importa a biblioteca math para usar sqrt

def bhaskara():
    # Recebe os coeficientes da equação
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    # Exibe a equação formatada
    print("\nA equação é: ", end="")
    
    # Termo com 'a' (sempre presente, a menos que seja 1)
    if a != 0:
        if a == 1:
            print("x² ", end="")
        elif a == -1:
            print("-x² ", end="")
        else:
            print(f"{a}x² ", end="")
    
    # Termo com 'b'
    if b > 0:
        if b == 1 and a != 0:
            print(f"+ x ", end="")
        elif a != 0:
            print(f"+ {b}x ", end="")
        elif b == 1 and a == 0:
            print("x ", end="")
        else:
            print(f"{b}x ", end="")
    elif b < 0:
        if b == -1 and a != 0:
            print(f"- x ", end="")
        elif a != 0:
            print(f"- {-b}x ", end="")
        elif b == -1 and a == 0:
            print("- x ", end="")
        else:
            print(f"{b}x ", end="")

    # Termo com 'c'
    if c > 0 and (a != 0 or b != 0):
        print(f"+ {c} = 0")
    elif c < 0:
        print(f"{c} = 0")
    elif c == 0 and (a != 0 or b != 0):
        print("= 0")
    elif c == 0 and a == 0 and b == 0:
        print("= 0")
    else:
        print("= 0")

    # Calcula o discriminante (delta)
    delta = b**2 - 4*a*c

    # Verifica o valor de delta para encontrar as raízes
    if delta < 0:
        print("O delta é negativo. Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"O delta é zero. Existe uma única raiz real: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes reais são: x1 = {x1} e x2 = {x2}")

# Chama a função para executar o cálculo
bhaskara()
