import os
import math as m
"""
# TODO - Atividade: Crie um programa onte o usuário possa escolher as seguintes operações:
- Calcular área de um quadrado
- Calcular área de um retângulo
- Calcular área de um triângulo
- Calcular área de um trapézio
- Sair do programa
# NOTE - o usuário devera escolher a operação em um menu
# NOTE - o program deverá ser feito com funções
"""
def quadrado():
    q = m.l**2
    return q
def retangulo():
    r = m.b*m.h
    return r
def triangulo():
    t = (m.b*m.h)/2
    return t
def trapezio():
    tr = ((m.B + m.b)*m.h)/2
    return tr

while True:
    print("1 - Calcular área de um quadrado")
    print("2 - Calcular ára de um retàngulo")
    print("3 - Calcular área de um triângulo")
    print("4 - Calcular área de um trapézio")
    print("5 - Sair do programa")
    opcao = input("Informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")

    try:
        match opcao:
            case "1":
                l = float(input("Informe o valor do lado: ").replace(",", "."))
                print(f"área de um quadrado: {quadrado()}.")
                continue
            case "2":
                b = float(input("Informe o valor da base:"))
                h = float(input("Informe o valor da altura: "))
                print(f"A área de um retângulo: {retangulo}.")
                continue
            case "3":
                b = float(input("Informe o valor da base menor: "))
                h = float(input("Informe o valor da altura: "))
                print(f"Informe a área de um triângulo.")
                continue
            case "4":
                B = float(input("Informe o valor da base Maior: "))
                b = float(input("Informe o valor da base menor: "))
                h = float(input("Informe o valor da altura: "))
                print(f"Informe a área de um triângulo.")
                continue
            case "5":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue
    except Exception as e:
        print(f"Não foi possível executar o cálculo. {e}.")
        continue