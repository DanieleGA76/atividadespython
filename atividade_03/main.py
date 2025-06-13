"""
Crie um programa que receba o nome, o peso e a altura do usuário, e informe seu IMC (Índice de Massa Corporal) e Informe seu diagnóstico de acordo com o valor de seu IMC:
- Magro demais
- Peso Normal
- Acima do Peso
- Obeso
- Obeso Nível II
- Obeso morbida
"""
#NOTE - DIVIRTAM-SE!! =D

#TODO 
try:
    # Declaração da variável
    nome = input("Infome o nome: ")
    peso = float(input("informe o peso: ").replace("," , "."))
    altura = float(input("informe a altura: ").replace("," , "."))
    md = "Magro demais"
    pn = "Peso Normal"
    ap = "Acima do Peso"
    o = "Obeso"
    on2 = "Obeso Nível I"
    om = "Obeso morbido"

    while True:
        print(f"{'+'*20} CALCULADORA DO IMC {'+'*20}")
        print(f"SE {nome} que possui {peso} e altura {altura} o seu IMC {md}.")
        print(f"SE {nome} que possui {peso} e altura {altura} o seu IMC {pn}.")
        print(f"SE {nome} que possui {peso} e altura {altura} o seu IMC {ap}.")
        print(f"SE {nome} que possui {peso} e altura {altura} o seu IMC {o}.")
        print(f"SE {nome} que possui {peso} e altura {altura} o seu IMC {on2}.")
        print(f"SE {nome} que possui {peso} e altura {altura} o seu IMC {om}.")

        imc = peso/altura**2