# Imagine that you want to buy a present for your friend, but you
# have little money. You want to choose a present which costs
# more than 120 cents and less than 137 cents.

# Implement a function called check() that takes a number as an
# argument. The function checks whether the number lies
# between 120 and 137. If the input is as expected, print it. If it
# is border or invalid, print the message "That's a bad
# present!"

# You do not need to take any input or call the function yourself.
# Only integer numbers will be given as parameters to the
# function

def check(x):
    print(x if 120 < x < 137 else "That's a bad present!")
