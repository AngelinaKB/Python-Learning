
# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#   X if condidtion else Y

num = -6
print("positive" if num>=0 else "negative")



age = 25
status= "Adult" if age>=18 else "Child"
print(status)



user_role = "admin"
access_level = "Full access" if user_role=="admin" else "Limited Access"
print(access_level)