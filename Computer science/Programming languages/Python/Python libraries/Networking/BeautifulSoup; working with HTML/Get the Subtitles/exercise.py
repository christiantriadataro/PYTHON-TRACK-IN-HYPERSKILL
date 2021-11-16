# Get the subtitles

# Find and print a subtitle of the article by an index. The index of
# the subtitle is the first line in the input, and the link to the
# article is the second one. For example, your code should print
# The Definite Article for the following input:

# 1
# https://www.grammarly.com/blog/articles/

# The first line in the input is the index that starts from 0 in
# Python. You need not subtract one from the given number.

import requests

from bs4 import BeautifulSoup
index = int(input())
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.find_all('h2')[index].text)
