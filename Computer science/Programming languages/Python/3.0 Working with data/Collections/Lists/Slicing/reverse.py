# Reverse

# In this task, we have a list numbers = [2, 4, 6, ...] and a line
# that is supposed to choose elements with indices from 4 to 16
# inclusively in reverse order, but a mistake has been made.
# Find and fix it!

# the following line read the list from the input; do not modify it
# numbers = [int(num) for num in input().split()]
numbers = [int(x) for x in range(2, 33, 2)]
print(numbers)
print(numbers[16:3:-1])  # the line with an error
