# Theory: Math functions

# We already learned how to perform basic arithmetics in Python.
# We covered addition, subtraction, multiplication, division and
# several other built-in operations. But if we want to do more
# complex operations on numbers we can use built-in
# mathematical functions or functions from the math module.

# math module provides useful mathematical functions and
# constants. This module is available on every platform in the
# standard library.

# 1. Advanced arithmetics
# There are built-in functions abs, round, pow, max and min:
# - abs(x) returns the absolute value of x (i.e. value without a
#   regard to its sign);
# - round(x, ndigits) returns x rounded to ndigits number of 
#   decimal part digits;
# - pow(x, y) returns x raised to the power of y;
# - max(a, b, c, ...) returns the largest argument;
# - min(a, b, c, ...) returns the samllest argument.

abs_integer = abs(-10)  # 10
abs_float = abs(-10.0)  # 10.0

round_integer = round(10.0)      # 10, returns integer
round_float = round(10.2573, 2)  # 10.26

pow_integer = pow(2, 10)  # 1024
pow_float = pow(2.0, 10)  # 1024.0

largest = max(1, 2, 3, 4, 5)   # 5
smallest = min(1, 2, 3, 4, 5)  # 1

# abs() and pow() functions have equivalents in the math
# module. The key difference of math.fabs() and math.pow() is
# that they always return floats:
import math

fabs_integer = math.fabs(-10)   # 10.0
fabs_float = math.fabs(-10.0)   # 10.0

pow_integer = math.pow(2, 10)   # 1024.0
pow_float = math.pow(2.0, 10)   # 1024.0

# Remember that in order to use definitions from math, you
# should import the module first.

# Suppose you raised x to the power y, and then forgot y. You can
# recover it using the math.log() function:

import math

x = 2
y = 10
pow = math.pow(x, y)     # 1024.0
log = math.log(pow, x)   # 10.0

# math.log(pow, x) returns z such that x raised to the power z 
# equals pow. If the second argument x (called the base of the
# logarithm) is omitted, it is considered equal to a special number
# e (approximately 2.718):
import math

natural_log = math.log(1024)  # 6.931471805599453

# Besides the round() function, we can use floor() and ceil()
# from the math module to obtain integer values from floats:
# - math.floor(a) returns the nearest integer less than or
#   equal to a;
# - math.ceil(a) returns the nearest integer greater than or
#   equal to a;
# The math module also provides the sqrt function to calculate
# the square root of a number.

import math

result = math.sqrt(100)  # 10.0


# 2. Geometry
# The number π is often used in geometry and other
# mathematical fields. It is the ratio of the circumference of a
# circle to its diameter. It can be found in the math module as pi.

# The next example shows how to calculate the circumference of 
# a circle:
import math

r = 3.5
circumreference = 2 * math.pi * r # 21.991

# There are also common trigonometric functions available in the 
# math module:
# - math.cos(a) returns the cosine of a radians;
# - math.sin(a) returns the sine of a radians;
# - math.degrees(a) returns angle a converted from radians to
#   degrees;
# - math.radians(a) returns angle a converted from degrees to
#   radians.

import math

deg = 60.0
x = math.radians(deg)  # 1.047...

cos = math.cos(x)   # 0.500...
sin = math.sin(x)   # 0.866...

degrees = math.degrees(x)  # 59.999...

# As you can see, due to a limited precision of floats the value of
# degress is actually 59.99999999999999 instead of expected
# 60.0

# It is impossible to cover all the math module in this topic so you
# can learn more from its documentation.

# 3. The volume of a cylinder
# Let's assume we have a cylinder with the height h = 5 and the
# radius of the base r = 3. The formula for the volume of a
# cylinder is V = πr^2h. This is how we can calculate the volume
# using Python.

import math

h = 5
r = 3

volume = math.pi * math.pow(r, 2) * h  # 141.3716

print(round(volume, 1))   # 141.4

# In the code above, we used the round function to get a prettier
# value for printing.

# 4. Summary
# In this topic, we've learned several new advanced arithmetic
# operations, familiarized ourselved with arithmetics and 
# geometry in math module, and calculated the volume of a
# cylinder. As you can see, it is possible to round a number or find
# a maximum value in Python using just built-in functions. 
# However, now you can use functions from the math module for
# more advanced tasks.