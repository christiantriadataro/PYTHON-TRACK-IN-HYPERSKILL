# Write a program that calculates the factorial of the input
# number using while loop.

# The input format:
# The number N in range from 1 to 100
# The output format:
# The factorial NI.

n = int(input())
ni = 1
i = n
while i > 1:
    ni *= i
    i -= 1
print(ni)