import tasks

while True:
    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        tasks.add_task()

    elif choice == "2":
        tasks.view_tasks()

    elif choice == "3":
        tasks.mark_done()

    elif choice == "4":
        tasks.delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")