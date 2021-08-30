# Let's say it's a wedding day, and two happy people are getting
# married. 

# we have a dictionary first_family, which contains the names
# of the wife's family members. For example:
first_family = {"wife": "Janet", "wife's mother": "Katie", "wife's father": "George"}

# And a similar dictionary second_family for the husband's
# family:
second_family = {"husband": "Leon", "husband's mother": "Eva", "husband's father": "Gaspard", "husband's sister": "Isabelle"}

# Create a new dictionary that would contain information about
# the big new family. Similarly with the ones above, family 
# members should be keys and their names should be values.
# First, update the new dictionary with elements from
# first_family and then from second_family. Print it out.

# The following lines create dictionaries from the input
first_family = json.loads(input())
second_family = json.loads(input())

# Work with the 'first_family' and 'second_family' and create a new dictionary
big_family = first_family
big_family.update(second_family)
print(big_family)