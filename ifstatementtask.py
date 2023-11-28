# Take three inputs from a user, separately. Print the largest of the numbers.
#Hint: Determine what type of data is taken in as input

in1 = int(input("Enter first number: "))
in2 = int(input("Enter second number: "))
in3 = int(input("Enter Third number: "))
# print (type(in1))
if (in1>in2 and in1>in3):
    print("Number one is the largest number")
elif (in2>in1 and in2>in3):
    print("Number two is the largest number")
else:
    print("Number three is the largest number")


