# In Python, the names of classes follow the CapWords
# convention. Let's convert the input phrase accordingly by
# capitilizing all words and spelling them without underscores in-
# between.

# The input format:

# A word or phrase, with words separated by underscores, like
# function and variable names in Python.

# You might want to change the case of letters since they are not 
# necessarily lowercased.

# The output format:
# The name written in the CapWords fashion.
# word.capitalize() if word.isalpha else
word = input()
print(word.title() if word.find("_") == -1 else word.title().replace("_", ''))

print(''.join([x.capitalize() for x in input().lower().split('_')]))