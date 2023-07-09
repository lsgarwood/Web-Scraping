from bs4 import BeautifulSoup
import requests
#  import time


# def find_jobs():

html_text = requests.get('https://appointments.thetimes.co.uk/jobs/?Keywords=python#browsing').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_= 'lister__item cf lister__item--display-logo-in-listing lister__item--display-logo-in-listing lister__item--is-backfill')
for index, job in enumerate(jobs):
    location = job.find('li', class_='lister__meta-item lister__meta-item--location').text
    if 'London' in location:
        title = job.h3.span.text
        salary = job.find('li', class_='lister__meta-item lister__meta-item--salary').text
        more_info = job.h3.a['href']
        with open(f'AdvancedScraper/posts/{index}.txt', 'w') as f:
            f.write(f'Title: {title}')
            f.write(f'Location: {location}')
            f.write(f'Salary: {salary}')
            f.write(f'More Info: {more_info}')
        print(f'File saved: {index}')

# To put in a repeat timer
# if __name__ == '__main__':
#     while true:
#         find_jobs()
#         time_wait = 10
#         print(f'Waiting {time_wait} minutes...')
#         time.sleep(time_wait * 60)