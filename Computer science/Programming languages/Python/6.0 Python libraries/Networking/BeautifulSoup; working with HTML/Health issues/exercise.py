# Read a link from the input. Get all the text paragraphs
# from all the a tags and single out the topics (not
# any word or phrase!) starting with the letter S. Print
# the final list. Beware of empty lines.

# For example, for this input and letter L (here we
# provide the link to the archive for consistency's
# sake):

# http://web.archive.org/web/20201201053628/https://www.who.int/health-topics

# output should be:
# ["Landslides", "Lassa fever", "Leishmaniasis", "Leprosy", "Lymphatic filariasis"]

# The link in the test will be the same one.
import re

import requests

from bs4 import BeautifulSoup


temp = []
r = requests.get('http://web.archive.org/web/20201201053628/https://www.who.int/health-topics')
soup = BeautifulSoup(r.content, 'html.parser')
for a in soup.find_all("a", text=re.compile("^L")):
        if 'topics' in a.get('href') or 'entity' in a.get('href'):
            if len(a.text) > 1:
                temp.append(a.text)
print(temp)