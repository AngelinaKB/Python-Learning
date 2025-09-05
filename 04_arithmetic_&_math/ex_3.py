# calculate the hypotenuse of a right angle triangle
import math

# c = √(a² + b²)
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b,2))

print(f"Side C = {round(c, 2)}")