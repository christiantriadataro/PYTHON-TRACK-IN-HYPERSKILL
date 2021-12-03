# Ask the user about parameters of a rectangular parallelepiped
# (3 integers representing the length, width, and height) and print
# the sum of edge lengths, its total surface area, and the volume.

# Sum of lengths of all edges:
# s=4(a+b+c)

# Surface area:
# S=2(ab+bc+ac)

# Volume:
# V=abc

# put your python code here

# user input
(a, b, c) = (int(input()), int(input()), int(input()))

# sum of lengths of all edges:
print(4 * (a + b + c))

# Surface area
print(2 * ((a * b) + (b * c) + (a * c)))

# Volume:
print(a * b * c)