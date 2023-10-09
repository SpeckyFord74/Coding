import math

radius = float(input("Please enter the radius of your circle: "))

circumference = round(2 * (math.pi * radius), 2)
diameter = round(2 * radius, 2)
area = round(2 * (math.pi * (radius**2)), 2)

print(f"Circumference: {circumference}\nDiameter: {diameter}\nArea: {area}")