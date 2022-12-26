# Some of the USA share their names with rivers. We have defined two variables
# with respective place names.

# Print out a new set with river names that don't overlap with given states.

# Sample Input 1:
# Alabama Missouri Mississippi
# Georgia Alaska Missouri

# Sample Output 1:
# {'Alabama', 'Mississippi'}

# work with these variables
rivers = set(input().split())
states = set(input().split())
rivers.difference_update(states)
print(rivers)