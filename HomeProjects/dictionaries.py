capitals = {"Kenya":"Nairobi",
            "USA": "Washington",
            "India":"New_Delhi",
            "China":"Beijing"}
print(capitals)

# To get a value in a dictionary use a key.

print(capitals.get("Kenya"))
print("")

if (capitals.get("Nigeria")):
    print("The country is Available")
else:
    print("the country is not available for now")
print("")

capitals.update({"Uganda": "Kampala"})
print(capitals)
print("")

print(capitals.keys())
print(capitals.values())
