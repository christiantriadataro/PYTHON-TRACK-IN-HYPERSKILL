# Checking email
# Let's say you've created a registration form for
# people wanting to take part in your online book
# club. In order to send them invitations, you need to
# know their email address, so you are writing a
# program to check whether the field "email" is filled
# correctly.

# Write a function that takes a string and checks that
# a user's email meets the following conditions:
# 1. it doesn't contain spaces,
# 2. it contains the @ symbol,
# 3. after @, there's a dot, but in a correct
#    address a dot shouldn't stand immediately
#    after @,
#    (@. should not be in the string).

# Note that dots may also occur before @!

# The function should return True if all of the
# conditions are true,and False otherwise.

# You are not supposed to handle input or call your
# function just implement it.

# Sample Input
# My e-mail is: this@example.com

# Sample Output:
# False

# def check_email(string):
#   ' ' not in string

def check_email(string):
    return '.' in string[string.find('@') + 2:] and '@' in string and ' ' not in string



print(check_email("My e-mail is: this@example.com"))