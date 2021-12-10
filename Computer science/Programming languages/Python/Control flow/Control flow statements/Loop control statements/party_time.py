# Jmaes is hosting a part today. He decided to welcome all new
# guests personally. To remember their names, James kindly asks
# you to write them in a list. Read the names from the input, each
# on a new line, and stop at a single period . that denotes the
# end of the sequence.

# Print your list and its length (the number of guests) for James.


names = []
while True:
    name = input()
    if name == '.':
        break
    names.append(name)
print(names)
print(len(names))

    