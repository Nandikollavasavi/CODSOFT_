# To-Do List Application in Python

tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔️ Completed" if task["completed"] else "❌ Pending"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        new_title = input("Enter new task title: ")
        tasks[task_num - 1]["title"] = new_title
        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1]["completed"] = True
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        print("Task deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

