# student_scores.py
# This program stores student names and scores in a CSV file
# Then reads the file to calculate the class average
# and identify the top performer

import csv

filename = "students.csv"

# -----------------------------
# STEP 1: Collect student data
# -----------------------------

students = []

while True:
    name = input("Enter student name (or type 'done'): ")

    if name.lower() == "done":
        break

    score = float(input("Enter score: "))

    students.append([name, score])

# -----------------------------
# STEP 2: Save data to CSV
# -----------------------------

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["Name", "Score"])

    # Write student rows
    writer.writerows(students)

print("Student data saved to CSV.")

# -----------------------------
# STEP 3: Read CSV file
# -----------------------------

scores = []
top_student = ""
highest_score = 0

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        score = float(row["Score"])

        scores.append(score)

        # Check if this student has the highest score
        if score > highest_score:
            highest_score = score
            top_student = name

# -----------------------------
# STEP 4: Calculate average
# -----------------------------

average = sum(scores) / len(scores)

# -----------------------------
# STEP 5: Display results
# -----------------------------

print("\nClass Average:", round(average, 2))
print("Top Performer:", top_student)
print("Highest Score:", highest_score)