# Theory: Algorithms in Python

# As you know, algorithms are language-independent,
# meaning that the same algorithm can be implemented in
# different programming languages. Since your goal is to
# learn Python, we will consider how to implement basic
# algorithms using this language and its features.

# 1. Implementing algorithms in Python
# Python has many libraries that provide ready-to-use
# functions for various problems. Algorithms are not an
# exception. You can find most of the widely-used
# algorithms in the Python standard library or in the
# external packages. Usually, an algorithm is a standalone
# function that may either be implemented directly in
# Python or represent a wrapper that calls a function
# written in another programming language.


# Python standard library contains such functions as
# sorted, min, max, which represent algorithms for
# sorting and finding the minimum/maximum values in a
# collection of elements. There are also modules that unite
# the algorithms of one subject area, for example:

# - math is a module with mathematical algorithms.
#   For example, math.sqrt is an algorithm that
#   calculates the square root of a number.
# - collections is a module that extends and improves
#   the functionality of standard collections such as
#   list or tuple. An example is collections.deque,
#   an efficient implementation of a double-ended
#   queue data structure.

# Although most standard algorithms are already present in
# libraries and packages, we will learn to implement some
# of them ourselves. This will help you practice your Python
# skills and understand how these algorithms work under
# the hood.

# 2. A particular example
# Let's implement a simple algorithm in Python and
# consider some typical problems that arise during the
# process. Below is an algorithm that finds the index of the
# maximum element in a list of numbers:

def indexof_max(numbers):
    index = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[index]:
            index = i

    return index

The