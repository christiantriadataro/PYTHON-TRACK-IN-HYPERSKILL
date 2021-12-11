# The class Patient needs both an unambiguous representation
# for developers and a readable string for users. Here's how they
# are supposed to look:

# - For developers: Object of the class Patient.name: {name},
#   last_name: {last_name}, age: {age}
# - For users: {name} {last_name}.{age}

# For example, for object john = Patient("John", "Doe", 50)
# these representations would respectively look like this:
# - Object of the class Patent.name: John, last_name: Doe,
#   age: 50
# - John Doe.50

# Create the necessary method below. Pay attention to spaces
# and punctuation in the strings.

class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here
    def __repr__(self):
        return f"Object of the class Patient. name: {self.name}, last_name: {self.last_name}, age: {self.age}"

    def __str__(self):
        return f"{self.name} {self.last_name}. {self.age}"

john = Patient("John", "Doe", 50)
print(john.__repr__())
print(john)