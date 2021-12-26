# Theory: Math magic methods
# If you want to improve and upgrade your classes, chances
# are that what you need can be done with magic methods.
# Dunders in Python provide a wide range of functionalities,
# from type conversion to attribute managing. In this topic,
# we'll focus on "mathematical" magic methods: the ones
# that deal with arithmetics and comparisons.

# 1. Arithmetic operations
# There is a group of magic methods representing common
# arithmetic operations:
# - __add__(): addition (+)
# - __sub__(): subtraction (-)
# - __mul__(): multiplication (*)
# - __truediv__(): division (/)
# - __pow__(): exponents: (**)

# This list is not exhaustive, there are many other methods,
# but these are the most common ones.

# However, the question is when would we need to use
# them? Let's consider an example.

class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

# This is a class that represents complex number. A
# complex number is a number that can be expressed as
# a + bi where a and b are real numbers and i is the
# imaginary number: the solution of the equation x^2 = -1.
# So a is the real part of the complex number and b is the
# imaginary one. Just like ordinary numbers, we can add
# two complex numbers, multiply them, do subtraction and
# division and many other standard operations. Let's create
# two complex numbers and try to add and multiply them:

z1 = ComplexNumber(1, 1)
z2 = ComplexNumber(-1, 2)

# z3 = z1 + z2
# TypeError: unsupported operand type(s) for +: 'ComplexNumber' and 'ComplexNumber'
z4 = z1 * z2
# TypeError: unsupported operand type(s) for +: 'ComplexNumber' and 'ComplexNumber'

# As you can see, we cannot simply add two complex
# numbers using the standard operators in Python. We
# could, of course, define custom methods like add or
# multiply and call them when we need to do math with
# complex numbers, but it wouldn't be too convenient. A
# more elegant solution to this problem is to define magic
# methods __add__ and __mul__ in our ComplexNumber
# class and then simply use standard operators with our
# complex numbers. Here's how it would look:

class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        """Addition of complex numbers."""
        real = self.real_part + other.real_part
        imaginary = self.im_part + other.im_part
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        """Multiplication of complex numbers."""
        real = self.real_part * other.real_part - self.im_part * other.im_part
        imaginary = self.real_part * other.im_part + other.real_part * self.im_part
        return ComplexNumber(real, imaginary)


# First, let's go over the details of the methods. Since both
# addition and multiplication operators are binary, the
# methods take two arguments, self and other. other is
# a name typically used to denote another object of the
# same class. These parameters represent the operands of
# these operations and in this case, self is the left
# operand and other is the right one. If the operator was
# unary, the method would only take self as a parameter.

# Both methods also calculate the real and the imaginary
# part of a new complex number and then return a new
# ComplexNumber object as their results.

# If we try to calculate the sum and the product of our
# complex numbers now, we won't get any errors:
z3 = z1 + z2
print(z3.real_part, z3.im_part)

z4 = z1 * z2
print(z4)