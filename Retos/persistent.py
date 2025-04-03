'''
Representation Scenario: Creating a simple to-do list application.

Task: Develop a program that stores a to-do list persistently using a file (e.g., a text file or JSON file). The program should allow users to:

Add tasks: Append new tasks to the list. Mark tasks as complete: Update the status of tasks. View the to-do list: Display all tasks with their status. Save and load the list: To and from the file. Example (using a text file):
'''

def load_todo_list(filename="todo.txt"):
    tasks = []
    try:    
        with open(filename, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass   #Ignorar si el archivo no existe
    return tasks  

def save_todo_list(tasks, filename="todo.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks, task):
    tasks.append(task)

def mark_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index] = tasks[index] + " - Complete"

def view_todo_list(tasks):
    for index, task in enumerate(tasks):
        print(f"{index + 1}: {task}")

def clean_todo_list(filename="todo.txt"):
    with open(filename,"w") as file:
        pass

#Ejemplo
todo_list = load_todo_list()

while True:
    print("Ingrese una tarea: ") 
    add_task(todo_list, input())
    print("¿Desea añadir otra tarea?")
    print("1. Si")
    print("2. No")
    if input() == "2":
        break

view_todo_list(todo_list)

save_todo_list(todo_list)

print("¿Que tarea ha completado?")
view_todo_list(todo_list)
print("Ingrese el numero de la tarea: ")
x= int(input())
mark_complete(todo_list, x)
view_todo_list(todo_list)
save_todo_list(todo_list)
