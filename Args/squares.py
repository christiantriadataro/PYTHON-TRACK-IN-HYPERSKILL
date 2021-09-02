# Declare a function sq_sum() that calculates the squares for
# arguments passed into it and returns their sum.

def sq_sum(*args):
    total = 0
    for n in args:
        total += (n ** 2)
    return total

def sqsum(*args):
    return sum(n ** 2 for n in args)

def sqsum(*args):
    return sum(pow(n,2) for n in args)

print(sqsum(1, 2, 2, 4))  # 25.0
print(sqsum(1.5))         # 2.25
print(sqsum(1, 10, 10))   # 201.0