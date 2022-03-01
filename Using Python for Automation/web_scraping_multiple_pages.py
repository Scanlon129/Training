'''
Written by: Matt Scanlon
Last Updated: 2021-11-15 10:00 AM

Part II of the web scraping instruction from Using Python for Automation in LinkedInLearning

This is a tutorial for scraping webpage information off of multiple pages
'''

#Import Packages-----------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests

#Set Definitions-----------------------------------------------------------------------------------
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#Program Logic-------------------------------------------------------------------------------------

'''
First we will set up a loop to get specific elements found on a single page and print them.
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    itemName = i.find('h4', class_='card-title').text.strip('\n') # .strip('\n') removes the carriage return
    itemPrice = i.find('h5').text
    print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1
'''

#Next we will loop through each page.
pages = soup.find('ul',class_='pagination')
urls = []
links = pages.find_all('a',class_='page-link')

#This loop will store each page's url
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
#print(urls)

#This will iterate between urls and return the list of values that we were looking for on each page.
count = 1
for i in urls:
    newURL = url + i
    response = requests.get(newURL)
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n') # .strip('\n') removes the carriage return
        itemPrice = i.find('h5').text
        print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1