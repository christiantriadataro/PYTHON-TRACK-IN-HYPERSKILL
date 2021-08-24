# Imagine that your friend asked you to write a program that finds
# the minimum and the maximum.

# Write the code that receives two integers as its input, each
# number goes on a new line. The output should show:

#  1. The biggest number in the first line
#  2. The smallest number in the second line.

# Note that your friend might insert identical numbers! In this
# case, just output both given numbers on seperate lines.

a = int(input())
b = int(input())

print(max(a, b))
print(min(a, b))