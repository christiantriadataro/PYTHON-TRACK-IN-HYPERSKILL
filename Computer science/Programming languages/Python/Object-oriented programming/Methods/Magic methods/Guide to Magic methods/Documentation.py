# A Guide to Python's Magic Methods
# Rafe Kettler
# September 4, 2015

# 1. Introduction
# This guide is the culmination of a few months' worth of blog posts. The subject is magic
# methods.
#   What are magic methods? They're everything in object-oriented Python. They're special
# methods that you can define to add "magic" to your classes. They're always surrounded by
# double underscores (e.g. __init__ or __lt__). They're also not as well documented as they
# need to be. All of the magic methods for Python appear in the same section in the Python
# docs, but they're scattered about and only loosely organized. There's handly all detailed in the
# language reference, along with boring syntax descriptions, etc).

#   So, to fix what I preceived as a flaw in Python's documentation. I set out to provide some
# more plain-English, example-driven documentation for Python's magic methods. I started out
# with weekly blog posts, and now that I've finished with those, I've put together this guide.

#   I hope you enjoy it. Use it as a tutorial, a refresher, or a reference; it's just intended to be
# a user-friendly guide to Python's magic methods.

# 2. Construction and Initialization
# Everyone knows the most basic method, __init__. It's the way that we can define the
# initialization behavior of an object. However, when I call x = SomeClass(), __init__ is not
# the first thing to get called. Actually, it's a method called __new__, which actually creates the
# instance, then passes any arguments at creation on to the initializer. At the other end of the
# object's lifespan, there's __del__. Let's take a closer look at these 3 magic methods:

# __new__(cls, [...) __new__ is the first method to get called in an object's instantiation.
#   It takes the class, then any other arguments that it will pass along to __init__. __new__
#   is used fairly rarely, but it does have it purposes, particularly when subclassing
#   an immutable type like a tuple or a string. I don't want to go in to too much detail on
#   __new__ because it's not too useful, but it is covered in great detail in the Python docs.

# __init__(self, [...) The initializer for the class. It gets passed whatever the primary constructor
#   was called with (so, for example, if we called x = SomeClass(10, 'foo'), __init__
#   would get 10 and 'foo' as arguments. __init__ is almost universally
#   used in Python class definitions.

# __def__(self) If __new__ and __init__ formed the constructor of the object, __del__ is the
#   destructor. It doesn't implement behavior for the statement del x (so that code would
#   not translate to x.__del__()). Rather, it defines behavior for when an object is garbage
#   collected. It can be quite useful for objects that might require extra cleanup upon deletion,
#   like sockets or file objects. Be careful, however, as there is no guarantee that __del__ will
#   be executed if the object is still alive when the interpreter exits, so __del__ can't serve
#   as a replacement for good coding practices (like always closing a connection when you're
#   done with it). In fact, __del__ should almost never be used because of the precarious
#   circumstances under which it is called; use it with caution!

# Putting it all together, here's an example of __init__ and __del__ in action:

from os.path import join

class FileObject:
    '''Wrapper for file objects to make sure the file gets closed
    on deletion.'''

    def __init__(self, filepath='~', filename='sample.txt'):
        # open a file filename in filepath in read and write mode
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file

# 3. Making Operators Work on Custom Classes
# One of the biggest advantages of using Python's magic methods is that they provide a simple way
# to make objects behave like built-in types. That means you can avoid ugly, counter-intuitive,
# and nonstandard ways of performing basic operations. In some languages, it's common to do
# something like this:

# if instance.equals(other_instance):
    # do something

# You could certainly do this in Python, too. but this adds confusion and is unnecessarily verbose.
# Different libraries might use different names for the same operations, making the client do way
# more work than necessary. With the power of magic methods. however, we can define one
# method (__eq__, in this case), and say what we mean instead:

# if instance == other_instance:
    # do something

# That's part of the power of magic methods. The vast majority of them allow us to define
# meaning for operators so that we can use them on our own classes just like they were built in
# types.

# 3.1 Comparison magic methods
# Python has a whole slew of magic methods designed to implement intuitive comparisons between
# objects using operators, not awkward method calls. They also provide a way to override the
# default Python behavior for comparisons of objects (by reference). Here's the list of those
# methods and what they do:

# __cmp__(self, other): __cmp__ is the most basic of the comparison magic methods. IT
#   actually implements behavior for all of the comparison operators (¡, ==, !=, etc), but
#   it might not do it the way you want (for example, if whether one instance was equal to
#   another were determined by one criterion and whether an instance is greater than
#   another were determined by something else). __cmp__ should return a negative integer if
#   self < other, zero if self == other, and positive if self > other. It's usually best
#   to define each comparison you need rather than define them all at once, but __cmp__
#   can be a good way to save repetition and improve clarity when you need all comparisons
#   implemented with similar criteria.

