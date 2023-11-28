# Write a program that displays a number 1 to 50 inside a list.
list_of_numbers = []
for i in range (1, 51):
    list_of_numbers.append(i)
print(list_of_numbers)
print("")

# From 1 above display the ones divisible by 7 or 5:
list_of_numbers = []
for i in range (1, 51):
    if (i % 7 == 0 or i % 5 == 0):
        list_of_numbers.append(i)
print(list_of_numbers)
print("")

# Find the sum and averages of values in 10 to 40
sum = 0
for num in range (10, 41):
    sum += num
    average = sum / num
print("The sum is: ", sum)
print("The average is: ", average)
print("")

# put in a list the first ten odd numbers between 10 to 50
main =[]
for i in range (10,51):
    if i % 2 != 0:
        main.append(i)
        if len(main) == 10:
            break
print(f"The main is: ", main)