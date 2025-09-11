# format specifiers = {value:flags} format a value based on what
#                              flags are inserted

# .(digit)f = round to that many decimal places (fixed point)
# :(digit) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3244654.14159
price2 = -987245.65
price3 = 126465.34


# rounded off decimal
print("\n rounded off decimal") 
print(f"Price 1 is {price1:.1f}")
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.3f}")

# space padded 
print("\n space padded ")
print(f"Price 1 is {price1:10}")
print(f"Price 2 is {price2:10}")
print(f"Price 3 is {price3:10}")

# 0 padded 
print("\n zero pad that many spaces")
print(f"Price 1 is {price1:010}")
print(f"Price 2 is {price2:010}")
print(f"Price 3 is {price3:010}")

# left justify
print("\n left justify")
print(f"Price 1 is {price1:<10}")
print(f"Price 2 is {price2:<10}")
print(f"Price 3 is {price3:<10}")

# right justify
print("\n right justify")
print(f"Price 1 is {price1:>10}")
print(f"Price 2 is {price2:>10}")
print(f"Price 3 is {price3:>10}")

# center align
print("\n center align")
print(f"Price 1 is {price1:^10}")
print(f"Price 2 is {price2:^10}")
print(f"Price 3 is {price3:^10}")

# + or - numbers
print("\n place + or - in front of numbers")
print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:-}")
print(f"Price 3 is {price3:+}")

# space for positive values
print("\n use space infront of positive numbers")
print(f"Price 1 is {price1: }")
print(f"Price 2 is {price2: }")
print(f"Price 3 is {price3: }")

# comma seperated 1000's place
print("\n comma seperated 1000's place")
print(f"Price 1 is {price1:,}")
print(f"Price 2 is {price2:+,.2f}")

print(f"Price 3 is {price3:+,.3f}")
