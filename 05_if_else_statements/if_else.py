# if = you do something if condition is True
# else = you dont something else

x = 3

if x > 5:
    print("x is greater than 5") 
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


response =  input("Would you like food? (Y/N): ").upper()
if response == "Y":
    print("Here is some sushi! 🍣 (๑ᵔ⤙ᵔ๑ 🥢)")
else:
    print("\nOkay! Maybe later?")
    