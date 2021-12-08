# Theory: Command line arguments
# Using the command line is sometimes very useful in the
# programmer's work. And Python scripts can be run from
# the command line just like its regular commands, e.g.
# "cd" or "mkdir". This means we can write a module that
# can take data as input, do something with it, and return
# the result. In this topic, we'll see how we can make that
# happen.

# 1. Running from the command line
# As an example, let's take a module that multiplies two
# numbers and nicely prints the result, and run it from the
# shell:

# python multiply_two_numbers.py 5 9

# In the line above, python is kind of a command that
# indicates that the Python interpreter should be used for
# the following script. In some cases, the system may
# already know how to run .py files but we will not go into
# details here and, for the sake of consistency, will use the
# python command throughout this topic.

# Then, seperated by a whitespace, follows the script name.
# Note that if the script is in another directory than the one
# you are working from, you should specify the path to the
# file. It may be an absolute path:

# python C:/python_script/add_two_numbers.py 11 44

# Or it can be a relative path, for example to run a script
# from the parent directory:

# python ../add_two_numbers.py 11 44

# Finally, if the script takes any argumenets, they are written
# separated by whitespaces after the script name.

# And that's it! However, the next question is - how can we
# get access to the specified arguments from our Python
# script?

# 2. System module
# In order to do so, we can make use of the sys module. It
# provides access to functions adn variables that allow for
# working with the underlying Python interpreter,
# irrespective of the operating system. We won't go into
# details talking about its features, but rather focus on the
# one that is the most important right now, namely,
# sys.argv. It performs the very operation we need: collects
# the arguments passed to the python script.

# By calling sys.argv, we get arguments specified by the
# user as a list of strings. Indexing, as always in Python,
# starts from 0 but the first argument, sys.argv[0] is the
# name of our Python script as it was invoked - either the
# name itself or including the path to the file. The items
# that follow are arguments that can also be accessed by
# their index. Take note that they are strings, and if we need
# a numerical value, we should perform type conversion.

# Le's write a simple program multiply_two_numbers.py:

import sys # first, we import the module

args = sys.argv # we get the list of arguments
first_num = float(args[1])
second_num = float(args[2])

product = first_num * second_num

print("The product of " + args[1] + " times " + args[2] + " equals", product)

# 4. Within the IDE
# Let's take a look at PyCharm's capabilities in comparison
# to the command line. Instead of manually writing the
# script name and arguments each time, you can set them
# in the configuration. For this in the Run area select Edit
# Configurations to open the Run/Debug Configurations
# dialog.
