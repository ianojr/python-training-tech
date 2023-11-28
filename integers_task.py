# Convert a float to an integer with an inbuilt function in Python temp = 56.8926 to 57
temp = 56.8926
print(round(temp))

# Convert the float below to give the results as follows temp = 56.8926 to 56.89
temp = 56.8926
print(round(temp,2))

# Convert the float below to give the results as follows temp = 56.8926 to 56.893
temp = 56.8926
print(round(temp,3))

# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float
temp = "56.8926"
temp = float(temp[2:] + "." + temp[4:])
print(temp)