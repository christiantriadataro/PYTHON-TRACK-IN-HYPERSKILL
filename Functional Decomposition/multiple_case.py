# In her program, Kate wants to use the following function:

# The template for this function is defined below. Your task is to
# create additional functions (one for each case) and complete
# f(x) by calling the additional functions and returning their
# values. The additional functions are named f1(x), f2(x), and
# f3(x).

# You need to return the values returned by additional functions.
# You do NOT need to work with the input or print anything.

# Sample Input 1:
# 1

# Sample Output 1:
# 0.0

# Sample Input 2:
# 0.1

# Sample Output 2:
# 99.99999999999999

def f1(x):
    return (x * x) + 1

def f2(x):
    return  1 / (x * x)

def f3(x):
    return  (x * x) - 1

def f(x):
    if x <= 0:
        return f1(x)
    elif 0 < x < 1:
        return f2(x)
    else:
        return f3(x)

