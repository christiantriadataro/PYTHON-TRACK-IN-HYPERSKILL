# Write a program that reads a value representing an angle (in
# radians), and prints the difference between its sine and cosine.
from math import sin, cos
angle = float(input())
print(sin(angle) - cos(angle))