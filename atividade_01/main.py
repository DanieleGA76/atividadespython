"""
Crie um programa que receba do usuário dois números reais, e uma das 4 operações da matemática informadas pelo usuário, e faça o cálculo correspondente.
"""
#NOTE - O programa só se encerrará caso o usuário informe isso no programa.

#TODO 

while True:

    # declaração das variàveis

    x = float(input("Informar o valor de x: ").replace("," , "."))
    y = float(input("Informar o valor de y: ").replace("," , "."))
    
    # Menu
    print(f"{'-' *20} CALCULADORA PYTHON {'-'*20}")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisao\n")

    operador = input("Informe a opção desejada: ")

    # verificar a operação escohido e fa o cálculo

    match operador:

        case "1":
            print(f"O resultado da soma é: {x+y}.")
        case "2":
            print(f"O resultado da subtração é: {x-y}.")
        case "3":
            print(f"O resultao da multiplicação é: {x*y}.")
        case "4":
            print(f"O resultado da divisão é: {x/y}.")
        case _:
            print(f"Operador inválido.")
    
    repetir = input("Deseja fazer um novo calculo? (s/n).").lower().strip()

    match repetir:
        
        case "s":
            continue
        case "n":
            break
        case _:
            print("Opção inválido.")
            break