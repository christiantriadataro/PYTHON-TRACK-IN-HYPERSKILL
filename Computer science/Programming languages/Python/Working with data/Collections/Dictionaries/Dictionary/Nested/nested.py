# Imagine, there are three children in a family and they wrote
# down what they want to be when they grow up:

children = {'Emily': 'artist', 'Adam': 'astronaut', 
            'Nancy': 'programmer'}
# Let's say you want to store not only the profession they have
# chose, but also their age: Emily is 5, Adam is 9, and Nancy is
# 14. Todo so, you can create nested dictionaries for each key in 
# the outer dictionary.

# For each name, create a nested dicitonary with the key
# 'profession' and 'age', modify the dictionary children but
# don't print it.

# NB: write the age as an integer.

children = {'Emily': {'profession': 'artist', 'age': 5},
            'Adam': {'profession': 'astronaut', 'age': 9},
            'Nancy': {'profession': 'programmer', 'age': 14}}