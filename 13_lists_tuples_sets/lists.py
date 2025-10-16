# collection = single "variable" used to store multiple values
# List [] = ordered and changeable. Duplicates OK
# Set {} = unordered and immutable, but Add/Remove OK. NO duplicates.
# Tuple () = ordered and unchangeable. Duplicates OK. Faster

fruits =  ["apple", "banana", "orange", "pear"]
# indexing a list
print(fruits[-1])

# index range
print(fruits[:3])

# adding a step
print(fruits[::2])

# loop a list
for x in fruits:
  print(x)

# in-built functions
# gives length of list
print(len(fruits))

# find if an element in list,  gives boolean answer 
print("apple" in fruits)

# change values after creation
fruits[0]="pineapple"
for x in fruits:
  print(x)
  
# append element
fruits.append("jackfruit")
print(fruits)

# remove element
fruits.remove("jackfruit")
print(fruits)

# insert element at certain postion
fruits.insert(2,"watermelon")
print(fruits)

# sort the list
fruits.sort()
print(fruits)

# reverse a list
fruits.reverse()
print(fruits)

# index of an element
print(fruits.index("pineapple"))

# count number of elements
print(fruits.count("apple"))

# clear a list
fruits.clear()
print(fruits)