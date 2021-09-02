# Write a function called multiply that takes a changeable
# number of arguments and returns their product.

# Assume that only integer numbers are to be passed into the 
# function.

# Given only one integer number, multiply it by 1. Thus, the
# product will be equal to this integer.

# You are not supposed to call the function, simply implement it.

def multiply(*args):
    product = 1
    for n in args:
        product *= n
    return product