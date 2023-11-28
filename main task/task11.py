# Write a program that takes the date of birth of a person 
# and the program outputs the age in terms of years,months,days TODAY.

current_day = 24
current_month = 11
current_year = 2023

birth_day = int(input("Enter the day that you were born: "))
birth_month = int(input("Enter the month that you were born: "))
birth_year = int(input("Enter the year that you were born: "))

age_day = birth_day - current_day
print(age_day)