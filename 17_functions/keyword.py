# keyword arguements = an arguement preceded by an identifier 
#                      helps with readibility 
#                      order of arguements does not matter  
#                      

def hello(greeting, title, first, last): 
    return f"{greeting} {title} {first} {last}"

print(hello("Hello", "Mr.", "Spongebob", "Squarepants")) # positional arguements follow positional arguements 
print(hello("Hello", "Spongebob", "Squarepants", "Mr.")) 
print(hello("Hello", first = "Spongebob", last = "Squarepants", title ="Mr.")) 

# end arguement 
for x in range(1,11):
    print(x, end =" ")

# sep arguement
print()
print("1", "2", "3", "4", "5", sep = "-")

# function to generate a phone number

def generate_phone_no(country_code, area_code, first_digits, last_digits):
    return f"{country_code}-{area_code}-{first_digits}-{last_digits}"

phone_num = generate_phone_no(country_code= 1, area_code= 123, first_digits= 456, last_digits= 7890)
print(f"Your phone number is {phone_num}")
