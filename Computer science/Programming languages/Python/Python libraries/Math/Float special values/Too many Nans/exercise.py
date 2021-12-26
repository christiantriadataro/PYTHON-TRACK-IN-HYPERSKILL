# Look at the expressions below and pick the ones that result in nan.

# Assume variables nan and inf defined as float("nan") and float("inf") respectively.

nan = float("nan")
inf = float("inf")

print(nan - inf)
print(inf - inf)
print(nan * 10)
print(nan ** 0)
print(-inf / inf)
# print(inf % 0.0)