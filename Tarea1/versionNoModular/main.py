from datetime import datetime

tasks = []

class Task:
    def __init__(self, description, date):
        self.description = description
        self.done = False
        self.date = date

    def __str__(self):
        status = "✅" if self.done else "🕒"
        return f"{status} {self.description} (creada el {self.date})"

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
    print("\nTareas actuales:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
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
    print("\nTareas actuales:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
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

def Menu():
    while True:
        print("------ MENÚ ------")
        print("1. Agregar nueva tarea")
        print("2. Actualizar tarea")
        print("3. Marcar tarea como completada")
        print("4. Ver tareas")
        print("5. Salir")
        choice = input("Elige una opción (1-5): ")

        if choice == "1":
            NewTask()
        elif choice == "2":
            UpdateTask()
        elif choice == "3":
            TaskDone()
        elif choice == "4":
            print("\nTareas actuales:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == "5":
            print("👋 Hasta luego.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.\n")


Menu()