import sys
import re
from bs4 import BeautifulSoup
from collections import Counter
from urllib.request import urlopen

url = sys.argv[1]
searchTerm = sys.argv[2]

page_content = urlopen(url)
soup = BeautifulSoup(page_content, 'html.parser').text

def findSearchTerm(searchTerm):
    counter = Counter()
    if searchTerm in soup.strip():
        counter[searchTerm] += len(re.findall(r'\b%s\b' % searchTerm, soup))
        for key, count in counter.most_common():
            print(f'Your search term {key} was found {count} times')
    else:
        print('Your search term was not found')

findSearchTerm(searchTerm)