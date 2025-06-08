from flask import Flask, request, jsonify
import os

app = Flask(__name__)
LOG_FILE = 'log.txt'

@app.route('/')
def index():
    return "Logging Service"

@app.route('/log', methods=['POST']) #guardar msj en el txt
def log_message():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "Falta el campo 'message'"}), 400

    with open(LOG_FILE, 'a') as log_file:
        log_file.write(message + '\n')

    return jsonify({"status": "mensaje registrado"}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify({"logs": []}), 200

    with open(LOG_FILE, 'r') as log_file:
        lines = log_file.readlines()

    logs = [line.strip() for line in lines]
    return jsonify({"logs": logs}), 200

if __name__ == '__main__':
    app.run(port=5003)
