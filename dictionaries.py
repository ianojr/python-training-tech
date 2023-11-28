# Creating dictionaries.
person = {"name":"John Doe",
          "age":60,
          "location":"Nairobi",
          "email":"ianojr@gmal.com"
        }
#Accessing and updating a dictionary
print(person["age"])
person["age"]=25
person["location"]="Nakuru"
person["email"]="ianojra2@gmail.com"
person["name"]="Ian Rugi"
print(person["name"])

print(person)
# Adding a key value
person["gender"]="Female"
person["gender"]="Male"

person["address"]="518-00100"
print(person)

#Dictionary methods
print(person.pop("name"))
print(person.get("age"))
print(person.copy())
print(person.popitem())
print(len(person))

# Updating data
new_data={"Career":"AI Engineering"}
person.update(new_data)
print(person)

# How to know the keys
print(person.keys())
# Seeing only the values
print(person.values())
