# program that takes 3 form inputs or from the terminal, and stores them in three variables. 
# Return the largest of the three. Do this without using the the inbuilt max () function!

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
numbers = [number1, number2, number3]
print(f" The largest number is:", max(numbers))
