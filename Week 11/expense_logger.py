# expense_logger.py
# Logs expenses with timestamps and analyzes them using pandas

import csv
from datetime import datetime
import pandas as pd

filename = "expenses.csv"

# -----------------------------
# STEP 1: Add expense
# -----------------------------
def add_expense():
    item = input("Enter expense item: ")
    amount = float(input("Enter amount: "))

    # Get current time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to CSV
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        # Write header only if file is empty
        file.seek(0)
        if file.tell() == 0:
            writer.writerow(["Item", "Amount", "Timestamp"])

        writer.writerow([item, amount, timestamp])

    print("Expense saved!")


# -----------------------------
# STEP 2: Analyze expenses
# -----------------------------
def analyze_expenses():
    try:
        df = pd.read_csv(filename)

        total = df["Amount"].sum()
        average = df["Amount"].mean()

        print("\nTotal Spent:", total)
        print("Average Expense:", round(average, 2))

    except FileNotFoundError:
        print("No expense file found yet.")


# -----------------------------
# MENU
# -----------------------------
while True:
    print("\n1. Add Expense")
    print("2. Analyze Expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        analyze_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")