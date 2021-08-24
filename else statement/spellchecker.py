# Write a simple spellchecker that tells you if the word is spelled
# correctly. Use the dictionary in the code below; it contains the
# list of all correctly written words.

# The input format:
# A single line with the "word"

# The output format:
# If the word is spelled correctly write Correct, otherwise,
# Incorrect.

dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]

word = input()

print("Correct" if word in dictionary else "Incorrect")