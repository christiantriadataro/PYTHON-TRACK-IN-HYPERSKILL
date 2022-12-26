# Advanced input() handling is used to read input directly into
# several variables, e.g.,

# name, surname = input().split(), but a user still can enter
# more or fewer words.

# In this task, you have to make sure that the user entered the
# necessary amount of words and...
#   - If there are more or fewer words in the input, print an
#     error: "You need to enter exactly 2 words. Try again!"
#   - If everything's good, greet the user personally.

try:
    name, surname = input().split()
except ValueError:
    print("You need to enter exactly 2 words. Try again!")
else:
    print("Welcome to our party,", name, surname)