# Let's say there's a script add_four_numbers.py. It takes exactly four arguments, all of
# which are numerical. It may be run from the command line like this:

# python3 add_four_numbers.py 25 17 808 9

# Inside the program itself, the arguments are firstly read from the command line into the
# list args:

# scripts 'add_four_numbers.py'

# import sys

# args = sys.argv

# You don't see the import part of the script, but you have access to args, see below
# (please don't import the module yourself, it is important for the tests).

# Your tasks is to access the arguments and print the result of the addition. Please make it
# an integer
import sys

args = ["add_four_numbers.py", "25", "17", "808", "9"]


# print(sum(map(lambda x: int(x), num)))

print(sum(map(int, args[1:])))