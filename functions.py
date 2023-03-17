"""
Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
Equation of an area of a triangle is,
area = (1/2)*base*height
"""


def calculate_area(base=0, height=0):
    return (1 / 2) * base * height


print(calculate_area(2, 3))

"""
Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take triangle as a default shape
"""


def calculate_area(base=0, height=0, shape='triangle'):
    if shape == 'triangle':
        return (1 / 2) * base * height
    else:
        return base * height


print(calculate_area(2, 3, 'rectangle'))

"""
Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
"""


def print_pattern(n):
    for i in range(0, n+1, 1):
        for j in range(0, i, 1):
            print('*', end='')
        print()


print_pattern(4)
