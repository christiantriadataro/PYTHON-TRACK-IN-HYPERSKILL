# Imagine, you have two variables and you don't know what they
# contain but need to check if they refer to the same object or not.
# How would do that ?

# Write a function check(obj1, obj2) that will take two objects
# and print True if they refer to the same object and False
# otherwise.

def check(obj1, obj2):
    print(True if obj1 is obj2 else False)