# logger.py
# Logs actions into a file

from datetime import datetime

def log_action(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs.txt", "a") as file:
        file.write(f"{time} - {message}\n")