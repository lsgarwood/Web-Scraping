from bs4 import BeautifulSoup
import requests
import sys

searchTerm = sys.argv[1]

html_text = requests.get('https://www.woolwarehouse.co.uk/yarn?brand_nav=39580').text

soup = BeautifulSoup(html_text, 'lxml')
yarns = soup.find_all('li', class_= 'item')
for index, yarn in enumerate(yarns):
    descriptionText = yarn.find('div', class_='desc std').text
    if searchTerm in descriptionText:
        title = yarn.h2.a['title']
        details = yarn.find('div', class_='desc std').text
        more_info = yarn.h2.a['href']

        with open(f'Yarn-listing-{searchTerm}.csv', 'a') as f:
            f.write(f'index: {index},\nyarn: {title},\ndetails: {details},\nlink: {more_info}\n-----------------\n')

print(f'Your search results have been written to: Yarn-listing-{searchTerm}.csv')

# if __name__ == "__main__":
#     print(f"Arguments count: {len(sys.argv)}")
#     for i, arg in enumerate(sys.argv):
#         print(f"Argument {i:>6}: {arg}")