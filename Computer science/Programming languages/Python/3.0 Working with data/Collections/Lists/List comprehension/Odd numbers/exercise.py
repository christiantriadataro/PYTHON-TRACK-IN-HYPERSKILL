# Read a string with digits from the input and convert each
# number to an integer. Create a list in which you should include
# only odd digits. Finally, print what you'll get.

print([int(x) for x in input() if int(x) % 2])
