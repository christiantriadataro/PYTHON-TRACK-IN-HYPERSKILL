# The class Patient needs both an unambiguous representation
# for developers and a readable string for users. Here's how they
# are supposed to look:

# - For developers: Object of the class Patient.name: {name},
#   last_name: {last_name}, age: {age}
# - For users: {name} {last_name}.{age}

# For example, for object john = Patient("John", "Doe", 50)
# these representations would repe