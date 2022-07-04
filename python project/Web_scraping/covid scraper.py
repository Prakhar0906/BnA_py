from bs4 import BeautifulSoup
import requests

html_text= requests.get('https://www.worldometers.info/coronavirus/country/india').text
Soup= BeautifulSoup(html_text, 'lxml')
cases= Soup.find_all('div', {'id':'maincounter-wrap'})
for i in cases:
    try:
        typ= i.find('h1').text#This will find the name of data  
        num= i.find('span').text# this will find the value 
        print(typ,num)
    except:
        pass

