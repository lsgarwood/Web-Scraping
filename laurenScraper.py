from bs4 import BeautifulSoup
import csv
import requests
import sys

# url, searchTerm = sys.argv[1], sys.argv[2]

html_text = requests.get('https://www.woolwarehouse.co.uk/yarn?brand_nav=39580').text

soup = BeautifulSoup(html_text, 'lxml')

yarns = soup.find_all('li', class_= 'item')

for index, yarn in enumerate(yarns):
    descriptionText = yarn.find('div', class_='desc std').text
    if '4 Ply' in descriptionText:
        title = yarn.h2.a['title']
        details = yarn.find('div', class_='desc std').text
        more_info = yarn.h2.a['href']
        # print(f'yarn: {title}, details: {details}, link: {more_info}')

        with open(f'Yarn-listing-4ply.csv', 'a') as f:
            f.write(f'index: {index},\nyarn: {title},\ndetails: {details},\nlink: {more_info}\n-----------------\n')


        # print(f'''
        #     yarn: {title}
        #     details: {details}
        #     link: {more_info}
        #     ''')

        # csvFile = open(f'yarn-listing-4ply.csv', 'wt+')
        # writer = csv.writer(csvFile)
        # writer.writerow(f'yarn: {title}\n, details: {details}\n, link: {more_info}\n -----------------')

# if __name__ == "__main__":
#     print(f"Arguments count: {len(sys.argv)}")
#     for i, arg in enumerate(sys.argv):
#         print(f"Argument {i:>6}: {arg}")