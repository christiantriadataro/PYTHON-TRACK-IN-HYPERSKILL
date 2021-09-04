# Write a program that read two integers (the first is always 
# positive) and calculates the logarithmic value of the first integer
# with the second integer as a base. If the second integer is
# negative, 0, or 1, return the natural log of the first number.

# Use the function log() from the math module. With one
# argument, it returns the natural logarithm of a number. It can
# also take two arguments: a number and a logarithmic base

# Print the result rounded to 2 decimal places
import math
a, b = abs(int(input())), int(input())

print(round(math.log(a), 2) if b < 2 else round(math.log(a, b), 2))


