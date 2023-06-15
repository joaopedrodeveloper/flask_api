from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/<int:id>") #URI com tipagem
def pessoas(id):
    return jsonify({'id': id, 'nome': 'Joao Pedro', 'profissao': 'Desenvolvedor'}) #Para retornar um JSON use jsonify({'ex':'teste'})

@app.route('/soma', methods=['POST', 'PUT', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data) #json.loads() para entender que os dados são um json
        print(dados)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 20
    return jsonify({'soma': total})

if __name__ == '__main__':
    app.run(debug=True)