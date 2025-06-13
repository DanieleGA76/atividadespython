import os
# TODO - Atividade: Crie um programa que receba do usuário os seguintes dados:
"""
- Nome:
- CPF:
- Data de Nascimento:
- E-mail:
- Gênero:
- Telefone:
- Endereço:
- Altura em metros:
- Peso em kg:
- Tipo Sanguíneo
Ao final, o program exibe dados.
"""
#NOTE - Deve ser feito utilizando o conceito de dicionario.

pessoa = {
    'Nome': "",
    'CPF': "",
    'Datanascimento': "",
    'Email':"",
    'Gênero': "",
    'Telefone': "",
    'Endereço':"",
    'Altura': "",
    'Peso': "",
    'TipoSang':""
}

try:
    pessoa['nome'] = input("Informe seu nome: ")
    pessoa['cpf'] = input("Informe seu CPF: ")
    pessoa['datanasc'] = input("Informe sua data de nascimento: ")
    pessoa['email'] = input("Informe seu e-mail: ")
    pessoa['genero'] = input("Informe seu Gênero: ")
    pessoa['telefone'] = input("Informe seu Telefone: ")
    pessoa['endereco'] = input("Informe seu endereço: ")
    pessoa['altura'] = input("Informe sua altura: ").replace(",",".")
    pessoa['peso'] = input("Informe seu peso: ").replace(",",".")
    pessoa['tiposang'] = input("Informe seu tipo sanguíneo: ")
    os.system("cls")
except Exception as e:
    print(f"não foi possovile inserir o valor {e}.")
finally:
    print(f"{'&'*20} CADASTRO {'&'*20}")
    print(f"Nome: {pessoa.get('nome')}.")
    print(f"CPF: {pessoa.get('cpf')}.")
    print(f"Data de Nascimento: {pessoa.get('datanasc')}.")
    print(f"E-mail: {pessoa.get('email')}.")
    print(f"Gênero: {pessoa.get('genero')}.")
    print(f"Telefone: {pessoa.get('telefone')}.")
    print(f"Endereço: {pessoa.get('endereco')}.")
    print(f"Altura: {pessoa.get('altura')}.")
    print(f"Peso: {pessoa.get('peso')}.")
    print(f"Tipo Sanguíneo: {pessoa.get('tiposang')}.")
