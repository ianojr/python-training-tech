# Write a program that takes as input the speed of a car e.g 80. 
# If the speed is less than 70, it should print “Ok”. 
# Otherwise, for every 5 km/s above the speed limit (70), 
# It should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. 
# If the driver gets more than 12 points, the function should print: “License suspended”.

speed = int(input("Enter the speed: "))

speed_limit = 70
demerits_points = 0
if speed <= speed_limit:
    print('Ok')
elif (speed > speed_limit and speed < 75):
    demerits_points = 1
else:
    demerits_points = round((speed - speed_limit)/5)
    if demerits_points > 12:
        print("Lisence Suspended")
    else:
        print(demerits_points)
print(demerits_points)