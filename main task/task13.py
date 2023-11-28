# Write a program that takes the email and password as input from a user 
# and checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.

email = input("Enter the Email: ")
password = input("Enter the Password: ")
trials = 0
if (email == "admin@mail.com" and password == "Admin@123"):
    print("Login is Successful.")
else:
    for i in range(3):
        trials += 1
        if (trials == 3):
            print("Try Again!!!")
    print("Account Blocked!!!"
