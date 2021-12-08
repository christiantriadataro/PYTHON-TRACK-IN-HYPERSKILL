# Define a function that takes a number n and returns a function
# that, in its turn, takes x as an argument and returns the remainder
# of the division of x by n.

# You don't have to handle input or print anything, just implement
# the function.
def create_function(n):
    return lambda x: x % n

func = create_function(2)
print(func(10))