#   __eq__(self, other) Defines behavior for the equality operator, ==.
#   __ne__(self, other) Defines behavior for the inequality operator, !=.
#   __lt__(self, other) Defines behavior for the less-than operator, <.
#   __gt__(self, other) Defines behavior for the greater-than operator, >.
#   __le__(self, other) Defines behavior for the less-than-or-equal-to operator, <=.
#   __ge__(self, other) Defines behavior for the greater-than-or-equal-to operator, >=.

#   For an example, consider a class to model a word. We might want to compare words
# lexicographically (by the alphabet), which is the default comparison behavior for strings, but
# we also might want to do it based on the some other criterion, like length or number of syllables.
# In this example, we'll compare by length. Here's an implementation:

class Word(str):
    '''Class for words, defining comparison based on word length.'''

    def __new__(cls, word):
        # Note that we have to use __new__. This is because str is an
        # immutable type, so we have to initialize it early (at creation)
        if '' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')]
            # Word is now all chars before first space
        return str.__new__(cls, word)

    def __gt__(self,other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) > len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

#   Now, we can create two Words (by using Word('foo') and Word('bar')) and compare them
# based on length. Note, however, that we didn't define __eq__ and __ne__. This is because
# this would lead to some weird behavior (notably that Word('foo') == Word('bar') would
# evaluate to true). It wouldn't make sense to test for equality based on length, so we fall back
# on str's implementation of equality.
#   Now would be a good time to note that you don't have to define every comparison magic
# method to get rich comparisons. The standard library has kindly provided us with a class
# decorator in the module functools that will define all rich comparison methods if you only
# define __eq__ and one other (e.g. __gt__, __lt__, etc) This feature is only available in Python
# 2.7, but when you get a chance it saves a great deal of time and effort. You can use it by placing
# @total_ordering above your class definition.

# 3.2 Numeric Magic methods
# Just like you can create ways for instances of your class to be compared with comparison
# operators, you can define behavior for numeric operators. Buckle your seat belts, folks, there's
# a lot of these. For organization's sake, I've split the numeric magic methods into 5 categories:
# unary operators, normal arithmetic operators, reflected arithmetic operators (more on this
# later), augmented assignment, and type conversions.

# 3.2.1 Unary operators and functions
# Unary operators and functions only have one operand, e.g. negation, absolute value, etc.

# __pos__(self) Implements behavior for unary positive (e.g. +some_object)
# __neg__(self) Implements behavior for negation (e.g. -some_object)
# __abs__(self) Implements behavior for the built in abs() function.
# __invert__(self) Implements behavior for inversion using the ~ operator.
# __round__(self, n) Implements behavior for the built in round() function. n is the number
#   of decimal places to round to.
# __floor__(self): Implements behavior for math.floor(), i.e., rounding down to the nearest
#   integer.
# __ceil__(self): Implements behavior for math.ceil(), i.e., rounding up to the nearest
#   integer.
# __trunc__(self): Implements behavior for math.trunc(), i.e., truncating to an integral.

# 3.3 Normal arithmetic operators
# Now, we cover the typical binary operators (and a function or two): +, -, * and the like. These
# are, for the most part, pretty self-explanatory.

# __add__(self, other) Implements addition.
# __sub__(self, other) Implements subtraction.
# __mul__(self, other) Implements multiplication.
# __floordiv__(self, other) Implements integer division using the // operator.
# __div__(self, other) Implements division using the / operator
# __truediv__(self, other) Implements true division. Note that this only works when from
#   __future__ import division is in effect.
# __mod__(self, other) Implements modulo using the % operator.
# __divmod__(self, other) Implements behavior for long division using the divmod() built tin
#   function.
# __pow__ Implements behavior for exponents using the ** operator.

# __lshift__(self, other) Implements left bitwise shift using the << operator.
# __rshift__(self, other) Implements right bitwise shift using the >> operator.
# __and__(self, other) Implements bitwise and using the & operator.
# __or__(self, other) Implements bitwise or using the ^ operator.

# 3.3.1 Reflected arithmetic operators.
# You know how I said I would get to reflected arithmetic in a bit? Some of you might think it's
# some big, scary, foreign concept. It's actually quite simple. Here's an example:
# some_object + other

# That was "normal" addition. The reflected equivalent is the same thing, except with the
# operands switched around:
# other + some_object

# So, all of these magic methods do the same thing as their normal equivalents, except the
# perform the operation with other as the first operand and self as the second, rather than the
# other way around. In most cases, the result of a reflected operation is the same as its normal
# equivalent, so you may just end up defining __radd__ as calling __add__ and so on. Note