assignments = []
expenses = []

choice = input("Type add, view, complete, remove, expense, show_expense, filter or exit: ")

while choice != "exit":

    if choice == "add":
        task = input("Enter assignment: ")
        assignments.append(task)

    elif choice == "view":
        for task in assignments:
            print(task)

    elif choice == "complete":
        num = int(input("Enter number: "))
        assignments[num] = assignments[num] + " done"

    elif choice == "remove":
        num = int(input("Enter number: "))
        assignments.pop(num)

    elif choice == "expense":
        item = input("Enter item: ")
        amount = float(input("Enter amount: "))
        expenses.append((item, amount))

    elif choice == "show_expense":
        for exp in expenses:
            print(exp)

    elif choice == "filter":
        limit = float(input("Enter limit: "))
        for exp in expenses:
            if exp[1] > limit:
                print(exp)

    choice = input("Type add, view, complete, remove, expense, show_expense, filter or exit: ")