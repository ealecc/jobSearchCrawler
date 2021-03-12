# A beautifulsoup job search webscraper
from bs4 import BeautifulSoup
from requests import get

URL = "https://www.seek.com.au/system-administrator-jobs/in-All-Brisbane-QLD"
DOMAIN = "https://www.seek.com.au/"

# Find jobs on seek and return a list containing job information
def find_all_jobs(url):
    output = ["Title","Location","Salary","Description","Date listed","Start Date"]
    last_page = False
    
    # iterate through pages of results until done
    while not last_page:
        #print("Working on page " + url)

        soup = BeautifulSoup(get(url).text, 'html.parser')
        output.append(find_jobs_on_page(soup))
        
        try:
            url = DOMAIN + soup.find('a',{"data-automation":"page-next"}).get('href')
        except AttributeError:
            last_page = True
    
    return output

# Given a soup of one SEEK page, return a list of job info
def find_jobs_on_page(soup):
    jobs = soup.findAll('article')
    page_info = []
    
    for job in jobs:
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
        except AttributeError:
            salary = "No Listed Salary"
        job_info.append(salary)

        description = job.find('span',{"data-automation":"jobShortDescription"}).span.text
        job_info.append(description)

        try:
            listed_date = job.find('span',{"data-automation":"jobListingDate"}).text
        except AttributeError:
            listed_date = "No listed date"
        job_info.append(listed_date)

        page_info.append(job_info)
    
    return page_info

def main():
    print(find_all_jobs(URL))

if __name__ == "__main__":
    main()