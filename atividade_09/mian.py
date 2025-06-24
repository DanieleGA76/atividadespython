import random
"""
# TODO - Atividade: Crie um programa que receba os dados de dois objetos diferentes da mesma classe Pessoa. Os dados serão os seguintes:
- Nome
- Idade
- E-mail
- Telefone
- Gênero
- Tipo Sanguíneo
Sunpnha que o objeto 'usuario_2" esteja precisando de doação de sangue do 'usuario_1'. O programa deve informar os dados dos dois usuários, e ao final, informar se o usuário_1 pode doar sangue para o usuário_2 ou não.
# NOTE - a última pergunta deverão ter uma resposta randômica.
"""
class Pessoa:
    def __init__(self, nome, idade, email, telefone,genero, tiposang):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.genero = genero
        self.tiposang = tiposang
    def sexo(self):
         return True
    if sexo():
         print("Masculino")
    else:
         print("Feminino")
    def tipo(self):
        return f" Qual seu tipo Sanguíneo?"
    
if __name__ == "__main__":
        usuario = Pessoa("", "", "", "", bool(random.getrandbits(1)),bool(random.getrandbits(1)))
        usuario.nome = input("Informe seu nome: ").title().strip()
        usuario.idade = int(input("Informe sua idade: "))
        usuario.email = input("Informe seu e-mail: ").title().strip()
        usuario.telefone = input("Informe o seu telefone: ").title().strip()
        usuario.genero = Pessoa.sexo()
