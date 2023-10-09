import math

# .format method
first_name = "Corey"
last_name = "Ford"
full_name = "{1} {0}".format(first_name, last_name)
print(full_name)

area_of_circle = math.pi * (2.4 ** 2)
print(f"Area: {area_of_circle:1.2f}".format())