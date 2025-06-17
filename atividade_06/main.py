import os
"""
# TODO - Atividade: Crie um programa com o seguinte menu:
- Cadastrar nova chave
- Exibir dados do usuarios
- Alterar valor da chave
- Excluir chave
- Sair do programa
# NOTE - Os dados a serem inseridos precisam ter a ver com dados de usuário
"""
usuario = {}

while True:
    print(f"{'#'*20} CADASTRO{'#'*20}")
    print("1 - Cadastro do usuário.")
    print("2 - Exibir os dados do usuário.")
    print("3 - Alteração dos dados do usuário.")
    print("4 - Excluir os campos do usuário.")
    print("5 - sair do programa.")

    opcao = input("Qual o opção deseja: ").strip()

    os.system("cls")

    match opcao:
        case "1":
            chave = input("Informe o nome da chave que deseja inserir: ").lower().strip()
            usuario[chave]= input("informe o valor da chave: ")
            os.system("cls")
            print("Chave cadastra com sucesso!")
            continue
            
        case "2":
           for chave in range(len(usuario)):
               print(f"{chave.capitalize()}: {usuario.get(chave)}.")
               continue
               
        case "3":
           chave = input("Informe o dado que deseja alterar: ").lower().strip()
           if chave in usuario:
               usuario[chave] = input("Informe o valor da chave: ")
               os.system("cls")
               print("Valor da chave alterado com sucesso!")
           else:
               os.system("cls")
               print("Chave não encontrada.")
           continue

        
        case "4":
            chave = input("Informe a chave que deseja excluir: ").lower().strip()
            confirmacao = input(f"Tem certeza de que desaja excluir {chave}? (s/n)").lower().strip()
            if confirmacao is "s":
                del usuario[chave]
                print("Chave escluída com sucesso!")
            else:
                print("Chave não foi excluída.")
            continue
                  
        case "5":
            print("Programar encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue

