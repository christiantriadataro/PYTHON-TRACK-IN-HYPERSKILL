# You need to create a class User that has the following
# attributes:

# active - a boolean attribute that indicates whether a user is
# activate at the moment,

# n_active = the number of active users,

# user_name = string with the username,

# users = a list of all users.

# The catch is that some of these attributes should be defined
# as class attributes, and others should be instance attributes.

# If there are 2 or more instance attributes, please list the in
# the __init__ in alphabetical order.

# NOTE: you do NOT need to create an instance of this class or
# print anything. YOU are also NOT required to write any
# additional code for modifying class attributes (leave them
# with default values).

class User:
    # class attributes
    n_active = 0
    users = []

    # instance attributes
    def __init__(self, active: bool, user_name: str):
        self.active = active
        self.user_name = user_name
        if active:
            User.n_active += 1
        User.users.append(self.user_name)


User(True, "Chan")
User(True, "Chong")
print(User.n_active)
print(User.users)