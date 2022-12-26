# Theory: How to read the documentation

# Most programmers are used to googling an answer when they
# don't know how to do something or ask a question on a forum
# like Stack Overflow. Sometimes, on forums, you can come
# across such as abbreviation as RTFM. It has slightly different
# meanings, but we will focus on "Read the following manual". It
# speaks for itself, doesn't it? If you see such an answer, it means
# that the question could have been answered by reading the
# corresponding manual or documentation.

# Reading the documentation is, an essential skill for a
# programmer. To understand why it is so, let's consider several
# points:

# 1. The official documentation is the most truthful and
#    complete source.
# 2. It contains up-to-date information for the latest versions.
# 3. The same code can be written in different ways, but the
#    documentation contains the best practices.

# These reasons should already be enough for you to open up to
# the documentation and hope that it will open up to you!

# 1. Main source of documentation
# Of course, Python has it own complete and up-to-date official
# documentation! Let's take a look at the site header:

# By default, we see the latest version of Python, but you can find
# documentation for older versions as well. For convenience, you
# can also select another available language or use the Quick
# Search field to find the information you need.

# Below you can see parts of the documentation. Let's take a
# quick look at some that are important for us:

# - Tutorial is the one to start with when discovering the
#   Python world.
# - Library Reference is a more detailed information on how
#   Python works and what features it has. In this section, you
#   will spend most of your time as a Python programmer.
# - Python Setup and Usage contains tips on how to install
#   and configure Python environment on different platforms.
# - Python HOWTOs are various guides on specific topics.

# You can also download the documentation in a format
# convenient for you on the download page.

# The docs contain a lot of information, but don't be afraid, you
# don't have to read everything at once. The main thing is to learn
# to find answers to your questions.

# 2. Official Python documentation
# The best way to learn something is to try it yourself, so let's
# refer to the documentation of the math module as an example.
# We suggest that you open it and take a look at it yourself first.
# Below we describe what you can find there.

# First of all, documentation tells us what a particular module is
# used for:

# This module provides access to the mathematical functions defined by the C standard.

# And also about various restrictions:

# These function cannot be used with complex numbers...

# For each function from this module, you can find a description of
# what it does and what value you get as a result. Consider the
# math.fabs(x) function:

# math.fabs(x)
#   Return the absolute value of x.

# Moreover, the documentation will
# indicate which errors we may encounter when calling the
# function with invalid arguments.

# Also, there are often some sections that are specific to the
# module itself. In math, for example, "Constants" is such a
# section and it contains a list of all constant values defined in the
# module, as the one below:

# math.pi
#   The mathematical constant = 3.141592... to available precision.

# Finally, in the See also section at the very end you can find
# alternatives or additional information:

# See also:

# Module cmath
#   Complex number versions of many of these functions.

# If you need to quickly find information about a specific
# module, function, and so on, use the page search in the
# browser (Ctrl + F)

# 3. Documentation of third-party libraries
# In addition to the standard libraries that come with the default
# Python installation, there are also third-party libraries. They are
# developed by third-party programmers (hence the name) and
# serve a specific purpose. Therefore, another source of
# information that you will often come across is the
# documentation of third-party libraries.

# Let's consider the documentation for one of such libraries-
# Colorama, which 'makes ANSI escape character sequences (for
# producing colored terminal text and cursor positioning) work
# under MS Windows". As we can see, just as the official
# documentation, it starts with a short description of what the
# library is used for.

# Also, you will find information on how to install a third-party
# library:
# Installation:
# pip install colorama
# or
# conda install -c anaconda colorama

# and examples of what you get as a result (follow the link and
# see for yourself).

# Then, the documentation will always contain examples of how
# to use the library in various cases illustrating its capabilities. We
# will not show it here, but you can see it yourself in the Colorama
# documentation.

# In order to get used to the documentation, you can familiarize
# yourself with its structure using examples of some other third-
# party libraries: Matplotlib, SymPy, PrettyTable, BeautifulSoup.
# Not all of them may be clear to you yet, but it's okay! In
# programming, you often have to face new things. However, all of
# them usually consist of the same parts: a short summary of
# what the library is used for, installation guidelines, and a list of
# functions with descriptions and usage examples.

#       Note that documentation of third-party libraries is not
#       always full and up-to-date. It is written by the developers
#       themselves, so keep that in mind.

# 4. Some help()
# Often you need to get information while writing code, and
# Python has a built-in help system for such cases, allowing you
# to get a quick reference about an object. To do this, you need to
# call the help() function and pass an object as an argument. For
# example, it can be a function

help(len)

# Help on built-in function len in module builtins:
#
# len(obj, /)
#   Return the number of items in a container.

# Note that the function in such a case is written without
# parentheses.

# Now, let's try to get brief documentation about the sqrt()
# function from the math module:

# something goes wrong:
help(math.sqrt)  # NameError: name 'math' is not defined'

# The thing is, you should either import the module first:
import math

help(math.sqrt)

# sqrt(x, /)
#   Return the square root of x.

# or pass the name of the object in brackets like:
# help('math.sqrt')

# All in all, it is a convenient method to get short info about the
# usage of an object without searching for its documentation on
# the Internet.


# 5. Conclusion
# Remember that just reading the documentation from the
# beginning





















