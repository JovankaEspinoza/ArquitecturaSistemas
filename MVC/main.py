from Controller.TaskController import NewTask, UpdateTask, TaskDone, GetTasks
from View.terminal_view import ViewTareas

def menu():
    while True:
        print("──── GESTOR DE TAREAS ────")
        print("1. Agregar nueva tarea")
        print("2. Editar tarea existente")
        print("3. Marcar tarea como completada")
        print("4. Ver todas las tareas")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            NewTask()
        elif opcion == "2":
            UpdateTask()
        elif opcion == "3":
            TaskDone()
        elif opcion == "4":
            ViewTareas(GetTasks())
        elif opcion == "5":
            print("👋 Hasta luego!")
            break
        else:
            print("❌ Opción inválida, intenta nuevamente.\n")

if __name__ == "__main__":
    menu()
