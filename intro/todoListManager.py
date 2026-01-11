# To-Do List Manager

tasks = []
task_id = 1

def add_task():
    global task_id
    description = input("Enter task description: ")

    task = {
        "id": task_id,
        "description": description,
        "status": "Pending"
    }

    tasks.append(task)
    print("Task added successfully!")
    task_id += 1

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nID\tDescription\t\tStatus")
    print("---------------------------------------")
    for task in tasks:
        print(f"{task['id']}\t{task['description']}\t\t{task['status']}")

def mark_complete():
    task_num = int(input("Enter task ID to mark as completed: "))

    for task in tasks:
        if task["id"] == task_num:
            task["status"] = "Completed"
            print("Task marked as completed!")
            return

    print("Task ID not found!")

def delete_task():
    task_num = int(input("Enter task ID to delete: "))

    for task in tasks:
        if task["id"] == task_num:
            tasks.remove(task)
            print("Task deleted successfully!")
            return

    print("Task ID not found!")

# Menu-driven program
while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List Manager...")
        break
    else:
        print("Invalid choice! Please try again.")
