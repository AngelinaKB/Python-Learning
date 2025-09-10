# while loop = execute some code WHILE some condition remains True

# Example 1
name = input("Enter your name: ")

while name=="":
    print("You did not enter your name!")
    name = input("Enter your name: ")

print(f"Your name is {name.capitalize()}.")

# Example 2
food = input("Enter a food you like (press q to quit): ")
while not food== "q":
    print(f"You like {food}!")
    food = input("Enter a food you like (press q to quit): ")

print("Bye! ^-^")

# Example 3
num= int(input("Enter a number between 1 - 10: "))

while num<1 or num>10: 
    print(f"{num} is invalid!")
    num= int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")