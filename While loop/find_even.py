# Write a program that prints all positive even numbers less
# than the input number. Please, use the while loop for that.

# The input format:
# The maximum number N varying from 1 to 200.

# The output format;
# All positive even numbers that are less than N. Print them in
# the ascending order. Each number must be on a separate line.
n = int(input())
i = 2
while i < n:
    print(i)
    i += 2
