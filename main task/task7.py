# Write that prompts the user to input student marks. The input should be between 0 and 100.
# Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
users_grade = float(input("Enter the grade of the student: "))
if users_grade > 79: print("The grade is: A")
elif users_grade > 60: print("The grade is: B")
elif users_grade > 50: print("The grade is: C")
elif users_grade > 40: print("The grade is: D")
else: print("The grade is E")