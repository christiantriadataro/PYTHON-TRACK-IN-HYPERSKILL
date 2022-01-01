# Theory: Command line arguments

# Using these command line is sometimes very useful in the
# programmer's work. And Python scripts can be run from
# the command line just its regular command, e.g.
# "cd" or "mkdir". This means we can write a module that
# can take data as input, do something with it, and return
# the result. In this topic, we'll see how we can make that
# happen.

# 1. Running from the command line
# As an example, let's take a module that multiplies two
# numbers and nicely prints the result, and run it from the
# shell:

# python multiply_two_numbers.py 5 9

# In the line above, python is kind of command that
# indicates that the Python interpreter should be used for
# the following script. In some cases, the system may
# already know how to run .py files but we will not go into
# details here and, for the sake of consistency, will use the
# python command throughout this topics.

# Then, separated by a whitespace, follows the script name.
# Note that if the script is in another directory than the one
# you are working from, you should specify the path to the
# file. It may be an absolute path:

# python C:\python_scripts\add_two_numbers.py 11 44

# Or it can be a relative path, for example to run a script
# from the parent directory:

# python ..\add_two_numbers.py 11 44

# Finally, if the scripts takes any arguments, they are written
# separated by whitespaces after the script name.

# And that's it! However, the next question is - how can we
# get access to the specified arguments from our Python
# script?

# 2. System module
# In order to do so, we can make use of the sys module. It
# provides access to functions and variables that allow for
# working with the underlying Python interpreter,
# irrespective of the operating system. We won't go into
# details talking about its features, but rather focus on the
# one that is the most important right now, namely,
# sys.argv. It performs the very operation we need: collects
# the arguments passed to the python script.

# By calling sys.argv, we get arguments specified by the
# user as a list of strings. Indexing, as always in Python,
# starts form 0 but the first argument, sys.argv[0] is the
# name of our Python sript as it was invoked - either the
# name itself or including the path to the file. The items
# that follow are argument that can also be accessed by
# their index. Take note that they are strings, and if we need
# a numerical value, we should perform type conversion.

# Let's write a simple program multiply_two_numbers.py

import sys  # first, we import the module

args = sys.argv # we get the list of argument
first_num = float(args[1])  # convert argument to float
second_num = float(args[2])

product = first_num * second_num

print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))


# 3. Checking the input
# It is also worth mentioning that if we expect to get a
# specific number of arguments (i.e. almost always), it is a
# good idea to check the lenght of sys.argv in the
# program. Let's chech that in our script
# multiply_two_numbers.py:

import sys

args = sys.argv

if len(args) != 3:
    print("The script should be called with two arguments, the first and the second number to be multiplied")

else:
    first_num = float(args[1])
    second_num = float(args[2])

    product = first_num * second_num

    print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))