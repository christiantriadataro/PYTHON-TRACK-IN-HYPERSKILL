# Write a program that reads an integer that represents the radius
# of a given circle and calculates its area. To calculate the area of
# a circle, use the following formula: S = πr^2.

# Sample Input 1:
# 5 

# Sample Output 1:
# 78.54
from math import pi
print(round(int(input()) ** 2 * pi, 2))