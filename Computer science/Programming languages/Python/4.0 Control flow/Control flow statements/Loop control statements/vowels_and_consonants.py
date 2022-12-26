# Let's work with texts! You'll get asequence of characters
# (a word, a sentence or just gibberish). For each character
# tell if it's a vowerl or consonant. If you hit a non-
# alphabetic symbol, just stop processing.

# The input format:
# One line with N characters.

# We will use letters from the English alphabet. The
# symbols aeiou are considered vowerls. Treat the rest of
# the letters as consonants.

# The output format:
# Print the line vowerl if the character is a vowerl, and
# consonant if the character is a consonant. Stop
# printing information at the first non-alphabetic symbol.
vowel = list("aeiou")
words = input()
for word in words:
    if not word.isalpha():
        break
    print("vowel" if word in vowel else "consonant")
