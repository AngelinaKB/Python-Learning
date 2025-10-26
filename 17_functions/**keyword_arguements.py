
# **kwargs = allows you to pass multiple keyword-arguements , packs into dictionary


def print_address(**kwargs):
    return type(kwargs)

print(print_address(street ="123 Fake Street",
                    city= "Detroit", 
                    state= "MI", 
                    zip="54321"))

# iterate over kwargs
def print_address_iterate(**kwargs):
    for key,value in kwargs.items():
        print(key, ":", value)

print(print_address_iterate(street ="123 Fake Street",
                    city= "Detroit", 
                    state= "MI", 
                    zip="54321"))

# shipping label program

def shipping_label(*args, **kwargs):
    print("To,")
    for arg in args:
        print(arg, end = " ")
    
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} { kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

print(shipping_label("Dr.", "Spongebob", "Squarepants", "III", 
                    street ="123 Fake Street",
                    city= "Detroit", 
                    state= "MI", 
                    zip="54321"))
