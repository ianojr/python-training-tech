# Write a program which accepts emails from user. 
# Validates and checks if its a valid email
users_email = input("Enter your Email: ")
if "@ " and "." in users_email:
    print("The Email is valid.")
else:
    print("The Email is invalid.")