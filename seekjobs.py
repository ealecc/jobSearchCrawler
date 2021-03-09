# A beautifulsoup job search webscraper
from bs4 import BeautifulSoup
from requests import get

url = "https://www.seek.com.au/system-administrator-jobs/in-Toowoomba-&-Darling-Downs-QLD"
soup = BeautifulSoup(get(url).text, 'html.parser')

jobs = soup.findAll('article')

def find_attribute (object, tag, data):
    try:
        out = object.find(tag,{"data-automation":data}).text
    except AttributeError:
        return "Null"
    except:
        return "!!!Unknown error!!!"
    
    return out

# Find and print Seek listings
for job in jobs:
    pageurl = "https://www.seek.com.au/" + job.find('a',{"data-automation":"jobTitle"}).get('href')
    result = []

    result.append(find_attribute(job, 'a', "jobTitle"))
    result.append(find_attribute(job, 'a', "jobCompany"))
    result.append(find_attribute(job, 'a', "jobLocation"))
    result.append(find_attribute(job, 'a', "jobClassification"))
    result.append(find_attribute(job, 'span', "subClassification"))
    result.append(find_attribute(job, 'span', "jobShortDescription").replace('\n',''))

    print("\t".join(result))