tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(index, "-", task)

def mark_done():
    view_tasks()
    if len(tasks) == 0:
        return

    num = int(input("Enter task number to mark as done: "))
    if 1 <= num <= len(tasks):
        tasks[num-1] = tasks[num-1] + " (Done)"
        print("Task marked as done!")
    else:
        print("Invalid number.")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return

    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted!")
    else:
        print("Invalid number.")