# You are given two lists: letters contain the letters of
# the Latin alphabet and vowels contains only the vowels
# ['a', 'e', 'i', 'u', 'o']

# Define a function choose_vowels() that, given the list
# letters, would return only those letters that are
# vowels. You do NOT need to call the function or take any
# input.

# Sample of the list letters:

def choose_vowels(letters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda x: x in vowels, letters))
