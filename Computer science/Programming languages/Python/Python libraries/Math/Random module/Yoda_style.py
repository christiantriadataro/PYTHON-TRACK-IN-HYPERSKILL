# Everybody wants to speak like master Yoda sometimes. Let's try to implement 
# a program that will help us with it.

# First, we turn the string of words into a list using the 
# string.split() method.

# Then use the function random.seed(43) and rearrange the 
# obtained sequence.

# To turn the list back into a string, use ' '.join(list)

# Print the message in the end.

# Note: you have to use random.seed(43) in this task!

import random

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
random.seed(43)
random.shuffle(sentence)
# shows the message
print(' '.join(sentence))