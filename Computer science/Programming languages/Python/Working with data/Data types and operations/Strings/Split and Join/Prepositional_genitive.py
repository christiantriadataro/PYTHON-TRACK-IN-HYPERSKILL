# Advanced input() handling is used to read input directly into
# several variables, for example:
x, y = input().split()

# Use it to print the next message with the two input values: "x
# of y"

def of(x, y):
    return f'{x} of {y}'

print(of(x, y))