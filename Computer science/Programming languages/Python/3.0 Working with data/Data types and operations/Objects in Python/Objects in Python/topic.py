# Theory: Objects in Python

# Knowing how different types of objects work in Python will help
# you understand some of the following topics more deeply, as
# well as the structure of the language in general. 

# Reference to an object
# In Python, all values are stored in objects. You can think that an
# object is like a box that contains information about some value 
# and you assign a value to a variable, e.g. string = "hello", Python
# creates a new object, places this values (the string "hello" in
# our case) inside the new object and then creates a reference
# from the variable name string to the object.

# Then, if we assign one variable to another, e.g. new_string = 
# string, Python will create a reference from the new variable
# new_string to the same object.

# You can ues the id function to see that both variables refer to
# the same object
string = 'hello'
new_string = string
print(id(string))
print(id(new_string))

# As a result, you can access the object using any of the two
# variable names. You can also assign a new value to one of these
# variables and this will not affect the other one.

string = "hello"
new_string = string
string = "world"

print(string, id(string))              # world 2383455759472
print(new_string, id(new_string))      # hello 2383455483056

# Note that the identity has changed along with the value.

# However, the situation is a bit more complex when we deal with
# mutable objects, e.g. some of the containers.

# Mutable objects & references
# Let's take a list as an example. The thing is, a list doesn't store
# its values inside itself. Instead, it stores references to objects
# that store values. For example, when you write lst = [2, 3, 
# 9], Python creates the following structure:

# Now, if we assign our list to a new variable and then try to alter
# the first object, this will also affect the new list:
lst = [2, 3, 9]
new_lst = lst

print(lst, id(lst))             # [2, 3, 9] 2192427479936
print(new_lst, id(new_lst))     # [2, 3, 9] 2192427479936

# we change an element of the first list
lst[2] = 0
print(lst, id(lst))            # [2, 3, 0] 2449967248256   

# but the new is also modified
print(new_lst, id(new_lst))    # [2, 3, 0] 2449967248256

# This is so because both lists refer tot he same object: when it is
# modified, all variables continue to refer to this very object. In
# the next topic, you will learn how to alter a list without changing
# its copies.

# Summary.
# - Variables in Python do not store values themselves, they
#   store references to objects that store values.
# - When we assign one variable to another, they refer to the 
#   same object.
# - After odifying mutable objects, other variables referring
#   to it will also change.


