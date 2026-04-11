# main.py
# This is the main controller of the app

from ai_generator import generate_message
from email_sender import send_email
from logger import log_action

print("=== Email Notification System ===")

# Step 1: Get user input
name = input("Enter student/parent name: ")
email = input("Enter email address: ")
announcement = input("Enter announcement: ")

# Step 2: Generate AI message
print("\nGenerating message...")
message = generate_message(name, announcement)

print("\nGenerated Message:\n")
print(message)

# Step 3: Send email
result = send_email(email, "School Announcement", message)
print("\n", result)

# Step 4: Log the result
log_action(f"{email} - {result}")