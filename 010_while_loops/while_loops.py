# while loop = execute some code WHILE some condition remains True

name = input("Enter your name: ")

while name=="":
    print("You did not enter your name!")
    name = input("Enter your name: ")

print(f"Your name is {name.capitalize()}.")