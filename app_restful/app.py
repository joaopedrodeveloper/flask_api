from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, AlteraHabilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
     'id': 0,
     'nome': 'Joao Pedro',
     'habilidades': ['Python', 'Flask']
    },
    {
     'id': 1,
     'nome': 'Teste',
     'habilidades': ['Python', 'Django']
    },
]

# devolve um desenvolvedor pelo id, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'ID {id} não existe'
            response = {'status': 'erro', 'msg': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'msg': mensagem}
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensage': 'Registro excluído'}

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

    def get(self):
        return desenvolvedores

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Habilidades, '/habilidades')
api.add_resource(AlteraHabilidades, '/habilidades/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)