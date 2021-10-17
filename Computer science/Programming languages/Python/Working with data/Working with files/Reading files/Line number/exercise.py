# Line number
# Read the file sample.txt and print the number of lines that this file has.

# Don't forget to close the file!

# read sample.txt and print the number of lines
with open('sample.txt', 'r') as file:
    print(len(file.readlines()))
