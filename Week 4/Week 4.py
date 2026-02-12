password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score = score + 1

if "A" in password or "B" in password:
    score = score + 1

if "1" in password or "2" in password:
    score = score + 1

if "!" in password:
    score = score + 1

if score <= 1:
    print("Weak")
elif score == 2:
    print("Medium")
else:
    print("Strong")


# ///////////////////////////////

expenses = []

user_input = input("Enter expense or type exit: ")

while user_input != "exit":
    expenses.append(float(user_input))
    user_input = input("Enter expense or type exit: ")

total = 0
for item in expenses:
    total = total + item

print("Total:", total)
