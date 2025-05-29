from flask import Flask, request, Response
import random
import requests

app = Flask(__name__)

# Lista de servidores que estarán disponibles
SERVERS = [
    "http://127.0.0.1:5001",
    "http://127.0.0.1:5002"
]

# Ruta para dirigir a los servidores disponibles
@app.route('/', defaults={'path': ''}, methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def proxy(path):
    # Selecciona un servidor aleatorio
    target_server = random.choice(SERVERS) #desde la lista de servidores que se creo antes
    url = f"{target_server}/{path}"

    try:
        # manda la solicitud al servidor seleccionado
        response = requests.request(
            method=request.method,
            url=url,
            headers={key: value for key, value in request.headers if key.lower() != 'host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )

        # Se devuelve la respuesta 
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(k, v) for k, v in response.raw.headers.items() if k.lower() not in excluded_headers]

        return Response(response.content, response.status_code, headers)

    except requests.exceptions.ConnectionError:
        return Response("Servidor no disponible", status=502)

# Inicia el servidor del balanceador
if __name__ == '__main__':
    app.run(port=8080)
