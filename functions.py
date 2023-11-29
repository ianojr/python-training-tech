# How to create functions.

def calc_gross(benefits,basic_salary):
    gross_salary = basic_salary + benefits
    return gross_salary
# Calling the function
basic_salary = float(input("Enter basic salary:"))
benefits = float(input("Enter benefits: "))
gross_salary1 = calc_gross(basic_salary,benefits)
print(gross_salary1)
print("")
print("")

def triangle_area(a,b):
    area = (a*b)/2
    return area
a = float(input("Enter the height: "))
b = float(input("Enter the base: "))
ans = triangle_area(a,b)
print(ans)


def users_age(age):
    total = 2023 - age
    return total
age = int(input("Enter the age: "))
ans = users_age(age)
print(ans)


# A function that checks if a number is even or odd from the user:

def number_type(number):
    if (number % 2 == 0):
        num = "Even"
    else:
        num = "Odd"
    return num

number = float(input("Enter the number: "))
answer = number_type(number)
print(answer)
