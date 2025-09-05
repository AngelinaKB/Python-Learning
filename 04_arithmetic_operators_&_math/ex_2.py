# calculate the area of a circle
import math

# a = pie*r²
radius = float(input("Enter the radius: "))
area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm²")