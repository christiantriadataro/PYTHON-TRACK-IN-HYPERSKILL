# Full name

# Rewrite the code below using the with keyword.

# Make sure to use the same variable names for file objects!

with open('name.txt') as f1, open('surname.txt') as f2, open('full_name.txt', 'w') as f3:
    name = f1.read()
    surname = f2.read()
    f3.write(f"{name} {surname}")
