# Create a tuple
fruits = ("apple", "banana", "orange", "pear", "coconuts", "coconuts")
print("Tuple:", fruits)

# -------------------------------
# Basic Tuple Operations
# -------------------------------

# Length of tuple
print(len(fruits))

# Check if an element exists (returns boolean)
print("Is 'apple' in tuple?:", "apple" in fruits)

# Find index of an element
print(fruits.index("apple"))

# Count how many times an element appears
print(fruits.count("coconuts"))

# Iterate over tuple
for fruit in fruits:
    print(fruit)

# -------------------------------
# Built-in Functions
# -------------------------------

# Maximum and minimum (alphabetical order for strings)
print(max(fruits))
print(min(fruits))

# Sorting the tuple (returns a list)
print(sorted(fruits))

# Sum function (works only with numbers)
numbers = (5, 10, 15, 20)
print(sum(numbers))
print(max(numbers))
print(min(numbers))

# -------------------------------
# Tuple Operations
# -------------------------------

# Concatenation
new_fruits = fruits + ("grapes", "mango")
print(new_fruits)

# Repetition
print(fruits * 2)

# Slicing
print(fruits[:3])
print( fruits[-2:])

