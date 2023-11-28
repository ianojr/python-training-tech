# 1. Print KES
# 2. Print 560
# 3. Print Maths
# 4. In the dictionary with the key currency, add another key “amount” with value 90
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
# 6. Change the name “John” to “Jane” . 

my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]

kes = my_ds[3][2]["currency"]
print(kes)

k560 = my_ds[2]
print(k560)

maths = my_ds[3][1]
print(maths)

my_ds1 = my_ds[3][2]["amount"]=90
print(my_ds)

987
rev = str(my_ds[4])
rev = rev[2::-1]
print(rev)

ans = my_ds[5] = list(my_ds[5])
my_ds[5][1] = "Jane"
my_ds[5] = tuple(my_ds[5])
print(my_ds)
