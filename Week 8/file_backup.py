# file_backup.py
# This script copies the content of one file into another file
# It prevents overwriting files and handles errors

import os

# Ask the user for file names
source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")

try:
    # Check if the source file exists
    if not os.path.exists(source):
        raise FileNotFoundError("Source file does not exist.")

    # Prevent overwriting an existing file
    if os.path.exists(destination):
        print("Destination file already exists. Copy cancelled.")

    else:
        # Open the source file and read its content
        with open(source, "r") as src_file:
            content = src_file.read()

        # Write the content into the destination file
        with open(destination, "w") as dest_file:
            dest_file.write(content)

        print("File copied successfully!")

# Handle case where file does not exist
except FileNotFoundError as e:
    print("Error:", e)

# Handle permission issues
except PermissionError:
    print("Error: Permission denied when accessing the file.")

# Handle other unexpected errors
except Exception as e:
    print("Unexpected error:", e)