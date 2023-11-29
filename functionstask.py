# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,
# then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
maths = float(input("Enter Maths: "))
eng = float(input("Enter English: "))
swa = float(input("Enter Swahili: "))
sci = float(input("Enter Science: "))
sos = float(input("Enter S.Studies: "))
def total_marks(maths, eng, swa, sci, sos):
    total = (maths + eng + swa + sci + sos)
    return total
ans = total_marks(maths, eng, swa, sci, sos)
print(f"The total marks is: {ans}")

def average(ans):
    average = (ans/5)
    return average
ans = average(ans)
print(f"The average is: {ans}")
print("")

def total_grade(ans):
    if (ans > 79):
        grade = "The grade is A"
    elif (ans >= 60 and ans <= 79):
        grade = "The grade is B"
    elif (ans >=50 and ans <= 59):
        grade = "The grade is C"
    elif (ans >= 40 and ans <= 49):
        grade = "The grade is D"
    else:
        grade = "The grade is E"
    return grade
ans = total_grade(ans)
print(ans)

