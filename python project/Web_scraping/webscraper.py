from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content= html_file.read()
    #1 first open file as
    #2 create the file object as read
    #3 soup it
    #4 find all
    
    soup= BeautifulSoup(content, 'lxml')
    courses_card= soup.find_all('div', class_='card')
    for course in courses_card:
        course_name= course.h5.text
        course_price= course.a.text.split()[-1]
        print(f'{course_name} cost {course_price}')

