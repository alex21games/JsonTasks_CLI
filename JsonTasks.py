import json
import os
from datetime import datetime

tasks_file = "tasks.json"

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description, expiration_date):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "expiration_date": expiration_date
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tarea añadida: {task}")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Tarea {task_id} borrada.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No hay tareas por realizar.")
        return
    for task in tasks:
        print(f"{task['id']}: {task['description']} (Expira: {task['expiration_date']})")

def main():
    while True:
        print("\nAdministrador de tareas")
        print("1. Añadir tarea")
        print("2. Eliminar tarea")
        print("3. Listar tareas")
        print("4. Salir")
        choice = input("Selecciona una opción: ")
        
        if choice == "1":
            description = input("Introduce la descripción de la tarea: ")
            expiration_date = input("Introduce la fecha de vencimiento (YYYY-MM-DD): ")
            try:
                datetime.strptime(expiration_date, "%Y-%m-%d")  # Validar formato de fecha
                add_task(description, expiration_date)
            except ValueError:
                print("Fecha inválida. Usa el formato YYYY-MM-DD.")
        elif choice == "2":
            try:
                task_id = int(input("Selecciona el ID de la tarea: "))
                delete_task(task_id)
            except ValueError:
                print("ID inválido.")
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
