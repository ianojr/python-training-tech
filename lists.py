# TASK: Create a List of days of the Week. Print the day today using an index.
week = ['Sunday', 'Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday']
print(week[3])
print(week.index('Wednesday'))
print(week[2][3])
print(len(week))


list1 = [[1,2,3,4,5],[23,24,25,26,34]]
print(list1[1][3])

numbers = [10,20,30,40,50]
numbers.append(60)
numbers.insert(0, 0)
numbers.extend([60,70,80,90])
del numbers[2]
numbers.pop(0)
numbers.reverse()
numbers.count(40)
numbers.sort()
print(numbers)
#print(70 in numbers)