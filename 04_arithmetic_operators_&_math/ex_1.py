# calculate the circumference of a circle
import math 

# c = 2*pie*r
radius = float(input("Enter the radius: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")