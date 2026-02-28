contacts = {}

choice = input("Type add, update, delete, search, list or exit: ")

while choice != "exit":

    if choice == "add":
        sid = input("ID: ")
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        role = input("Role: ")

        duplicate = False
        for c in contacts.values():
            if c["email"] == email or c["phone"] == phone:
                duplicate = True

        if duplicate:
            print("Duplicate email or phone.")
        else:
            contacts[sid] = {
                "name": name,
                "email": email,
                "phone": phone,
                "role": role
            }

    elif choice == "update":
        sid = input("ID: ")
        if sid in contacts:
            contacts[sid]["name"] = input("New name: ")
            contacts[sid]["email"] = input("New email: ")
            contacts[sid]["phone"] = input("New phone: ")
            contacts[sid]["role"] = input("New role: ")

    elif choice == "delete":
        sid = input("ID: ")
        if sid in contacts:
            del contacts[sid]

    elif choice == "search":
        sid = input("ID: ")
        if sid in contacts:
            print(contacts[sid])

    elif choice == "list":
        print(contacts)

    choice = input("Type add, update, delete, search, list or exit: ")