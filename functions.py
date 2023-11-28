# How to create functions.

def calc_gross(benefits,basic_salary):
    gross_salary = basic_salary + benefits
    return gross_salary
# Calling the function
basic_salary = float(input("Enter basic salary:"))
benefits = float(input("Enter benefits: "))
gross_salary = calc_gross(basic_salary,benefits)
print(gross_salary)