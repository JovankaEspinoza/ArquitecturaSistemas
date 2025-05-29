from flask import Flask, request, jsonify, render_template_string, redirect
import json
import os
from flask import Flask, request, render_template, redirect
import json, os


app = Flask(__name__)
TASKS_FILE = "tasks.json"


#funciones para guardar tareas y cargarlas
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks): 
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Rutas


@app.route("/")
def index():





    tasks = load_tasks()




    # Obtener el puerto del request
    try:
        port = request.host.split(":")[1]
    except IndexError:
        port = "5001"  # es este puerto por default

    # Definir color de fondo según puerto
    bg_color = "#ADD8E6" if port == "5001" else "#FFC0CB" 

    return render_template("index.html", tasks=tasks, port=port, bg_color=bg_color)
  

@app.route("/tasks/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    description = request.form.get("description")
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return redirect("/")

@app.route("/tasks/<int:task_id>/complete")
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break
    save_tasks(tasks)
    return redirect("/")

@app.route("/tasks/<int:task_id>/delete")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return redirect("/")

# Iniciar el servidor


if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
    app.run(debug=True, port=port)
