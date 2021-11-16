# Get the hyperlink

# You will get a link to a web page with the text of "Pygmalion" by
# Bernand Shaw. There are several hyperlinks on this page, which
# can be used to jump to one of the play's five acts.

# Write a program that prints a hyperlink to the specific act. The
# number of the act and the link to the page with the text will be
# given as two lines in the input. For example, the input may look
# as follows:

# 3
# http://www.gutenberg.org/files/3825/3825-h/3825-h.htm

# It is important that you read the link from the input, rather than
# specify it yourself!

# Then, your program should print the hyperlink #act3. Note that
# you shouldn't print the WHOLE page link, just this small part.
import re

import requests

from bs4 import BeautifulSoup

act = input()[0]
url = input()

soup = BeautifulSoup(requests.get(url).content, 'html.parser')
anchors = soup.find('a', href=re.compile(act))
print(anchors['href'])


