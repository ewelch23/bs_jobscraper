from bs4 import BeautifulSoup
import requests
# url = "https://secure.indeed.com/auth?hl=en_US&service=my&co=US&continue=https%3A%2F%2Fwww.indeed.com%2Flogin"
url = "https://www.indeed.com/jobs?q=aerospace+internship+2023&l=&vjk=87773bedbfaecf25"
req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')
## click on a job with the following attributes:
# internship
# summer 2023
# <div class="jcs-JobTitle css-jspxzf eu4oa1w0"
# <div class="jobsearch-LeftPane">

all_jd = soup.find_all("jobDescriptionText", class_="jobsearch-jobDescriptionText")
for jd in all_jd:
    print(jd.get_text(strip=True))