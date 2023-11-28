# Write a program input a password. 
# Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. 
# After you show them a message , the account is blocked.

# password = input("Enter the password: ")
# saved_password = "admin@123"
# if password == saved_password:
#     print("Account Opened")
# else:


saved_email = "admin@123"
attempts = 4
for i in range (attempts):
    user_email = input("Enter your Email:")
    if (user_email == saved_email):
        print("Account Opened! ")
        break
    print("")
else:
    print("Email blocked!!!")
print("")
print("")

# Using the While loop.
correct_password = "admin@123"
attempts = 0
while attempts < 4:
    password = input("Enter the password: ")
    if password == correct_password:
        print('Access Granted')
        break
    else:
        print("Incorrect Password!!!")
        attempts += 1
        if attempts == 4:
            print("Account blocked!!!!")
