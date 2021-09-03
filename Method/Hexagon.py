# The class Hexagon represents the regular hexagons (all sides
# are equal in length and all angels equal 120). The only
# parameter needed to create a regular heaxgon is the length of 
# its side t.

# Create a method get_area that calculates the area of the 
# hexagon according to the formula:

# The name of the method has to be get_area! The method
# doesn't receive any parameters and it doesn't print anything, 
# just returns the calculated area (rounded to 3 decimals). You do
# NOT need to call the method in your program!

# To calculate the square root use the math.sqrt(x) method.
# (The math module has already been imported.)

# Nothing else is required (you do NOT need to work with the
# input).

import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length
    
    def get_area(self):
        s = (3 * (math.sqrt(3) * (self.side_length ** 2))) / 2
        return round(s, 3)

Hex = Hexagon(float(input()))

print(Hex.get_area())
