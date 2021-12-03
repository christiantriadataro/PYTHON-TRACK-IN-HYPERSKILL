# N squirrels found K nuts and decided to divide them equally.
# Find how many nuts will be left after each of the squirrels takes
# the equal amount of nuts.

# Input data format

# There are two positive integers N and K, neither of them are
# greater than 10000.

# Sample Input 1:

# 3
# 14
# Sample Output 1:

# 2

# put your python code here
# print(int(input()) % int(input()))
N = int(input())
K = int(input())
print(K % N)

print("{1} % {0}".format(int(input()), int(input())))