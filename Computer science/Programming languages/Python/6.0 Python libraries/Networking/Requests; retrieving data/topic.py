# Theory: Requests: retrieving data

# This topic is an introduction to requests, an elegant and simple
# HTTP library for Python.

# Hypertext Transfer Protocol (HTTP) is arguably the most
# popular application protocol used on the Internet. It allows for
# communication between HTTP clients (e.g., web browsers) and
# HTTP servers (web servers) by sending text messages: the
# client sends a request message to the server which, in turn,
# returns a response message.

# Python requests allows you to send all kinds of requests and
# get the responses to them in an easy and intuitive way. Don't
# forget that it's not in the standard library, and therefore you
# might need to instal it by typing pip install requests in your
# command line.

# To start using requests in your code, import the library:

import requests

# 1. Making a GET request
# The GET request is used to retrieve information from the given
# server using a URL. For example, whenever you enter a URL in
# the address box of your browser, it translates it into a GET
# requests message and sends it to the server.

# Imagine we need to get the main page of the official website of
# the requests library. We can do so with the help of
# requests.get(url) as follows:

r = requests.get('https://requests.readthedocs.io/en/master/')

print(r)

# <Response [200]>

# This returns a response object r containing all the necessary
# information about the response of the server. Note that 200 is a
# standard HTTP code indicating that the request succeeded,
# while code 404 means that the resource you were looking for
# was not found. You can explicitly access the response code in
# the status_code attribute of the response object:

print(r.status_code)

# If you use a response object in an if statement, it will
# evaluate to True if the status code starts with the digits 2
# (request was accepted) or 3 (redirection), and False
# otherwise:

if r:
    print("Success!")
else:
    print("Fail")

# Success!

# To read the content of the server's response, look at the text
# property:

# print(r.text)


# Note that requests automatically decodes the content of the
# response from the server. You can find out what encoding is
# being used and change it, if necessary, using the encoding
# property:

print(r.encoding)

# Other useful information, e.g., content type, is stored in the
# response headers. To view them, access .headers:

r = requests.get('https://requests.readthedocs.io/master')
print(r.headers)

# A dictionary-like object is returned, so you can access the
# header value you need by its key. Note that the headers are
# case-insensitive, meaning you don't have to worry about their
# capitalization:

print(r.headers['Content-Type'])

# 2. Query parameters
# A query string is a convention for appending key-value pairs to a
# URL. It's separated from the standard URL with a question mark
# sign ? and contains key-value pairs. Each key is separated from
# the value by an equality sign =, while the pairs are separated
# by the ampersand &.

# Query strings can include fields added to a base URL by the
# browser or other client applications. How these parameters are
# used it up to the server-side application. For example,
# https://www.python.org/search/ is a search page of the official
# Python website. If you search for 'requests' there, the results
# will be displayed on the page with the URL
# https://www.python.org/search/?q=requests.

# When using requests, there's no need to manually add query
# strings to your URLs. The library allows you to provide these
# arguments as a dictionary of strings using the params keyword
# argument when making a requests:

# The dictionary of the query parameters
params = {'q': 'requests'}

# This request will get the page with the results of the search for 'requests'
# on the official Python website:
r = requests.get('https://python.org/search', params=params)


# If you need to send similar requests multiple times in your
# project, it makes sense to define a special function for that. For
# example, google_search(query, num) returns a URL to the page
# containing num Google search results for a given query:

def google_search(query, num):
    r = requests.get('https://google.com/search',
                     # ?q={query}&{num}=1
                     params={'q': query, 'num': num})
    return r.url


print(google_search('python', 1))

# https://www.google.com/search?q=python&num=1

        # Unfortunately, a lot of requests to Google can lead to
        # banning. Try to be attentive when sending multople
        # requests!

# 3. Summary
# - requests is a Python library for making HTTP requests.
# - GET requests requests.get() is used to retrieve the data
#   from the server.
# - To provide additional parameters to the server with your
#   GET request, use a query string.
# - A query string can be passed to requests.get() as a
#   dictionary of key-value pairs.

