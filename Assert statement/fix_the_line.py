# Imagine that you want to write a program that checks an email
# address input by a user. Now, your program is very simple: If the
# string contains the '@' sign, you want to print the word "Done!",
# otherwise, you should use the assert keyword and output the
# message "try again!". This procedure is implemented in the
# following piece of code:

email = input()

def check_email(address):
    assert '@' in address, 'Try again!'
    return "Done!"
    
check_email(email)