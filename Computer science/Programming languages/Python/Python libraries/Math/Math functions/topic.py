# Theory: Math functions
import math
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
# - abs(x) returns the absolute value of x (i.e value without a
#   regard to its sign);
# - round(x, ndigits) returns x rounded to ndigits number of
#   decimal part digits;
# - pow(x, y) returns x raised to the power of y;
# - max(a, b, c, ...) returns the largest argument;
# - min(a, b, c, ...) returns the smallest argument.

abs_integer = abs(-10)  # 10
abs_float = abs(-10.0)  # 10.0

round_integer = round(10.0)      # 10, returns integer when ndigits is omitted
round_float = round(10.2573, 2)  # 10.26

pow_integer = pow(2, 10)  # 1024
pow_float = pow(2.0, 10)  # 1024.0

largest = max(1, 2, 3, 4, 5)   # 5
smallest = min(1, 2, 3, 4, 5)  # 10

# abs() and pow() functions have equivalents in the math
# module. The key difference of math.fabs() and math.pow() is
# that they always return floats:

fabs_integer = math.fabs(-10)  # 10.0
fabs_float = math.fabs(-10.0)  # 10.0

pow_integer = math.pow(2, 10)  # 1024.0
pow_float = math.pow(2.0, 10)  # 1024.0

# Remember that in order to use definitions from math, you
# should import the module first.

# Should you raised x to the power y, and then forgot y. You can
# recover it using the math.log() function:
x = 2
y = 10
pow = math.pow(x, y)        # 1024.0
log = math.log(pow, x)      # 10.0

# math.log(pow, x) returns z such that x raised to the power z
# equals pow. If the second argument x (called the base of the
# logarithm) is omitted, it is considered equal to a special number
# e (approximately 2.718):

natural_log = math.log(1024)  # 6.931471805599453

# Besides the round() function, we can use floor() and ceil()
# from the math module to grain largest from floats:

# - math.floor(a) returns the nearest integer less than or
#   equal to a;
# - math.ceil(a) returns the nearest integer greater than or
#    equal
