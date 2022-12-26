# There is also one interesting feature of the built-in exceptions to 
# be mentioned. If you print dir(locals()['__builtins__]), you
# obtain a list of all built-in exceptions and functions that exist in
# Python. Your task is to use the index given in the input and print
# the name of the exception that has this index.

print( dir(locals()['__builtins__'])[int(input())])