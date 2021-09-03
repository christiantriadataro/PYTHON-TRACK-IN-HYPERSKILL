# Below you can see the class User.

# This class has two methods: __init__ and add_friends

# The __init__ method does what any __init__ does, while
# add_friends increases the number of friends that the user has
# by the value of n. However, the add_friends method has been
# defined somewhat incorrectly and right now it doesn't do what
# it's supposed to do.

# Your task is to fix the mistakes in the method.

class User:
    def __init__(self, username):
        self.username = username
        self.friends = 0
    
    # fix this method
    def add_friends(self, n):
        self.friends += n
        print("{} now has {} friends.".format(self.username, self.friends))