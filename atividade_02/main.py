"""
Crie um programa que receba o nome do usuário e a idade informe o menu abaixo:
Sala 1 - a Roda Quadrada - Livre
Sala 2 - a Volta dos que não foram - 12 anos
Sala 3 - Poeira em Alto Mar - 14 anos
Sala 4 - As Tranças do Rei Careca - 16 anos
Sala 5 - A Vigança do Frango Assado - 18 anos
O usuário deverá escolher a sala do filme que deseja assistir, e o programa deverá:
- Liberar a entrada do usuário e encerrar, caso o usuário tenha a idade minima, ou maior.
- Bloquear a entrada do usuário e pedir para o mesmo escolher outro filme, caso não tenha a idade minima.
"""
#TODO 

while True:

    # Declaração das variáveis

    nome = input("Infome o nome: ")
    idade = int(input("Informe a Idade: "))

    # Salas

    print(f"{'*'*20} SALAS DOS CINEMA {'*'*20}")
    print("Sala 1 - A Roda Quadrada - Livre")
    print("Sala 2 - A Volta dos que não Foram - 12 anos")
    print("Sala 3 - Poeira em Alto Mar - 14 anos")
    print("Sala 4 - As Tranças do Rei Careca - 16 anos")
    print("Sala 5 - A vigança do Frango Assado - 18 anos")

    sala = input("Informe a opção de sala desejada")

    match sala:
        case "1":
            print(f"{nome} com a {idade} está liberado para assistir o filme ")
        case "2":
            print(f"")
        case "3":
           print(f"")
        case "4":
           print(f"")
        case "5":
            print(f"")
        case _:
            print("Operação Inválida")
            break