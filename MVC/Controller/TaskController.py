from datetime import datetime
from Model.task import Task
from View.terminal_view import ViewTareas
from storage.task_repo import save_tasks, load_tasks
tasks = load_tasks()




def NewTask():
    while True:
        task = input("Ingresa una nueva tarea: ")
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks.append(Task(task, now))
        reply = input("¿Quieres ingresar una nueva tarea? (S/N): ").strip().upper()
        if reply != "S":
            break
    print("\nTareas registradas:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def TaskDone():
    ViewTareas(tasks)
    try:
        done = int(input("Ingresa el número de la tarea que has finalizado: "))
        if 1 <= done <= len(tasks):
            tasks[done - 1].done = True
            print(f"Tarea marcada como completada: '{tasks[done - 1].description}'")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def UpdateTask():
    ViewTareas(tasks)
    try:
        done = int(input("Ingresa el número de la tarea que quieres actualizar: "))
        if 1 <= done <= len(tasks):
            update = input("Ingresa el nuevo texto para la tarea: ")
            tasks[done - 1].description = update
            print("Tarea actualizada con éxito.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def GetTasks():
    return tasks