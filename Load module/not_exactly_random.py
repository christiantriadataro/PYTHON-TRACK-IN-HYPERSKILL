# In the random module, random elements are generated using a 
# complex algorithm whose starting point is some number called
# a seed. A seed can be set manually using the seed() function -
# then, all numerical sequences generated in our program after
# taht will be the same. If we don't specify the seed manually, the
# randomly generated numbers will depend on the current system
# time (default value for the seed). Therefore, the results provided
# by functions from the random module are not exactly random,
# but rather pseudo-random, and we can make sure they remain
# the same regardless of how many times we run our program.

# Write a program that takes an integer number n, sets a random
# number generator (the seed) to that number, and then prints a
# pseudo-random number from -100 to 100.

# Use seed and randint functions. The former takes one argument
# and the latter takes two numbers that represent the range.

# The variable n is already defined.


# place `import` statement at top of the program
from random import seed
from random import randint

# don't modify this code or variable `n` may not be available
n = int(input())

# put your code here
seed(n)
print(randint(-100, 100))