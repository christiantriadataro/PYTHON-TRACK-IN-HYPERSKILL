# Create a function called grades() that should take a grade
# as a argument (it can be 'A', 'B', 'C', 'D', or 'F'). If a correct
# parameter is given to the function, return the message "You
# have got <grade>", where <grade> is the given parameter. if
# there is something else as a parameter, use the assert
# keyword.

# You do not need to take any input or call the function 
# yourself.

def grades(x):
    grade = ['A', 'B', 'C', 'D', 'F']
    assert x in grade
    return f"You have got {x}"

print(grades(input()))
