# Imagine you're working at IMDb and your new task is to write a
# program that will replace all the letters with ligatures and
# diacritic marks with their equivalents from the Latin alphabet in
# the celebrities' names. The list of replacements is the following:

# é -> e
# ë -> e
# á -> a
# å -> a
# œ -> oe
# æ -> ae

# Complete the code below so that the function would take a 
# string with diacritics and return the one where all of them have
# been replaced with the equivalents.

name = input()

def normalize(new_name):
    # put your code here
    return new_name.replace('ë', 'e').replace('é', 'e').replace('á', 'a').replace('å', 'a').replace('œ', 'oe').replace('æ', 'ae')

print(normalize(name))