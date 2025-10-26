# *args = allows you to pass multiple non-key arguements  , packs into tuple
# **kwargs = allows you to pass multiple keyword-arguements , packs into dictionary
#            * unpacking operator
#               

def add(a,b):
    return a+b

print(add(1,2)) # doesnt accept multiple arguements

def multiple_args(*args):
    return type(args)
print(multiple_args(1,2,3)) # accepts multiple arguements 

def multiple_args_2(*nums): # iterate over args
    total = 0
    for num in nums:
        total += num
    return total
print(multiple_args_2(1,2,3)) 

# function to display name

def display_name(*args):
    for arg in args:
        print(arg, end =" ")
        
display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III") 
