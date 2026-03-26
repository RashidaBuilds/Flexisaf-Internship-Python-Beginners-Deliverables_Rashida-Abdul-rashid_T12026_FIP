# main_calculator.py
# This file uses the functions from math_tools.py

import math_tools

while True:
    print("\n===== CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "5":
        print("Goodbye!")
        break

    # Ask for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = math_tools.add(num1, num2)

    elif choice == "2":
        result = math_tools.subtract(num1, num2)

    elif choice == "3":
        result = math_tools.multiply(num1, num2)

    elif choice == "4":
        result = math_tools.divide(num1, num2)

    else:
        print("Invalid option.")
        continue

    print("Result:", result)