# Voldemort
# The function to set a starting point of the random search
# algorithm is called random.seed() and takes a single integer
# number. Write a program that takes a single number n, sets a
# seed to n and then prints a pseudo-randomly chosen letter from
# the string "Voldemort"

# The variable n is already defined.

import random

# work with this variable
n = int(input())
random.seed(n)
print(random.choice("Voldemort"))