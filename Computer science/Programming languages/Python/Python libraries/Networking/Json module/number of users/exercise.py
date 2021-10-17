# Number of Users
# There is a JSON file users.json. The file has already been
# created and filled with data.

# It has the following structure.
# {
#   "users": [
#     {
#       "name": "John",
#       "last_name": "Doe",
#       "age": 33
#     },
#     ...
#   ]
# }

# Find out how many users are defined in this file and print this
# number.

# Note that the json module has already been imported, you
# don't need to import it again!
import json

with open('users.json', 'r') as user_file:
    users = json.loads(user_file)

for x, y in users.items():
    print(len(y))

with open('users.json', 'r') as user_file:
    print(len(json.load(user_file)['users']))

with open('users.json', 'r') as user_file:
    print(len(x) for x in users.values())