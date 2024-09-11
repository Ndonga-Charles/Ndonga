import math
# Function to calculate the area of a rectangle
def calculate_rectangle_area(width, length):
    return width * length
 
def calculate_circle_area(radius):
    return math.pi * radius * radius #math.pi gives the value of pi
 
 
# Main function
def main():
    length = 5
    width = 10
    radius = 7
    rectangle_area = calculate_rectangle_area(width, length)
    print(f"The area of the rectangle is {rectangle_area}")
    circle_area = calculate_circle_area(radius)
    print(f"The area of the circle is {circle_area}")

# Calling the main function to execute the program
main()
 
 
# User input
# width = float(input("Enter the width of the rectangle: "))
# length = float(input("Enter the length of the rectangle: "))
