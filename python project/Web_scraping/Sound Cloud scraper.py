from bs4 import BeautifulSoup
import requests
#Sound cloud web scraper
#The link is default
#First find all the tags in list
#pick all indivisually with for loop
#https://soundcloud.com/search?q=ehrling
search= input("Enter the artist:")
link='https://soundcloud.com/search?q='+search
print()
print(f"Searching Link-{link}")
print()
html_text= requests.get(link).text
Soup= BeautifulSoup(html_text, 'lxml')
Songs= Soup.find_all('li')
print("Showing top 8 results")
print()
for song in Songs:
    name= song.find('a').text #Look for the link because name is as a link and get the name by .text
    if 'Search' not in name : # if search is not in name it is a song
        print(name)#Print the song Name
        link= song.a['href'] #get the link
        print(f"Link-{'https://soundcloud.com'+link}") #combine link with the website
        print()
