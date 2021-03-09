# A beautifulsoup job search webscraper
from bs4 import BeautifulSoup
from requests import get
import texttable

url = "https://www.seek.com.au/system-administrator-jobs/in-Toowoomba-&-Darling-Downs-QLD"
soup = BeautifulSoup(get(url).text, 'html.parser')

jobs = soup.findAll('article')

table = texttable.Texttable(max_width=200)

# Find and print Seek listings
for job in jobs:
    pageurl = "https://www.seek.com.au/" + job.find('a',{"data-automation":"jobTitle"}).get('href')
    page = BeautifulSoup(get(pageurl).text, 'html.parser')
    result = []

    title = job.find('a',{"data-automation":"jobTitle"}).text
    result.append(title)

    try:
        company = job.find('a',{"data-automation":"jobCompany"}).text
    except AttributeError:
        company = "Private Advertisor"
    result.append(company)

    location = job.find('a',{"data-automation":"jobLocation"}).text
    result.append(location)

    try:
        salary = job.find('span',{"data-automation":"jobSalary"}).span.text
    except:
        salary = "No Listed Salary"
    result.append(salary)

    description = job.find('span',{"data-automation":"jobShortDescription"}).span.text
    result.append(description)

    listed_date = job.find('span',{"data-automation":"jobListingDate"}).text
    result.append(listed_date)
    
    start_date = page.find('dd',{"data-automation":"job-detail-date"}).span.span.text
    result.append(start_date)

    table.add_row(result)

print(table.draw())