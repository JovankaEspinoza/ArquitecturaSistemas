from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)
DATA_FILE = 'tasks.json'

# Endpoint
@app.route('/')
def home():
    return " Storage Service"

# GET  Devuelve las tareas guradadas
@app.route('/storage/tasks', methods=['GET'])
def get_tasks():
    if not os.path.exists(DATA_FILE):
        return jsonify([]), 200
    with open(DATA_FILE, 'r') as f:
        tasks = json.load(f)
    return jsonify(tasks), 200

# POST para guardar una lista completa de tareas
@app.route('/storage/tasks', methods=['POST'])
def save_tasks():
    tasks = request.get_json()
    if not isinstance(tasks, list):
        return jsonify({"error": "El cuerpo debe ser una lista de tareas"}), 400
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)
    return jsonify({"status": "tareas guardadas correctamente"}), 200

if __name__ == '__main__':
    app.run(port=5002)
