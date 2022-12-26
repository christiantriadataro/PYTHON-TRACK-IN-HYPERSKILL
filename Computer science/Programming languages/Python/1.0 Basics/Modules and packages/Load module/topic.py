# Theory: Load module

# There are different ways to interact with code. In this topic, we'll
# learn whay they are and in what cases which option is the most
# convenient. However, most importantly, we'll find out how to
# save our code into a file for further use or correction. As you
# probably have already guessed. that applies to any code, which
# means you can also use someone else's code and this part
# is a pretty big deal you'll quickly appreciate as a developer.

# 1. Module basics
# While working on simple examples, you probably type your code
# directly into the interpreter. But every time you quit from the
# interpreter and start it again, you lose all the definitions you
# made before. So as you start writing larger programs, it makes
# sense to prepare your code in advance using a text editor and
# then run it with the interpreter. A file containing a list of
# operations that will be read and interpreted further on is called
# script.

# You also may want to write some functions and then use them
# in other programs or even reuse code someone else wrote
# before. One way is just to copy the code into your program, but
# it soon leads to code that is badly structured and hard to read.
# Luckily, there is another way in Python to organize and reuse
# code called modules.

# The module is simply a file that contains Python statements and
# definitions. It usually has a .py extension. What really makes the
# module system powerful is the ability to load or import one
# module from another.

# 2. Module loading
# To load a module, just use an import statement. In its basic
# form, it has the following syntax: import module.

import super_module

super_module.super_function()   # calling a function

print(super_module.super_variable)  # accessing a variable

# super_module is the name of the module you want to import.
# For example, a file called super_module.py has a nmae
# super_module. In order to be available for import,
# super_module.py should be located in the same directory as
# the file you are trying to import it from. At first, Python
# importing system looks for a module in the current directory,
# then it checks the built-in modules, and if nothing is found an
# error will be raised. After importing, the module becomes
# avaiable under its name and you can access functions and
# variables defined in it using the dot notation.

# It's also common to only import required functions or variables
# from a module but not the module itself. You can do this by
# using a from form of import statement.

from super_module import super_function

super_function()   # super_function is now available directly at the current module

super_module.super_function()  # note, that in this case name super_module is not imported,
                               # so this line leads to an error

# A good practice is to load a single module in a single line and
# put all your imports at the top of the file because it increases
# readability.

import module1
import module2
import module3

# the rest of module code goes here

# A special form of import statement allows you to load all the
# names defined in a module. It is called wildcard import and has
# the syntax from module import *. You should generally avoid
# this in your code. It can cause unexpected behavior because you
# don't know what names exactly are imported into the current
# namespace. Besides, these names may shadow some of the 
# existing ones without your knowledge. It's better to make it
# explicit and specify what you're importing.

# In case you have to use several import statements, pay
# attention to their order:
# 1. standard library imports
# 2. third party dependency imports
# 3. local application imports

# Having your imports grouped, you may put a blank line betweeen
# import sections. Also, some guidelines, including ours,
# recommend sorting imports alphabetically.

# 3. Built-in modules
# Python comes with a great standard library. It contains a lot of
# built-in moduiles that provide useful functions and data
# structures. Anotehr advantage is that the standard library is
# available on every system that has Python installed. Here you
# can find an official library reference.

# Python has a math module that provides access to
# mathematical functions
import math

print(math.factorial(5))  # prints the value of 5!

print(math.log(10))  # prints the natural logarithm of 10

print(math.pi)  # math also contains several constants
print(math.e)

# The string module contains common string operations and
# constants.
from string import digits

print(digits)   # prints all the digit symbols

# The random module provides function that let you make a 
# random choice.

from random import choice
print(choice(['red', 'green', 'yellow']))  # print a random item from the list

# 4. Summary
# Thus, in this topic, we've learned what scripts and modules are,
# why they're useful, and how to import modules (or particular
# things from them). We've also discussed external modules and
# those that come with a standard Python library. This basic skill
# will definitely give you a lot of opportunities in the future, so
# don't be shy to try module loading on your own!
