# In a galaxy far, far away, there is a planet where biology works in
# mysterious ways. Not only do the planet's residents inherit genes
# from their parents, but also parts of their identity. Each parent
# contributes one half.

# Read two strings with parental genetic information, find their IDs
# and calculate the mean, that is alien = id(one)+id(other)/2.

# Note that the found identity should be an integer. Also, do NOT
# print the result and rename the variables defined below.

# The parental gene sequences are stored here
one_ancestor = input()
other_ancestor = input()

# Calculate the identity of a new alien here
new_alien = (id(one_ancestor) + id(other_ancestor)) / 2
