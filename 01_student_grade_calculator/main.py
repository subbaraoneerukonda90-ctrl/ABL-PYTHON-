# Student Marks and Grade Calculator
# Syllabus topics used:
# input/output, variables, type conversion, lists, for loop,
# arithmetic operators, and if-elif-else decision-making.

def main():
    marks = []
    total = 0

    # Read and validate marks for five subjects.
    for subject in range(1, 6):
        mark = float(input(f"Enter marks for subject {subject} (0-100): "))

        if mark < 0 or mark > 100:
            print("Invalid marks. Enter a value from 0 to 100.")
            return

        marks.append(mark)
        total = total + mark

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


if __name__ == "__main__":
    main()
