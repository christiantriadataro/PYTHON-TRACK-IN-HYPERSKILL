# There's function blackbox(lst) that takes a list, does some
# magic, and returns a list. You don't know if it modifies the given
# list of creates a completely different one. Find this out and print
# "modifies" if the function changes the given list or "new" if
# the returned list is not connected to the initial one.

# Remember to define your list. Content is not important.

lst = [1, 2]
print("modifies" if blackbox(lst) is lst else "new")
