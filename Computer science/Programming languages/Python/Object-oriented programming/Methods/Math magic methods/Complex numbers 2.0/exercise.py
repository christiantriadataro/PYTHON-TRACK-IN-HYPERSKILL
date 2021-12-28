# In this topic, we've defined the class ComplexNumber and
# several magic methods for this class. However, it makes
# sense to define a couple of other methods so that we
# can use this class to its full potential.

# We need methods for subtraction and division.

# Subtraction

# If we have 2 complex numbers x = a + bi and y = c + di,
# then x - y equal (a - c) + (b - d)i.

# Division
# For division, we need to calculate the reciprocal of a
# complex number. If x = a + bi, then 1/x = a / (a^2 + b^2) - b / (a^2 + b^2) i.
# x/y can then be represented as x * 1/y.

class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary = self.im_part + other.im_part
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        real = self.real_part - other.real_part
        imaginary = self.im_part - other.im_part
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real_part * other.real_part - self.im_part * other.im_part
        imaginary = self.real_part * other.real_part + self.im_part * other.im_part
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        div = other.real_part ** 2 + other.im_part ** 2
        other.real_part /= div
        other.im_part /= -div
        return self.__mul__(other)

    def __eq__(self, other):
        return self.real_part == other.real_part and self.im_part == other.im_part

    def __str__(self):
        return f"{self.real_part} {'-' if self.im_part < 0 else '+'} {abs(self.im_part)}i"


z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(4,  5)
z3 = z1 / z2
print(z3)
print(complex(2,3) / complex(4,5))

