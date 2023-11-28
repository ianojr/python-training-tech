n = "10"
for i in n:
    print(i)
print("")

for i in range(0, 1000):
    print(i)
print("")

#Looping through a list.
num = 0
nov_intake = ['Iano','Joy','Jane','Mercy','Alma','kamau']
for i in nov_intake:
    if i == nov_intake[3]:
        break
    num += 1
    print(num,":", i)
print("")

# looping through a control statement.
for i in range(20):
    if i == 5:
        continue
    print(i)

person = {"name:":"John Doe",
          "age:":60,
          "location:":"Nairobi",
          "email:":"ianojr@gmal.com"
        }
for key,value in person.items():
    print(key,value)
