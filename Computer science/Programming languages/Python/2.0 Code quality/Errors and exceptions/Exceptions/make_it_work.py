# You have a program that is supposed to take two inputs from
# the user and turn them into integers to be compared later. Fix
# all the errors in this program, make it properly compare
# variables, and print the result.

# Sample input 1:
# 8
# 11
# Sample Output 1:
# The second one wins

# Sample Input 2:
# 5
# 5

# Sample Output 2:
# Draw

first = int(input())
second = int(input())
if first > second:
    print("The first one wins")
elif second > first:
    print("The second one wins")
else:
    print("Draw")
