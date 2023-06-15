from flask import Flask, jsonify, request
import json
app = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': 'Joao Pedro',
        'tarefa': 'Limpar a casa',
        'status': 'Pendente',
    }
]

@app.route("/tarefas", methods=['GET'])
def lista_tarefas():
    return jsonify(tarefas)

@app.route("/add-tarefa", methods=['POST'])
def adiciona_tarefa():
    id = len(tarefas)
    dados = json.loads(request.data)
    dados['id'] = id
    tarefas.append(dados)
    return jsonify(tarefas[id])

@app.route("/tarefas/<int:id>", methods=['GET', 'DELETE'])
def consulta_tarefa(id):
    try:
        if request.method == 'GET':
            response = tarefas[id]
        elif request.method == 'DELETE':
            tarefas.pop(id)
            response = {'msg': 'Registro excluido', 'status': 'ok'}
    except IndexError:
        response = {'error': f'ID {id} não encontrado'}
    return jsonify(response)

@app.route("/tarefas/<int:id>/<string:status>", methods=['PUT'])
def altera_status_tarefa(id, status):
    try:
        tarefa = tarefas[id]
        tarefa['status'] = status
        response = tarefas[id]
    except IndexError:
        response = {'error': f'ID {id} não encontrado'}
    return response

if __name__ == '__main__':
    app.run(debug=True)