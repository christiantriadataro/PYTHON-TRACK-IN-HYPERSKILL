# You know how to catch the built-in exceptions. Right now, try to
# create a function exception_check(a, b) that catches the
# ZeroDivisionError. If there is no ZeroDivisionError, print the
# result of their division. Otherwise, print the following message:
# The Error! Don't take any input.

# Sample Input 1:
# 45
# 15
# Sample Output 1:

def exception_check(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("The Error!")
