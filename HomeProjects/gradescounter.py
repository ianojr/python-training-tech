# A program that will count the marks of each student and tell them their grades.

maths = float(input("Enter the maths grade: "))
english = float(input("Enter the english grade: "))
swahili = float(input("Enter the swahili grade: "))
chem = float(input("Enter the chemistry grade: "))

# Calculate the total Marks
def calc_grades(maths, english, swahili, chem):
    marks = (maths + english + swahili + chem)
    return marks
total_grades = calc_grades(maths, english, swahili, chem)
# Validate the input.
if (total_grades > 400):
    print("Invalid Marks! Ensure you enter valid marks.")
    print("The highest mark should be 100")
else:
    print (f"The total score is: {total_grades}")

    # Calculate the total Avg
    def asign_avg(total_grades):
        avg = (total_grades/4)
        return avg
    average = asign_avg(total_grades)
    print(f"The Average is: {average}")

    # Asign grade to averages.
    def asign_grade(average):
        if (average >= 70 and average <= 100):
            grade = "A"
        elif (average >= 60 and average < 70):
            grade = "B"
        elif (average >= 50 and average < 60):
            grade = "C"
        elif (average >= 40 and average < 50):
            grade = "D"
        else:
            grade = "E"
        return grade
    grade_ans = asign_grade(average)
    print(f"Your grade is: {grade_ans}")
