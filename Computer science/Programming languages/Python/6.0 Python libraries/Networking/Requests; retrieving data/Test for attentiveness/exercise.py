# Take a look at the following code snippet. First, we retrieve data
# from the main page of Python's documentation. Then we want
# to check if the content of the resource is represented in 'ISO-
# 8859-1'. If it is not, the program should print the message 'You
# should change the encoding'.

import requests

url = 'https://docs.python.org/3/'
r = requests.get(url)

if r.encoding == 'ISO-8859-1':
    print('Right encoding!')
else:
    print('You should change the encoding')