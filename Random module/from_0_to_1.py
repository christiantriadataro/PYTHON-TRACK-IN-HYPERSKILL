# The function used to set a starting point of the random search
# algorithm is called random.seed() and takes a single integer
# number. Write a program that takes an integer number n, sets n
# as a seed and then prints a pseudo-random number from 0 to 1

# The variable n is already defined.

import random

# work with this variable
n = int(input())
random.seed(n)
print(random.uniform(0, 1))