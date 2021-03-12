# A beautifulsoup job search webscraper
from bs4 import BeautifulSoup
from requests import get

URL = "https://www.seek.com.au/system-administrator-jobs/in-Toowoomba-&-Darling-Downs-QLD"

# Find jobs on seek and return a list of
def seek_jobs (search_query):
    output = ["Title","Location","Salary","Description","Date listed","Start Date"]

    soup = BeautifulSoup(get(search_query).text, 'html.parser')
    jobs = soup.findAll('article')
    
    for job in jobs:
        pageurl = "https://www.seek.com.au/" + job.find('a',{"data-automation":"jobTitle"}).get('href')
        page = BeautifulSoup(get(pageurl).text, 'html.parser')
        job_info = []

        title = job.find('a',{"data-automation":"jobTitle"}).text
        job_info.append(title)

        try:
            company = job.find('a',{"data-automation":"jobCompany"}).text
        except AttributeError:
            company = "Private Advertisor"
        job_info.append(company)

        location = job.find('a',{"data-automation":"jobLocation"}).text
        job_info.append(location)

        try:
            salary = job.find('span',{"data-automation":"jobSalary"}).span.text
        except:
            salary = "No Listed Salary"
        job_info.append(salary)

        description = job.find('span',{"data-automation":"jobShortDescription"}).span.text
        job_info.append(description)

        listed_date = job.find('span',{"data-automation":"jobListingDate"}).text
        job_info.append(listed_date)
        
        start_date = page.find('dd',{"data-automation":"job-detail-date"}).span.span.text
        job_info.append(start_date)

        output.append(job_info)
    
    return output