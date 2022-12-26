# Write a function check_values that accepts two values (for
# example, 0 and 1, or "string" and []) and checks if both of
# them are True. To achieve this, convert the values via the built-in
# bool() function.

# If both values are True, then your function should return True,
# otherwise False, Note that you are NOT supposed to call the 
# function, just implement it.

def check_values(first_value, second_value):
    return bool(first_value) and bool(second_value)