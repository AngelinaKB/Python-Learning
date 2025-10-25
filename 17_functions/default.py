# default arguements = a default value for certain parameters
#                      default is used when that arguement is omitted
#                      make your functions more flexible, reduces # of arguements 
#                      1. postional 2. DEFAULT 3. keyword 4. arbitrary

def net_price(list_price, discount = 0, sales_tax = 0.05):
    return list_price *  (1 - discount) * (1 + sales_tax)

print(net_price(500))
print(net_price(500, 0.1)) # 10% discount
print(net_price(500, 0.1, 0)) # no sales tax
