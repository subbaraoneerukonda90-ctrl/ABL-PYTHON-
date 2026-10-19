# Student Marks and Grade Calculator
# Concepts: input/output, type conversion, lists, arithmetic, if-elif-else

def main():
    marks = []

    # Read marks for five subjects.
    for subject in range(1, 6):
        mark = float(input(f"Enter marks for subject {subject} (0-100): "))

        if mark < 0 or mark > 100:
            print("Invalid marks. Enter a value from 0 to 100.")
            return

        marks.append(mark)

    total = sum(marks)
    percentage = total / len(marks)

    # Grade boundaries used for this assignment.
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
