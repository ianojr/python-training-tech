fruits = ["apple","orange","banana","coconut"]
print(fruits)
print(fruits[1])
print(fruits[2:])

for fruits in fruits:
    print(fruits)


print(help(fruits))
print(len(fruits))

names = ["Ian", "Joy", "Jane", "Ben", "Usher"]
print(names)
print ("Ian" in names)


# Methods in a list.

numbers = [12,23,34,45,56,67,78,89,32]
numbers.append(100)
numbers.remove(12)
print (numbers)
print("")
print("")

# SETS

set1 = {"ian", "ben", "joy", "ann"}
print (set1)
set1.remove("ben")
print(len(set1))