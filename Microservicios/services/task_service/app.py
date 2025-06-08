from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
STORAGE_URL = 'http://localhost:5002/storage/tasks'
LOGGING_URL = 'http://localhost:5003/log'

def load_tasks():
    try:
        response = requests.get(STORAGE_URL)
        return response.json() if response.status_code == 200 else []
    except Exception as e:
        print(f" Error al cargar tareas: {e}")
        return []

def save_tasks(tasks):
    try:
        requests.post(STORAGE_URL, json=tasks)
    except Exception as e:
        print(f" Error al guardar tareas: {e}")

def log_event(message):
    try:
        requests.post(LOGGING_URL, json={"message": message})
    except Exception as e:
        print(f" Error al registrar log: {e}")

@app.route('/')
def home():
    return " Bienvenido al Task Service"

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    print(" /tasks llamado")
    tasks = load_tasks()
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get("title")
    if not title:
        return jsonify({"error": "Falta 'title'"}), 400
    tasks = load_tasks()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    log_event(f"Tarea creada: {title}")
    return jsonify({"status": "tarea agregada"}), 201

@app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
        log_event(f"Tarea completada: {tasks[task_id]['title']}")
        return jsonify({"status": "completada"}), 200
    return jsonify({"error": "No encontrada"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        title = tasks[task_id]['title']
        del tasks[task_id]
        save_tasks(tasks)
        log_event(f"Tarea eliminada: {title}")
        return jsonify({"status": "eliminada"}), 200
    return jsonify({"error": "No encontrada"}), 404

if __name__ == '__main__':
    app.run(port=5001)
