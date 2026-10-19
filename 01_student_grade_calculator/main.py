# Student Marks and Grade Calculator
# Syllabus topics: variables, input/output, type conversion, lists,
# for loop, break, arithmetic operators, if-elif-else, string formatting.

marks = []
total = 0
valid = True

# Read and validate marks for five subjects.
for subject in [1, 2, 3, 4, 5]:
    mark = float(input(f"Enter marks for subject {subject} (0-100): "))

    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        valid = False
        break

    marks.append(mark)
    total = total + mark

if valid:
    # Five subjects are each marked out of 100.
    percentage = total / 5

    # Sample grade boundaries for this assignment.
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    print("\n----- Student Result -----")
    print(f"Total marks : {total:.1f} / 500")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
