import math 

#Pythagorus' theorum
side_a = float(input("Please enter side a: "))
side_b = float(input("Please enter side b: "))

side_c = (side_a ** 2) + (side_b ** 2)
side_c_final = math.sqrt(side_c)

print(side_c_final)