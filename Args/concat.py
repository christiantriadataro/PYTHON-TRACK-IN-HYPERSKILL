# Write a concat() function that will take an arbitrary number of 
# strings and combine them into one through a separator (the
# keyword argument sep). If no separator is specified, then it
# should separate the strings by spaces:
def concat(*args, sep=" "):
    string = ''
    for n in args:
        string += sep + n
    return string

# print(concat("turtle"))                # "turtle"
# print(concat("cat", "dog"))            # "cat dog"
# print(concat("a", "b", "c", sep=":"))  # "a:b:c

def con(*args, sep=" "):
    return sep.join(args)

print(con("turtle"))                # "turtle"
print(con("cat", "dog"))           # "cat dog"
print(con("a", "b", "c", sep=":"))  # "a:b:c