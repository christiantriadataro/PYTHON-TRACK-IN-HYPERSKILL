# Numeric Types
# A young programmer Mark wants to calculate the following
# expression:

# 1. First, get the remainder of dividing a by b.
# 2. Raise b to the power of a.
# 3. Subtract the two resulting numbers.
# 4. Get the absolute value of the subtraction.

# But it seems that he made several errors in the code. In the
# Numeric Types section of the documentation, you can find a
# table describing the operations Mark wanted to perform.

# You don't need to call the some_calculate() function or read
# from the input. Just implement the function and print the result
# after corrections.

def some_calculate(a, b):
    print(abs((a % b) - pow(b, a)))

some_calculate(2, 3)