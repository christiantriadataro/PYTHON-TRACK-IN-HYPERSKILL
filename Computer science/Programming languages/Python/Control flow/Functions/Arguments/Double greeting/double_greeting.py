# We wrote a function that greets two people:

def greeting(first_name, second_name):
    print("Hello,", first_name, "and", second_name)

# The first name is already stored in the variable name_1, and the
# second is stored in the variable name_2. Your task it to call this 
# function twice in the code section. The first time it should print
# Hello, name_1 and name_2, and the second time Hello, name_2
# and name_1.


name_1 = input()
name_2 = input()

greeting(name_1, name_2)
greeting(name_2, name_1)