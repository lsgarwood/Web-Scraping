import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = sys.argv[1]
searchTerm = sys.argv[2]

page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

def findSearchTerm(searchTerm):
    if searchTerm in soup.text.strip():
        print(True)
    else:
        print(False)

findSearchTerm(searchTerm)