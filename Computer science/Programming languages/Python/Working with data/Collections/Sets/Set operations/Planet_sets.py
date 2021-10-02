# Using the three given sets, write a code that creates a set
# containing the elements that all of the original sets have in
# common. Output this resulting set.

# NB! You don't need to read the input; the variables containing
# the input data are already created for you.

# Sample Input 1:

# Jupiter Saturn Mars
# Earth Mars Venus
# Mars Pluto Uranus

# Sample Output 1:

# {'Mars'}

set_1 = set(input().split())
set_2 = set(input().split())
set_3 = set(input().split())

print(set_1 & set_2 & set_3)