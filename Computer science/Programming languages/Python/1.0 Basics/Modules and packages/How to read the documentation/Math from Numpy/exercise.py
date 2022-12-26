# Math from Numpy

# Mathematics is often useful in programming. Let's solve one
# math problem using the math library.

# Your task is to implement the calculate_cosine() function. The
# function parameter is an angle in degrees. The function should
# calculate the cosine of the given angle using the corresponding
# math.cos() function from the math library, then round the
# result to two decimal places using the round(..., 2) function,
# and print it.

# But it's not so simple. Read the documentation for this function
# and pay attention to what unit of measure the angle must be in.

# You can find the additional function you need on the same page
# in the Angular conversion section.

# Do not forget to import the necessary library. Don't call the
# function, just implement it.

# import the required library
import math

def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    print(round(math.cos(math.radians(angle_in_degrees)), 2))
