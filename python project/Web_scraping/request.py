from bs4 import BeautifulSoup
import requests
#1 request the page url
#2 Soup it out
#3 use .find('tag', 'class')
#4 fors and ifs in
#5 Print Pretty
unwanted_skills= input("Enter the skills you do not have>")
print(f"Filtering {unwanted_skills}")

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
Soup= BeautifulSoup(html_text, 'lxml')
jobs= Soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    date= job.find('span', class_= 'sim-posted').span.text
    if 'few' in date:
        company_name= job.find('h3', class_='joblist-comp-name').text.replace(' ','')
        skills= job.find('span', class_= 'srp-skills').text.replace(' ','')
        link= job.header.h2.a['href']
        if unwanted_skills not in skills:            
            print(f"Company Name:{company_name.strip()}")
            print(f"Requires skills: {skills.strip()}")
            print(f"Link:{link}")
            print()
            
