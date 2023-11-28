# Grading marks according to what a student has scored.
marks = round(49.5)

if (marks >= 60):
    print ("A")
elif (marks >= 50):
    print("B")
elif (marks >= 40):
    print("C")
else:
    print("Fail")


# TAke users input and ask them for their marks. Print their grades
average_marks = input("Enter your marks: ")
if (int(average_marks) >= 70):
    print("A")
elif (int(average_marks) >= 60):
    print("B")
elif (int(average_marks) >= 50):
    print("C")
elif (int(average_marks) >= 40):
    print("D")
else:
    print("E")


# Check if a number is odd or even
num = input("Enter the number: ")
num = int(num)
if num%2 == 0:
    print("Even")
else:
    print("Odd")