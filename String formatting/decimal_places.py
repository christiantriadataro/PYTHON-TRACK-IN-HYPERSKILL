# Round the number from input to the required number of
# decimals.

# The input format:

# Two lines: the first with a floating-point number, the second
# with an integer representing the decimal count.

# The output format:

# A formatted string containing the rounded number.

# Do NOT forget to convert the input numbers and to enclose
# each value in {} in a formatted string

# Sample Input 1:

# 2.71828
# 3

# Sample Output 1:

# 2.718

# first solution
decimal = float(input())
nth_place = int(input())

print(f'%.{nth_place}f' % decimal)
#second sol
print(f'{decimal:.{nth_place}f}')

#one line code
print(f"{float(input()):.{int(input())}f}")


