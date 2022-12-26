# Theory: BeautifulSoup: working with HTML

# Imagine you are a student who is eager to study regional
# press news. If you collect every news piece manually, it
# will take plenty of time. Lucky for us, Python has some
# tools to offer to automate this process. beautifulsoup is
# a library that helps you analyze the HTML and the XML
# syntax, create parse trees and extract necessary
# information. It also provides web scraping, a simple
# technique of getting data for further analysis. So, by
# combining basic operations in Python, requests, and
# beautifulsoup libraries, you can get all the texts and
# save precious time. Although it is possible to work with
# XML using the library, in this topic, we will focus on
# HTML.

# 1. Installation
# To install beautifulsoup, you need a Python package
# manager pip.

# pip install beautifulsoup4

# Also, you need the requests library to send HTPP
# requests. It can also be installed using ip.

# pip install requests

# Do not forget to import these libraries before starting
# your work.

import requests
from bs4 import BeautifulSoup

# 2. Getting started with web scraping
# First, we need to create a variable that will store the
# content of the page. To do so, use requests.get() with a
# link as an attribute.

r = requests.get('https://newsineasyenglish.com/2018/05/13/air-pollution/')

# To check whether the page was downloaded successfully,
# you can use status_code. If the returned code is 200,
# there are no errors. If your code is 400 or 500, there are
# some difficulties with getting the page.

print(r.status_code)

# Then we use BeautifulSoup() class to create a parse
# tree of our page.

soup = BeautifulSoup(r.content, 'html.parser')

# There are two parameters: r.content is the data of the
# page, and html.parser is a parser included in the
# standard Python library. You can install additional parsers
# like lxml via pip and use them instead of the
# html.parser. The lxml parser is used for swift
# processing.

# The result of the procedure is a tree. You can use the
# prettify() method to turn your tree into a nicely
# formatted string.