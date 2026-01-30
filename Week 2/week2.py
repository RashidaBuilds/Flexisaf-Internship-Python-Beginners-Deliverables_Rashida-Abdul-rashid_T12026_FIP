import json

# 1. Ask + check
name = input("Enter name: ")
while name == "":
    name = input("Name cannot be empty: ")

age = input("Enter age: ")
while not age.isdigit():
    age = input("Enter a valid age: ")

# 2. Store in a box
profile = {
    "name": name,
    "age": int(age)
}

# 3. Save the box
with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

# 4. Open and show the box
with open("profile.json", "r") as file:
    saved_profile = json.load(file)

print(saved_profile)
