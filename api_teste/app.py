from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_wtf.csrf import generate_csrf
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e9c35a5519a149be84c02c69bdc5e997'
CORS(app, resources=r'/api/*')

@app.route("/api/v1/csrf-token", methods=['GET'])
def get_csrf_token():
    csrf_token = generate_csrf()
    return jsonify({'csrfToken': csrf_token})


@app.route("/api/v1/login", methods=['POST'])
def recebe_login():
    data = json.loads(request.data)
    print(data)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)