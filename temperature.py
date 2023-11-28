#Take as input from a user the temperature if the temperature is above 30°C 
#display “The temperature is too high”, otherwise display “Normal temperature”

temperature = float(input("Enter the temperature: "))
# if (type(temperature) == float):
if (temperature > 30 and temperature < 100):
    print("The temperature is too high! ")
elif (temperature < 15):
    print("Tempearature too low!")
elif (temperature >= 15 and temperature < 30):
    print("Normal temperature. ")
else:
    print("Extreme temperature!!!")
