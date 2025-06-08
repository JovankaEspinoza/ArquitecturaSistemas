from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)
TASK_SERVICE = 'http://localhost:5001/tasks'

TEMPLATE = """
<!doctype html>
<title>Task Manager</title>
<h1>Gestor de Tareas</h1>
<form method="post">
  <input name="title" placeholder="Nueva tarea">
  <input type="submit" value="Agregar">
</form>
<ul>
  {% for task in tasks %}
    {% set idx = loop.index0 %}
    <li>
      {% if task.completed %}
         <s>{{ task.title }}</s>
      {% else %}
         {{ task.title }}
        <a href="/complete/{{ idx }}">[Completar]</a>
      {% endif %}
      <a href="/delete/{{ idx }}">[Eliminar]</a>
    </li>
  {% endfor %}
</ul>
<a href="/logs">Ver Logs</a>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        requests.post(TASK_SERVICE, json={"title": title})
        return redirect('/')
    tasks = requests.get(TASK_SERVICE).json()
    return render_template_string(TEMPLATE, tasks=tasks)

@app.route('/complete/<int:task_id>')
def complete(task_id):
    requests.put(f'{TASK_SERVICE}/{task_id}/complete')
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    requests.delete(f'{TASK_SERVICE}/{task_id}')
    return redirect('/')

@app.route('/logs')
def logs():
    log_data = requests.get('http://localhost:5003/logs').json()
    return render_template_string("""
    <h2>Historial de Logs</h2>
    <ul>
    {% for log in logs %}<li>{{ log }}</li>{% endfor %}
    </ul>
    <a href="/">Volver</a>
    """, logs=log_data['logs'])

if __name__ == '__main__':
    app.run(port=5000)
