# collection = single "variable" used to store multiple values
# List [] = ordered and changeable. Duplicates OK
# Set {} = unordered and immutable, but Add/Remove OK. NO duplicates.
# Tuple () = ordered and unchangeable. Duplicates OK. Faster than lists

# Creating and Accessing Elements
fruits = ["apple", "banana", "orange", "pear"]

 # Access last element
fruits[-1]       
# Access elements from index 0 to 2
fruits[:3]        
# Access every 2nd element
fruits[::2]       

# Loop through list
for x in fruits:  
    print(x)

# Length of list
len(fruits)             

# Check if element exists
"apple" in fruits      

# Find index of element
fruits.index("apple")    

# Count occurrences
fruits.count("apple")    

# Change value at index
fruits[0] = "pineapple"          

# Add at end
fruits.append("jackfruit")          

# Insert at index
fruits.insert(2, "watermelon") 

# Add multiple elements
fruits.extend(["grapes", "melon"])  

# Remove by value
fruits.remove("banana")   

# Remove last element
fruits.pop()              

# Remove by index
fruits.pop(1)    

# Delete element by index
del fruits[0]            

# Remove all elements
fruits.clear()          

 # Sort ascending
fruits.sort()               

# Sort descending
fruits.sort(reverse=True)       

# Reverse order
fruits.reverse()               

# Shallow copy
copy_list = fruits.copy()   

# Join two lists
new_list = fruits + ["kiwi"]    

# Repeat list elements
fruits *= 2                     

numbers = [10, 20, 5, 15]
#  Maximum value
max(numbers)  

# Minimum value
min(numbers)  

# Sum of all elements
sum(numbers)     

# Returns a sorted copy (does not modify original)
sorted(numbers)  
