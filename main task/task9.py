# Write a program called stars. It should prompt the user for a number,
# and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....

star = ""
number = int(input("Enter the number: "))
count = ""
for i in range(number):
    star += "*"
    count += "."
    print(star + count)