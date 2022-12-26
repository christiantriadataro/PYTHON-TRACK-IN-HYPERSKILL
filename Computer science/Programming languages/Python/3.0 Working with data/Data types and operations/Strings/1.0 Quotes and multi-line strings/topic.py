# Theory: 1.0 Quotes and multi-line strings

# You are already familiar with strings, which are extremely
# common and useful in programming. Let's take a look at some
# features of Python strings related to quotes and multi-lines
# strings.

# 1. Quotes
# As you know, a string literal is surrounded by a pair of single or
# double quotes. There is basically no difference between the
# two, but there are some common conventions concerning their
# use:

# - Use double quotes if your string contains single quotes,
#   for example, "You're doing great!".
# - Use single quotes if your string contains double quotes,
#   for example, 'Have you read "Hamlet"?'.
# - Do not mix two styles in one literal! For example,
#   something like "string!' is not correct.
# - Most importantly, be consistent in your use!

# There is a way to include any quotes in your string, regardless of
# the style of the outer quotes, and that is to use the backslash
# symbol (\) before the quotes inside of the string. The
# backslash will basically tell Python that the quote symbol that
# follows it is a part of the string rather than its end or beginning.
# It is called escaping, and you'll learn about it in detail in the next
# topics.

# In the examples below, both ways of writing strings are correct
# and will produce the same result:

# example 1
# print("You're doing great!")
# print('You\'re doing great!')
# example 2
# print("Have you read \"Hamlet\"?")
# print('Have you read "Hamlet"?')

# 2. Multiline strings
# Strings can represent a long text, a single character, or even no
# characters, like in the case of an empty string. One thing has so
# far been true about all of them: all our strings were single line,
# no matter how long they were. However, you can also write
# multi-line strings in Python! To do that, you need to use triple
# quotes on each side of the string literal. Again, the choice of
# single or double quotes is up to you as both work fine in Python.

# Multi-line string in double quotes:

# print("""This
# is
# a
# multi-line
# string""")

# Multi-line string in single quotes:

# print('''This
# is
# a
# multi-line
# string''')

# Both examples print the same result:

# This
# is
# a
# multi-line
# string

# 3. Summary
# In this topic, we've covered some basic information about using
# quotes in strings and saw how to write multi-line strings. This is
# by far not all you can do with strings in Python: there is a lot
# more to learn and, very importantly, to practice!
