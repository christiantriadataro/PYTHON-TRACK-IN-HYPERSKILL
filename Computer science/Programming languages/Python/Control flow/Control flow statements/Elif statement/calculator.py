# Let's write a simple calculator!
# it will read 3 lines:
# the first number
# the second number
# the arithmetic operation.

# Numbers are floats!

# The output is the result of the following: first_number
# operation second_number

# Operations are: +, -, /, *, mod, pow, div.
# mod - modulo operation, i.e. the remainder of the division
# first_number % second_number,
# pow - exponentiation, the first number will be the base and the
# second- the power: first_number ** second_number, 
# div - integer division first_number // second_number.

# Note that if the second number is 0 and you want to perform
# any of the operations /, mod, or div, the calculator should
# say "Division by 0!"

# put your python code here

first_number = float(input())
second_number = float(input())
operation = input()
forbidden = ['/', 'mod', 'div']
if operation == '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == 'pow':
    print(first_number ** second_number)

if second_number == 0.0 and operation in forbidden:
    print("Division by 0!")
else:
    if operation == 'mod':
        print(first_number % second_number)
    elif operation == '/':
        print(first_number / second_number)
    elif operation == 'div':
        print(float(first_number // second_number))

