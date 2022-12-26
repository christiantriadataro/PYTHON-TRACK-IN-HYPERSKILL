# Eugene and Rose decided to travel abroad. For convenience, they will to a country
# where one of them has already been, but not where they both have.

# Output a set of potential countries for them.

# Sample Input 1:
# Greece Netherlands Colombia UK
# Italy UK Russia Greece Canada

# Sample Output 1:
# {'Columbia', 'Russia', 'Italy', 'Netherlands', 'Canada'}
new_set = {}
# work with these variables
eugene = {'Greece', 'Netherlands', 'Colombia', 'UK'}
rose = {'Italy', 'UK' ,'Russia', 'Greece', 'Canada'}
new_set = eugene.difference(rose).union(rose.difference(eugene))
print(new_set)
