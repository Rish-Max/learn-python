import os

PATH = "tasks.txt"

def add_task(task):
    new_task = f"{task} - not done\n"
    if os.path.exists(PATH):
        with open(PATH, "a") as file:
            file.write(new_task)
    else:
        with open(PATH, "w") as file:
            file.write(new_task)
    print("Task added successfully.")

def view_task(task_id):
    with open(PATH, "r") as file:
        tasks = file.readlines()
    print(tasks[task_id])
    return tasks[task_id]

def update_task(task_id, task):
    tasks = []
    with open(PATH, "r") as file:
        tasks = file.readlines()
    updated_task = tasks[task_id]
    _, status = updated_task.split(" - ")
    updated_task = f"{task} - {status}"
    tasks[task_id] = updated_task.strip()
    with open(PATH, "w") as file:
        file.writelines(tasks)
    print("Task updated successfully.")

def mark_task_as_done(task_id):
    tasks = []
    with open(PATH, "r") as file:
        tasks = file.readlines()
    updated_task = tasks[task_id].replace("not done", "done").strip()
    tasks[task_id] = updated_task.strip()
    print(tasks)
    with open(PATH, "w") as file:
        file.writelines(tasks)
    print("Task updated successfully.")

def delete_task(task_id):
    tasks = []
    with open(PATH, "r") as file:
        tasks = file.readlines()
    tasks.pop(task_id)
    with open(PATH, "w") as file:
        file.writelines(tasks)
    print("Task deleted successfully.")
    
def main():
    print("""    
    Welcome to the task manager
    1. Add a task
    2. View a task
    3. Update a task
    4. Mark task as done
    5. Delete a task
    6. Exit
    """)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter the task: ").strip()
        add_task(task)
    elif choice == 2:
        task_id = int(input("Enter the task id: ").strip())
        view_task(task_id)
    elif choice == 3:
        task_id = int(input("Enter the task id: "))
        task = input("Enter the task: ").strip()
        update_task(task_id, task)
    elif choice == 4:
        task_id = int(input("Enter the task id: "))
        mark_task_as_done(task_id)
    elif choice == 5:
        task_id = int(input("Enter the task id: "))
        delete_task(task_id)
    elif choice == 6:
        print("Thank you for using the task manager.")
    else:
        print("Invalid choice. Please enter a valid choice.")
        main()


main()