# Many years ago, when Paul went to school, he did not like using
# Heron's formula to calculate the area of a triangle, because he
# considered it to be very complex. One day he decided to help all
# the students in his school by writing a program that calculated
# the area of a triangle by its three sides.

# However, there was a problem: as Paul did not like the formula, 
# he did not memorize it. Help him finish this act of kindness and
# write the program following Heron's formula:
# S = math.sqrt(p * (p - a) * (p - b) * (p - c))

# where p = a + b + c / 2 is a half-perimeter of the triangle. On the
# input, the program has integers, and the output should be a real
# number corresponding to the area of the triangle.

# Do NOT round the result.
import math

a, b, c = int(input()), int(input()), int(input())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)