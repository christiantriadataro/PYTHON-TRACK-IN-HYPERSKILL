# You are given a list my_list that contains both negative and positive numbers.
# Define a function find_positive(my_list) that would construct and return a new list
# containing only those numbers from my_list that are greater than 0. Zero itself should
# not be included in the new list.

# Make use of map() or filter() where possible.

def find_positive(my_list):
    # complete the next line
    return list(filter(lambda x: x > 0, my_list))

print(find_positive([-1, 0, 1, 2]))