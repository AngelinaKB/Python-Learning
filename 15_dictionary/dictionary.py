# dictionary = a collection of {key: value} pairs
#              ordered and changeable. No duplicates

capitals = { 
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# attributes and methods of dictionary
dir(capitals)

# to know more about the attributes and methods of dictionary
help(capitals)

# to get a value from dictionary 
print(capitals.get("USA"))

# check if a key exists in the dictionary
if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("Does not exist.")

# Update values - can update existing value or add new value
capitals.update({"Germany": "Berlin"})   # adds a new key-value pair
capitals.update({"USA": "Detroit"})      # updates existing value for key "USA"

# remove key-value pair
capitals.pop("USA")                      

# to remove latest key-value pair 
capitals.popitem()                       

# to get all keys without values
capitals.keys()                          

for key in capitals.keys():              # iterate through all keys
    print(key)

# to get all values
capitals.values()                        

for value in capitals.values():          # iterate through all values
    print(value)

# get all key-value pairs
print(capitals.items())                  

for key, value in capitals.items():      # iterate through all key-value pairs
    print(key, ":", value)

# clear the dictionary 
capitals.clear()                         
