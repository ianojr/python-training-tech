# A program which get a phone number from a user. Validates the number by checking if it starts with +254 or 07 or 71 or 254 or 01
# Convert the numer to start with +254

phone_number = input("Enter the phone number: ")
if (phone_number[0:4]=="+254" and len(phone_number)==13):
    print(f"{phone_number} is a valid number.")

elif (phone_number[0:2]=="07" and len(phone_number)==10):
    new_number = ("+254"+ phone_number[1:])
    print(new_number)

elif (phone_number[0:2]=="01" and len(phone_number)==10):
    new_number = ("+254"+ phone_number[1:])
    print(new_number)

elif (phone_number[0:1]=="7" and len(phone_number)==9):
    new_number = ("+254"+ phone_number)
    print(new_number)

elif (phone_number[0:3]=="254" and len(phone_number)==12):
    new_number = ("+" + phone_number)
    print(new_number)

else:
    print("Ensure you type a good phone number")