import json

name = input("Enter name: ")
while name == "":
    name = input("Enter name again: ")

age = input("Enter age: ")
while not age.isdigit():
    age = input("Enter valid age: ")

email = input("Enter email: ")
while "@" not in email:
    email = input("Enter valid email: ")

profile = {
    "name": name,
    "age": int(age),
    "email": email
}

file = open("profile.json", "w")
json.dump(profile, file, indent=4)
file.close()

file = open("profile.json", "r")
data = json.load(file)
file.close()

print("Saved profile:")
print(data)
