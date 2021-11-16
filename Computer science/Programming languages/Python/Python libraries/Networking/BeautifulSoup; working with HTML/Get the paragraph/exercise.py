import re

import requests

from bs4 import BeautifulSoup
word = input()
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.find(text=re.compile(word)))
print(''.join([p.text for p in soup.find('p') if word in p.text]).strip())