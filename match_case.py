'''
Usando o match case, faça um programa que pergunta ao usuário qual sua linguagem de programação preferida. 
A partir da linguagem escolhida, mostre ao lado:

Python - Você pode se tornar um cientista de dados.
PHP - Você pode se tornar um desenvolvedor backend.
Solidity - Você pode se tornar um desenvolvedor blockchain.
Java - Você pode se tornar um desenvolvedor de aplicativos mobile.
'''

resposta = input("Qual a sua linguagem de programação:  ")

match resposta:
    case "Python" | "python" | "PYTHON":
        print("Você pode se tornar um cientista de dados.")
    case "PHP" | "php":
        print("Você pode se tornar um desenvolvedor backend.")
    case "Solidity" | "solidity" | "SOLIDITY":
        print("Você pode se tornar um desenvolvedor blockchain." )  
    case "Java" | "java" | "JAVA":
        print("Você pode se tornar um desenvolvedor de aplicativos mobile.")
    case _:
        print("A linguagem não importa, o que importa é resolver programas.")
