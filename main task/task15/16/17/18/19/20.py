# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:

basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter the benefits: "))

gross_salary = basic_salary + benefits
print(gross_salary)

if (gross_salary <= 5999):
    nhif = 150
elif (gross_salary >= 6000 and gross_salary <= 7999):
    nhif = 300
elif (gross_salary >= 8000 and gross_salary <= 11999):
    nhif = 400
elif (gross_salary >= 12000 and gross_salary <= 14999):
    nhif = 500
elif (gross_salary >= 15000 and gross_salary <= 19999):
    nhif = 600
elif (gross_salary >= 20000 and gross_salary <= 24999):
    nhif = 750
elif (gross_salary >= 25000 and gross_salary <= 29999):
    nhif = 850
elif (gross_salary >= 30000 and gross_salary <= 34999):
    nhif = 900
elif (gross_salary >= 40000 and gross_salary <= 44999):
    nhif = 950
elif (gross_salary >= 45000 and gross_salary <= 49999):
    nhif = 1000
elif (gross_salary >= 50000 and gross_salary <= 54999):
    nhif = 1100
elif (gross_salary >= 60000 and gross_salary <= 59999):
    nhif = 1200
elif (gross_salary >= 70000 and gross_salary <= 69999):
    nhif = 1300
elif (gross_salary >= 80000 and gross_salary <= 79999):
    nhif = 1400
elif (gross_salary >= 90000 and gross_salary <= 89999):
    nhif = 1500
elif (gross_salary >= 100000 and gross_salary <= 99999):
    nhif = 1600
else:
    nhif = 1700
print (f"NHIF: {nhif}")


# # Continue with the program above, 
# then use  the gross salary to find the NSSF. 
# # To find the Kenya NSSF Rate using. 
# Compute NSSF using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF.

basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter the benefits: "))

gross_salary = basic_salary + benefits
rate = 0.06

if (gross_salary > 0 and gross_salary <= 18000):
    nssf = 18000

# 17
# Continue with the same program 
# and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
nhdf = gross_salary * 0.015
print(nhdf)

# 18
taxable_income = gross_salary - (nssf+nhdf)
print(taxable_income)

#19
relief =2400
if taxable_income <= 2400:
    payee = (taxable_income*0.1)-relief
elif (taxable_income > 2400 and taxable_income <= 32333):
    payee == ((2400*0.1)+(8333*0.25)+((taxable_income-32333)*0.3))-relief
print(payee)

# 20
net_salary =gross_salary - (nhif + nhdf + nssf + payee)