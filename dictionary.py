# Simple demonstration of dictionary in python.

customer = {
    "name": "Dave Paras",
    "age": 21,
    "is_verified": True
}

print(customer["name"])         #It will print the name

#get method for dictionary
print(customer.get("birthdate"))

# Adding new key-value pair

customer["dob"] = "Jan 1 1998"

print(customer["dob"])
