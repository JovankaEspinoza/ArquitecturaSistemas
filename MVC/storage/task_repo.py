import json
from Model.task import Task

FILE_PATH = "storage/task.json"

def save_tasks(tasks):
    """Guarda la lista de tareas en formato JSON"""
    with open(FILE_PATH, "w") as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks():
    """Carga las tareas desde el archivo JSON y devuelve objetos Task"""
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return [Task(d["description"], d["date"], d["done"]) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
