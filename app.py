from flask import Flask, request, jsonify
from flask_cors import CORS
from connector_db import connection, cursor
import requests

# Initialize API
app = Flask(__name__)
CORS(app)

if not connection or not connection.is_connected():
    print("Erro: Conexão com banco de dados falhou!")
    exit(1)

# Rota Helth Check
@app.route('/')
def index():
    return jsonify({"message": "API runing sussesfull"})

# Connected API

def fetch_cep(cep):
    response = requests.get((f"https://viacep.com.br/ws/{cep}/json/"))
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == '__main__':
    app.run(debug=True)