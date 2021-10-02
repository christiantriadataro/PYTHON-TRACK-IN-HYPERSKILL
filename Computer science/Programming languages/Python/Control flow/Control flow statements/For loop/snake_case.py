# Since we are learning Python, sometimes it might be useful to
# convert text from lowerCamelCase to snake_case. The main trick is
# to find the correct place where to insert an underscore.
# Let's make a rule that it's right before a capital letter of the next
# word. If the first letter is capitalized, convert it to lowercase and
# don't forget to insert an underscore before it.

# The input format:
# Read a word or a phrase written in lowerCamelCase.

# The output format:
# Print out words in lowercase and separate them by
# underscores.

def convert(camel):
    snake = [camel[0].lower()]
    for c in camel[1:]:
        if c == c.upper():
            snake += '_' + c.lower()
        else:
            snake += c
    return ''.join(snake)

def change(camel):
    return ''.join(['_' + i.lower() if i.isupper()
              else i for i in camel]).lstrip('_')


camel = input()
print(change(camel))

