# keyword arguements = an arguement preceded by an identifier 
#                      helps with readibility 
#                      order of arguements does not matter  
#                      

def hello(greeting, title, first, last): 
    return f"{greeting} {title} {first} {last}"

print(hello("Hello", "Mr.", "Spongebob", "Squarepants")) # positional arguements follow positional arguements 
print(hello("Hello", "Spongebob", "Squarepants", "Mr.")) 
print(hello("Hello", first = "Spongebob", last = "Squarepants", title ="Mr.")) 

for x in range(1,11):
    print(x, end =" ")
    
print()
print("1", "2", "3", "4", "5", sep = "-")
