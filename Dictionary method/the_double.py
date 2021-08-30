# Write a program that creates a dictionary, in which keys are
# latin letters, and values are their doubling:

# {a: aa, b: bb, ..., z: zz}

# Save this dictionary ihn the variable double_alphabet.
import string


double_alphabet = {}
for i in string.ascii_lowercase:
    double_alphabet.update({i: 2 * i})
print(double_alphabet)