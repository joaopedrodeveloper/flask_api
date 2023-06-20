from models import Pessoas, db_session, Usuarios

#Cria pessoa na tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Joao Pedro2', idade=19)
    print(pessoa)
    pessoa.save()

#Consulta pessoa na tabela Pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Joao Pedro').first()
    print(Pessoas.query.all())

#Altera dados da pessoa na tabela Pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joao Pedro').first()
    pessoa.idade = 200
    pessoa.save()

#Excluir dados da pessoa da tabela Pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joao Pedro2').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__ == '__main__':
    #insere_usuario('joao', 123)
    #consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
