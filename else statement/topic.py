# Setting conditions is a pretty popular and useful tool in
# programming. However, sometimes just to check if a condition
# is true or not might not be enough. Let's say, you don't want a
# piece of code to execute if your condition is false, but, if that's
# the case, there is another piece of code you do want to execute.
# For situations like this Python has another powerful tool about
# which we're gonna learn in this topic!

# Simple if-else
# An if-else statement is another type of conditional expressions
# in Python. It differs from an if statement by the presence of the
# additional keyword else. The block of code that else contains
# executes when the condition of your if statement does not hold
# (the Boolean value is False). Since an else statement is an
# alternative for an if statement, only one block of code can be
# executed. Also, else doesn't require any condition:

if today == "holiday":
    print("Lucky you!")
else:
    print("Keep your chin up, then.")

# Note that the 4-space indentation rule applies here too.

# As you may soon find out, programmers do like all sorts of
# shortcuts. For conditional expression, there's a trick as well - 
# you can write an if-else statement in one line. This is called a
# ternary operator and it looks like this:

print("It's a day now!" if sun else "It's a night for sure!")

# Or, more generally:

# first_alternative if condition else second_alternative

# It's a metter of conveniece, but remember that the code you
# create should still be readable.

# Nested if-else
# It should be mentioned that if-else statements can be nested
# the same way as if statements. An additional conditional
# expression may appear after the if section as well as after the
# else section. Once again, don't forget to indent properly:

if x < 100:
    print('x < 100')
else:
    if x == 100:
        print('x = 100')
    else:
        print('x > 100')
    print('This will be printed only because x >= 100')

# Summary
# In this topic, we've learned about one more type of conditional
# expression: if-else statement. Let's go through the main points
# again:

# - the keyword else is used to give an alternative;
# - It will be executed in case if statement isn't;
# - It doesn't require any condition;
# - if-else statements can be nested.

# That's it! Now you are ready not only to set conditions but also
# to consider different alternatives. Congratulations!
