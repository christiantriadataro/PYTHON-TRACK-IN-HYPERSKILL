# Kitty wants to visit a cat café! Help her find the one with the largest number of cats.
# Input format
# Each string contains a café's name followed by a space and the number of cats in it, e.g.
# Paws 11, Kittens 9.

# The names would be one-word only. Read input lines until you get a string MEOW
# (without any number).

# Output format
# The café with the maximum number of cats.

cat_cafe = {}
while True:
    try:
        cafe, n = input().split()
    except ValueError:
        break
    cat_cafe[int(n)] = cafe
print(cat_cafe[max(cat_cafe.keys())])