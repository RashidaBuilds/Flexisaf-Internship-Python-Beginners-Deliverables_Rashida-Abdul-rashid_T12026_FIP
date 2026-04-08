# action_logger.py
# Logs user actions and exports environment packages

from datetime import datetime
import subprocess

log_file = "actions_log.txt"

# -----------------------------
# STEP 1: Log actions
# -----------------------------
def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a") as file:
        file.write(f"{timestamp} - {action}\n")


# -----------------------------
# STEP 2: Export environment
# -----------------------------
def export_environment():
    with open("requirements.txt", "w") as file:
        subprocess.run(["pip", "freeze"], stdout=file)

    print("Environment exported to requirements.txt")


# -----------------------------
# MENU
# -----------------------------
while True:
    print("\n1. Perform Action")
    print("2. Export Environment")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        action = input("What action did you perform? ")
        log_action(action)
        print("Action logged!")

    elif choice == "2":
        export_environment()

    elif choice == "3":
        break

    else:
        print("Invalid choice.")