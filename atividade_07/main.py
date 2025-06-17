
import os
"""
# TODO - atividade: Crie um programa que faça as seguintes operações:
- Inserir dados de novo usuário
- Exibir lista de usuários
- Alterar dados de um usuário já cadastrado
- Excluir usuário da lista
- Sair do programa
Os dados a serm cadastrados serão os seguintes:
- Nome
- Data de Nascimento
- E-mail
- CPF
- Telefone
- Profissão
- Gênero
# NOTE - a lista deve começar vazia
"""
chaves = ('Nome', 'Data de Nascimento', 'e-mail', 'CPF', 'Telefone', 'Profissão', 'Gênero')
pessoas = []

while True:
    pessoa = {}
    print(f"{'#'*20} CADASTRO{'#'*20}")
    print("1 - Inserir do usuário.")
    print("2 - Exibir lista do usuário.")
    print("3 - Alteração dos dados do usuário.")
    print("4 - Excluir os campos do usuário.")
    print("5 - sair do programa.")

    opcao = input("Qual o opção deseja: ").strip()
    os.system("cls")

    match opcao:
        case "1":
            try:
                for chave in chaves:
                    if chave == "Nome":
                        pessoa[chave] = input(f"Informe seu nome: ")
                    else:
                        pessoa[chave] = input(f"Informe {chave}: ")
                pessoas.append(pessoa)
                print(f"{pessoa.get(chaves[0])} inserida com sucesso.")
            except Exception as e:
                print(f"Não foi possível cadastrar nova pessoa. {e}.")
            finally:
                for pessoa in pessoas:
                    for chave in pessoa:
                        print(f"{chave}: {pessoa.get(chave)}.")
            print(f"\n{'-'*40}\n")
            continue
        case "2":
            for pessoa in pessoas:
                for chave in pessoa:
                    print(f"{chave}: {pessoa.get(chave)}.")
        case "3":
            try:
                chaves = input("Informe o chaves que deseja alterar: ")
                if chaves >= 0 and chaves < len(pessoas):
                    pessoas[chaves] = input("Informe a pessoa: ")
                    print("Chave alterada com sucesso!")
                else:
                    print("Chave inválida.")
            except Exception as e:
                print(f"Não foi possível alterar a chave da lista {e}.")
            finally:
                continue

        case "4":
            try:
                if chaves in pessoa:
                    del pessoa[chaves]
                    print("Chave excluida com sucesso!")
                else:
                    print("Não foi possível achar a chave.")
            except Exception as e:
                print(f"Não foi possível deletar a chave {e}.")
            finally:
                for chave in pessoas:
                    print(f"{chaves.capitalize()}: {pessoas.get(chaves)}.")
            continue
        case "5":
            print("Programar encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue