# Animals

# The file animals.txt has a list of animals, each written on a new
# line. For example:

# rabbit
# cat
# turtle

# Create a new file, animals_new.txt, where those animals are
# written on a single line and separated by a whitespace.

# Don't forget to close all files!

with open('animals.txt', 'r') as old, open('animals_new.txt', 'w') as new:
    new.writelines([animal.replace('\n', ' ') for animal in old.readlines()])


