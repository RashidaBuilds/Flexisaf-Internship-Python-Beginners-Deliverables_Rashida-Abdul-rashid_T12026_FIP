test = float(input("Test score: "))
assignment = float(input("Assignment score: "))
exam = float(input("Exam score: "))

total = test + assignment + exam
average = total / 3

print("Total:", total)
print("Average:", average)

if average >= 50:
    print("You Passed")
else:
    print("You Failed")

if average >= 80:
    print("You get an Award")
