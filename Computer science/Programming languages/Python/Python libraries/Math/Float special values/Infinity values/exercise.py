# Which of the following expressions return the infinity values?

# Suppose, the variables inf and nan have been defined.
nan = float("nan")
inf = float("inf")

print(0.0 / inf)            # nan
print(inf / 2 - inf)        # inf
print(100 * inf + nan)      # inf
print(inf - 10 ** 300)      # nan
print(-inf * inf)           # inf
# print(inf % 0.0)