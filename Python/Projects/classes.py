def calculate_area(length, width):
    area = length * width
    return area

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

usr_rectangle_length = int(input("Please enter your rectangle's length: "))
usr_rectangle_width = int(input("Please enter your rectangle's width: "))

usr_rectangle = Rectangle(usr_rectangle_length, usr_rectangle_width)

# Call the calculate_area function and capture the result in a variable
area_of_rectangle = calculate_area(usr_rectangle.length, usr_rectangle.width)

# Now, print the calculated area
print("Area of the rectangle:", area_of_rectangle)
