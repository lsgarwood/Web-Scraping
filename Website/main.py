from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://appointments.thetimes.co.uk/jobs/?Keywords=python#browsing').text

soup = BeautifulSoup(html_text, 'lxml')
# print(soup.prettify)
jobs = soup.find_all('li', class_= 'lister__item cf lister__item--display-logo-in-listing lister__item--display-logo-in-listing lister__item--is-backfill')
# print(job)

for job in jobs:
    location = job.find('li', class_='lister__meta-item lister__meta-item--location').text
    # print(job_location)
    if 'London' in location:
        salary = job.find('li', class_='lister__meta-item lister__meta-item--salary').text
        # print(job_salary)
        print(f'''
            Job Location: {location}
            Salary: {salary}
            ''')