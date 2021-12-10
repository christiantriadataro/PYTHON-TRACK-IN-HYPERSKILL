# Letters
# Write a program that calculates how many distinct letters the
# input word has. The word is stored in the variable word. Print
# out the result you'll get.

# Sample Input:
# mississippi

# Sample Output:
# 4

word = input()  # the input
print(len(set(word)))