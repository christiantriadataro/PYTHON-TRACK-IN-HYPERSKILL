# We've written a simple program for calculating the roots of a
# quadratic equation:

def find_roots(a, b, c):
    # the equation is ax^2 + bx + c = 0\
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print("No real roots!")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b + discriminant ** 0.5) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)

# After that, we decided to decompose this code and create
# additional functions:

def calculate_discriminant(a, b, c):
    return b * b - 4 * a * c

def calculate_roots(a, b, d):
    x1  = (-b + d ** 0.5) / (2 * a)
    x2 =  (-b - d ** 0.5) / (2 * a)
    if x1 == x2:
        print("x =", x1)
    else:
        print("x1 =", x1)
        print("x2 =", x2)

# How should the final function look? Make sure that the function
# produces the correct output and is properly decomposed(no
# unnecessary actions are performed).

