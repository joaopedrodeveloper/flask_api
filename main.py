from flask import Flask
app = Flask(__name__)

@app.route("/<numero>", methods=['POST', 'GET'])
def ola(numero):
    return f"Ola mundo. {numero}"

if __name__ == '__main__':
    app.run(debug=True)