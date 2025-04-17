def ViewTareas(tasks):
    if not tasks:
        print("\n📭 No hay tareas registradas.\n")
        return
    print("\nTareas actuales:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")