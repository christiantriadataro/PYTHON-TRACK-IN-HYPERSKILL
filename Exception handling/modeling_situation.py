# Your program will have access to the exception_test()
# function, which can throw exceptions.

# You need to write code that runs this function, then catches
# ArithmeticError, AssertionError, ZeroDivisionError
# exceptions and prints the name of the caught exception.

# An example solution that you should send for review:
try:
    exception_test()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
