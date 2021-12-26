# Write a function that returns an object whose identity ends with
# 888.

# iterate numbers from 0 to 10_000 and check their identity via
# id() to find a value ending with ...888.
def object_with_beautiful_identity():
    for i in range(10_000):
        # Change the next line
        if (id(i) % 1_000) == 888:
            return i
    return None
