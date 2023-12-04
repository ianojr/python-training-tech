# Calculating the total Marks of all students.

no_of_students = int(input("Enter the number of students: "))

count = 0
for i in range(0, no_of_students):
    marks = float(input("Enter the marks of a student: "))
    total_marks = count + marks
print(f"The class total mark is: {total_marks}")
