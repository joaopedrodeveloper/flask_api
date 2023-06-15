from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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
@app.route("/dev/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'ID {id} não existe'
            response = {'status': 'erro', 'msg': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'msg': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensage': 'Registro excluído'})

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route("/dev", methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
        

if __name__ == '__main__':
    app.run(debug=True)
