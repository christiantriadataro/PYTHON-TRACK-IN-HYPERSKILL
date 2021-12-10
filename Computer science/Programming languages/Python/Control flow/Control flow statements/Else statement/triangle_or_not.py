# Read three angles, which are given on separate lines, from the
# input and print in the following format whether they form a
# triangle: "The triangle is valid!" or "The triangle is not valid!"

a = int(input())
b = int(input())
c = int(input())

print("The triangle is valid!" if a + b + c == 180 else "The triangle is not valid!")