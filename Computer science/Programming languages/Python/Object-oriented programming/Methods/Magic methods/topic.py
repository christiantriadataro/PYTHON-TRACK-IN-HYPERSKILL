# Theory: Magic methods

# There are different ways to enrich the functionality of your classes
# in Python. One of them is creating custom methods which you've
# already learned about. Another way, the one that we'll cover in this
# topic, is using "magic" methods.

# 1. What are "magic" methods?
# Magic methods are special methods that make using your
# objects much easier. They are recognizable in the code of the
# class definitions because they are enclosed in double
# underscores: __init__, for example, is one of those "magic"
# methods in Python. Since they are characterized by double
# underscores they are often called dunders.

# Dunders are not meant to be invoked directly by you or the user
# of your class, it happens internally on a certain action. For
# example, we do not explicitly call the __init__ method when
# we create a new object of the class, but instead, this method is
# invoked internally. All we need to do is to define the method
# inside the class in a way that makes sense for our project.

# There are many different dunders that you can use, but in this
# topic, we will focus on the most helpful ones.

#  2. __new__ vs __init__
# So far we've been calling __init__ the constructor of the class,
# but in reality, it is its initializer. New objects of the class are in
# fact created by the __new__ method that in its turn calls the
# __init__ method.

# The first argument of the __new__ method is cls. It represents
# the class itself, similar to how self represents an instance of
# the class. This also makes __new__ a different kind of method
# since it doesn't require an instance of the class. This makes
# sense since it is supposed to create those instances. The method
# returns a new instance of the class which is then passed to the
# __init__ method.

# Usually, there is no need to define a special __new__ method,
# but it can be useful if we want to return instances of other
# classes or restrict the number of objects in our class.

# Imagine, for example, that we want to create a class Sun and
# make sure that we create only one object of this class. We would
# need to define a class variable that would track the number of
# instances in the class and forbid the creation of new ones if the
# limit has been reached.

class Sun:
    n = 0  # number of instances of this class

    def __new__(cls):
        if cls.n == 0:
            cls.n += 1
            return object.__new__(cls)  # create new object of the class
        