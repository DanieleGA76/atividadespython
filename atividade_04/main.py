import os

# TODO - Atividade
"""
Crie um programa em que o usuário pode escolher entre:
- Inserir um nome em uma lista
- Exibir a lista de nomes
- Pesquisar por um nome na lista
- Alterar item da lista
- Excluir item da lista.
- sair do programa.
"""
# NOTE - a lista deve começar vazia.
# NOTE - Todos os nomes dever ser inseridos pelo uusario.
# NOTE - Divistam-se!!! =D



nomes = []

while True:
    print(f"{'&'*20} Lista de nomes {'&'*20}")
    print("1 - Informe o nome: ")
    print("2 - Exibir lista")
    print("3 - Pesquisar nome na lista")
    print("4 - Alteração nome da lista")
    print("5 - Excluir nome da lista")
    print("6 - Sair do programa")

    opcao = input("opção desejada: ").strip()

    os.system("cls")
    match opcao:
        case "1":
            novo_nome = input("informe o nome a ser cadastrado: ").strip().title()
            os.system("cls")
            try:
                nomes.append(novo_nome)
                print(f"{novo_nome} inserido com sucesso.")
            except Exception as e:
                print(f"Não foi possível inserir nome na lista. {e}.")
            finally:
                continue 
        case "2":
            try:
                print("\nLista:\n")
                for nome in nomes:
                    print(nome)
                print("\n")
            except Exception as e:
                print(f"Não foi possível exibir a lista.{e}.")
            finally:
                continue
        case "3":
            nome_pesquisado = input("Informe o nome a ser pesquisado: ").title().strip()
            os.system("cls")
            result = nomes.count(nome_pesquisado)
            print(f"{nome_pesquisado} foi encontrado {result} vezes.")
            continue
        case "4":
            for i in range(len(nomes)):
                print(f"Indice{i}: {nomes[i]}.")
            try:
                i = int(input("Informe o número do índice a ser alterado: "))
                os.system("cls")
                if i >= 0 and i < len(nomes):
                    nomes[i] = input(" Informe o novo nome as ser alterado: ")
                    os.system("cls")
                    print("Nome alterado com sucesso.\n")
                else:
                    print(f"Valor do índice inválido.")
            except Exception as e:
                print(f"Não foi possível executar a operação. {e}.")
            finally:
                print("\n nova lista:\n")
                for i in range(len(nomes)):
                    print(f"Indice{i}: {nomes[i]}.")
        case "5":
            for i in range(len(nomes)):
                print(f"Indice{i}: {nomes[i]}.")
            try:
                i = int(input("Informe o indice que deseja excluir: "))
                os.system("cls")
                if i>= 0 and i < len(nomes):
                    print(f"Nome a ser excluido: {nomes[i]}")
                    confirma = input(f"Deseja excluir {nomes[i]}? (s/n)").lower().strip()
                    os.system("cls")
                    match confirma:
                        case "s":
                            nome_excluido = nomes[i]
                            del(nomes[i])
                            print(f"nome {nome_excluido} excluido com sucesso.")
                        case "n":
                            print(f"{nomes[i]} não será excluido..")
                        case _:
                            print("Opção inválida")
                else:
                    print("Indice inválido.")
            except Exception as e:
                print(f"Não foi possível excluir nome. {e}.")
            finally:
                print(f"Nova Lista: \n")
                for i in range(len(nomes)):
                    print(f"Indice{i}: {nomes[i]}.")
        case "6":
            print("Programa encerrado! ;)")
            break
        case _:
            print("Opção inválida.")
            continue


""" 
lista = []
nome = input("Informe o nome: ").capitalize().strip()
    lista.append(nome)
    print(f"{nome} inserido na lista com sucesso!")
    adicionar = input("Deseja adicionar outro nome? (s/n)").lower().strip()
    match adicionar:
        case "s":
            continue
        case "n":
            break
        case _:
            print("comanddo inválido!")
            continue
lista.sort()
for nome in lista:
    print(nome)
pesquisa = input("Informe o nome a ser pesquisado: ").title().strip()
if pesquisa in lista:
    print(f"{pesquisa} encontrado!")
else:
    print(f"{pesquisa} não encontrado.")
"""