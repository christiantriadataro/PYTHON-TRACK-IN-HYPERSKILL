# Requests: retrieving data -> Searching for a book

# You are looking for a rare book in multiple online stores. To
# automate the process, you want to write Python code that
# would collect the search results for you.

# Define a function do_search(bookstore_url, params) that takes
# the url of the store bookstore_url and the dictionary of the
# search parameters params, sends a GET request to the page
# with the search results and returns the response object.

# For instance, if bookstore_url =
# 'http://bookstore.com/search' and params = {'author':
# 'Austen', 'title': 'Emma'}, the response object should
# contain the data retrieved from
# http://bookstore.com/search?author=Austen&title=Emma.

# Note that you do not need to read any input or call the funciton
# do_search() yourself.

import requests


def do_search(bookstore_url, params):
    return requests.get(bookstore_url, params=params)



print(do_search('http://bookstore.com/search', {'author': 'Austen', 'title': 'Emma'}))
