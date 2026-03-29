'''Create a tool for math calculations
It's time to build your tool. Let's imagine you run a small construction company and need to calculate the length of one side of a roof. If you know the lengths of two beams that support the roof at a right angle, you can use their lengths to calculate the length of the roof using the hypotenuse formula below.


Use the necessary decorator to define the function as a tool.
To find the hypotenuse, use the .split() method on the input string to extract the two other lengths of a right-sided triangle.
Convert each triangle side, a and b, to floats and use .strip() to remove any extra spaces from the values.
Use Python's math module to square the lengths a and b, sum their values, and find their square root to reveal the length of the roof.

'''
from json import tool


# Define this math function as a tool
@tool
def hypotenuse_length(input: str) -> float:
    """Calculates the length of the hypotenuse of a right-angled triangle given the lengths of the other two sides."""

    # Split the input string to get the lengths of the triangle
    sides = input.split(',')

    # Convert the input values to floats, removing extra spaces
    a = float(sides[0].strip())
    b = float(sides[1].strip())

    # Square each of the values, add them together, and find the square root
    return math.sqrt(a**2 + b**2)
