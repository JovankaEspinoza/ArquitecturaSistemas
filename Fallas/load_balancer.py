import requests
from itertools import cycle
from flask import Flask, jsonify, request

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Lista de servidores Flask
servers = ["http://127.0.0.1:5001", "http://127.0.0.1:5002"]
server_pool = cycle(servers)

def get_next_server():
    """Obtiene el siguiente servidor en el pool de servidores"""
    return next(server_pool)

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def load_balance(path):
    """Redirige las peticiones a los servidores Flask disponibles"""
    server = get_next_server()
    url = f"{server}/{path}"

    try:
        # Realiza la petición al servidor elegido
        if request.method == 'GET':
            response = requests.get(url, params=request.args)
        elif request.method == 'POST':
            response = requests.post(url, json=request.get_json())
        elif request.method == 'PUT':
            response = requests.put(url, json=request.get_json())
        elif request.method == 'DELETE':
            response = requests.delete(url)
        
        # Verificar si la respuesta contiene datos
        if response.text:
            try:
                response_json = response.json()  # Intenta analizar como JSON
                return jsonify(response_json), response.status_code
            except requests.exceptions.JSONDecodeError:
                # Si la respuesta no es JSON válido, regresa la respuesta como está
                return response.text, response.status_code
        else:
            # Si la respuesta está vacía, manejar el error adecuadamente
            return jsonify({"error": "Empty response from server"}), 500

    except requests.exceptions.RequestException as e:
        # Si ocurre un error en la conexión, se maneja la excepción
        return jsonify({"error": "Error al procesar la solicitud en el servidor", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8080)
