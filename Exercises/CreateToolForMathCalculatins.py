# pylint: disable=invalid-name
"""Create a custom math tool that computes a triangle hypotenuse."""

import math

from langchain_core.tools import tool


# Define this math function as a tool
@tool
def hypotenuse_length(lengths: str) -> float:
    """Calculate hypotenuse length from comma-separated side values."""

    # Split the input string to get the lengths of the triangle
    sides = lengths.split(",")

    # Convert the input values to floats, removing extra spaces
    a = float(sides[0].strip())
    b = float(sides[1].strip())

    # Square each of the values, add them together, and find the square root
    return math.sqrt(a**2 + b**2)
