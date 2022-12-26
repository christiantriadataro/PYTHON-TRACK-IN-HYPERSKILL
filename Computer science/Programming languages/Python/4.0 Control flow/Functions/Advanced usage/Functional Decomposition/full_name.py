# In the code below, you can see a program that creates a full
# name from the first and last names for several people.

name_1 = "John"
last_name_1 = "Lennon"
full_name_1 = name_1 + " " + last_name_1

name_2 = "Hermione"
last_name_2 = "Granger"
full_name_2 = name_2 = " " + last_name_2

# Wouldn't it be much easier if we had a function that could do the
# same?

# Your task is to write the body of the function create_full_name
# that takes name and last_name (in this order) and returns the
# full name.

# Do NOT change the variable names. You don't need to call the
# function yourself.

def create_full_name(name, last_name):
    return name + " " + last_name
