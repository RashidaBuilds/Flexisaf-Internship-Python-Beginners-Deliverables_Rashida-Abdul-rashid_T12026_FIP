# STEP 1: Import the tool to save data
import json

# STEP 2: Function to ASK and CHECK
def collect_profile():
    # Ask question
    name = input("Name: ")
    # Check answer - keep asking until good
    while len(name) < 2:
        name = input("Name too short, try again: ")
    # Put in box (dictionary)
    return {"name": name}

# STEP 3: Function to SAVE
def save_profile(data):
    # Open file and dump data in
    with open("profile.json", "w") as file:
        json.dump(data, file, indent=4)

# STEP 4: Function to READ and SHOW
def display_profile():
    # Open file and load data out
    with open("profile.json", "r") as file:
        data = json.load(file)
    # Print it nicely
    print(f"Name: {data['name']}")

# STEP 5: MENU to control everything
def main():
    while True:  # Keep looping
        print("1. Create  2. Display  3. Exit")
        choice = input("Pick: ")
        
        if choice == "1":
            profile = collect_profile()  # Get data
            save_profile(profile)        # Save it
        elif choice == "2":
            display_profile()            # Show it
        elif choice == "3":
            break  # Stop the loop
            
main()  # Start the program