from flask import Flask, request, jsonify
from flask_cors import CORS
from validador import validar_contrasena

app = Flask(__name__)
CORS(app)

@app.route('/validar', methods=['POST'])
def validar():
    datos = request.get_json()
    contrasena = datos.get('contrasena', '')
    resultado = validar_contrasena(contrasena)
    return jsonify(resultado)

@app.route('/', methods=['GET'])
def inicio():
    return jsonify({"estado": "API funcionando correctamente"})

if __name__ == '__main__':
    app.run(debug=True)