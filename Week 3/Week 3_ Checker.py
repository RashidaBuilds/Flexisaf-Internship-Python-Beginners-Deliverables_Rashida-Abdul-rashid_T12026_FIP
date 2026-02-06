#AGE VALIDATOR / LOGIN FLOW

age = int(input("Enter your age: "))

# If age is 18 or more, allow access
if age >= 18:
    print("Access granted ✅")
else:
    print("Access denied ❌")


#LOAN ELIGIBILITY CHECKERrr

age = int(input("\nEnter your age: "))
income = int(input("Enter your monthly income: "))

# Check two conditions at the same time
if age >= 21 and income >= 100000:
    print("You are eligible for a loan 🎉")
else:
    print("Sorry, you are not eligible 😔")


#EXPENSE TRACKER

limit = 50000  # This is the spending limit
expense = int(input("\nEnter your total expenses: "))

# Compare spending with limit
if expense > limit:
    print("Warning! You are overspending ⚠️")
else:
    print("You are within your budget 👍")
