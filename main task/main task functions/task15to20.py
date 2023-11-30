# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK

basic_salary = float(input("Enter the basic salary: "))
benefits = float(input("Enter the Benefits: "))

def calc_salary(basic_salary,benefits):
    gross_salary = (basic_salary + benefits)
    return gross_salary

gross_salary = calc_salary(basic_salary,benefits)
print(f"The Gross Salary is: {gross_salary}")
print("")

def nhif(gross_salary):
    if (gross_salary <= 5999):
        nhif = "150"
    elif (gross_salary >= 6000 and gross_salary < 7999):
        nhif = "300"
    elif (gross_salary >= 8000 and gross_salary < 11999):
        nhif = "400"
    elif (gross_salary >= 12000 and gross_salary < 14999):
        nhif = "500"
    elif (gross_salary >= 15000 and gross_salary < 19999):
        nhif = "600"
    elif (gross_salary >= 20000 and gross_salary < 24999):
        nhif = "750"
    elif (gross_salary >= 25000 and gross_salary < 29999):
        nhif = "850"
    elif (gross_salary >= 30000 and gross_salary < 34999):
        nhif = "900"
    elif (gross_salary >= 35000 and gross_salary < 39999):
        nhif = "950"
    elif (gross_salary >= 40000 and gross_salary < 44999):
        nhif = "1000"
    elif (gross_salary >= 45000 and gross_salary < 49999):
        nhif = "1100"
    elif (gross_salary >= 50000 and gross_salary < 59999):
        nhif = "1200"
    elif (gross_salary >= 60000 and gross_salary < 69999):
        nhif = "1300"
    elif (gross_salary >= 70000 and gross_salary < 79999):
        nhif = "1400"
    elif (gross_salary >= 80000 and gross_salary < 89999):
        nhif = "1500"
    elif (gross_salary >= 90000 and gross_salary < 99999):
        nhif = "1600"
    else:
        nhif = "1700"
    return nhif
nhif = nhif (gross_salary)
print(f"The nhif is: {nhif}")
print("")


# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF.
def calc_nssf(gross_salary):
    nssf = (0.06 * gross_salary)
    return nssf
nssf = calc_nssf(gross_salary)
print(f"The NSSF is: {nssf:.2f}")
print("")


# Continue with the same program and calculate an individual’s NHDF using:
# i.e NHDF = gross_salary *  0.015
def calc_nhdf (gross_salary):
    nhdf = (gross_salary * 0.015)
    return nhdf
nhdf = calc_nhdf(gross_salary)
print(f"The NHDF is: {nhdf:.2f}")
print("")


# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF) 
def tax_income(gross_salary, nssf, nhdf):
    income = (gross_salary - (nssf + nhdf))
    return income
taxable_income = tax_income(gross_salary, nssf, nhdf)
print(f"The Taxable Income is: {taxable_income}")
print("")


# Continue with the same program and find the person's 
# PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK

# relief =24000
# if taxable_income <= 24000:
#     payee = (taxable_income*0.1)-relief
# elif (taxable_income > 24000 and taxable_income <= 32333):
#     payee == ((24000*0.1)+(8333*0.25)+((taxable_income-32333)*0.3))-relief
# print(payee)
def calc_payee(taxable_income, relief=2400):
    if taxable_income <= 24000:
        payee = ((taxable_income*0.1)-relief)
    elif (taxable_income > 24000 and taxable_income <= 32333):
        payee = ((24000*0.1)+(8333*0.25)+((taxable_income-32333)*0.3))-relief
    else:
        payee = ((24000*0.1)+(8333*0.25)+((taxable_income-32333)*0.3))-relief
        return payee
payee = calc_payee(taxable_income)
print(f"The PAYEE is: {payee:.2f}")
print("")

# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
def calc__net_salary(gross_salary,nhdf,nssf,payee):
    net_salary = gross_salary - (nhdf +  nssf + payee)
    return net_salary
total_net_salary = calc__net_salary(gross_salary,nhdf,nssf,payee)
print(f"The total Net Salary is: {total_net_salary}")