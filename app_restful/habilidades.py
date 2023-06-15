from flask_restful import Resource
from flask import request
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def post(self):
        dados = json.loads(request.data)
        if dados not in lista_habilidades:
            lista_habilidades.append(dados)
            response = {'msg': 'habilidade inserida com sucesso.'}
        else:
            response = {'msg': 'habilidade já existe nos nossos registros'}
        return response
    
class AlteraHabilidades(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        if dados not in lista_habilidades:
            lista_habilidades[id] = dados
            response = {'msg': 'registro alterado'}
        else:
            response = {'msg': 'habilidade já existe nos nossos registros'}
        return response
    
    def delete(self, id):
        lista_habilidades.pop(id)
        return {'msg': 'registro excluido'}