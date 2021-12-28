# Let's do some text formatting. Read an input word and print it
# with an indicated number of spaces between the letters. There
# are two different inputs: a word in the first line and a number of
# spaces in the second line.

print(*input(), sep=int(input()) * ' ')