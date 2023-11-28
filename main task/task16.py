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