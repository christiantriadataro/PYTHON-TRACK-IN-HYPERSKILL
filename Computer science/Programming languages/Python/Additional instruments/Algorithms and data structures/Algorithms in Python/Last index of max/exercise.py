# In the topic, you were given an algorithm that finds the first index of maximum
# element in a list of numbers. Your task here is to modify that algorithm so that if finds
# the last index of the maximum element.

# The input and output examples below are there to give you the idea of the algorithm. You
# do NOT need to work the input, call function, or print anything!

def last_indexof_max(numbers):
    return max(x for x, y in enumerate(numbers) if y == max(numbers))