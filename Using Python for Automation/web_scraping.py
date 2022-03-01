'''
Written by: Matt Scanlon
Last Updated: 2021-11-15 10:00 AM

Part I of the web scraping instruction from Using Python for Automation in LinkedInLearning
Web Scraping - A popular tool used to collect information from online resources.

HTML - HyperText Markup Language

Three basic steps to web scraping:
    1) GET: Sending a get query to the website. - This returns an html based document containing all information on the website
    2) PARSE: Break down the html to make it more navigable and easier to reach target information
    3) EXTRACTION: Isolate and store target data in desired format
   
Common libraries used for web scraping include:
    - Beutiful Soup
    - lxml
    - requests
'''

#lines for terminal to install appropriate libraries:
    #requests is used for the get query
    #lxml is used for processing the html
    #Beautiful Soup creates a parsed and navigable html library

'''
TO BE INSTALLED VIA THE TERMINAL:
install requests
install lxml
install beautifulsoup4
'''

#will acquire the quote, author, and tags associated with each quote on a website called "Quotes to Scrape" at "quotes.toscrape.com
#Note - chrome inspector tool > right click > inspect allows you to find a ton in the webpage

#Basically we are c

import requests
from bs4 import BeautifulSoup

#GET
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

#PARSE
soup  = BeautifulSoup(response.text, 'lxml') #this line asks BeautifulSoup to parse the responses' text attribute using the lxml parser.
#print(soup)


#EXTRACTION
    #First, inpect the location you would like to extract and inspect it. This will show you the HTML behind that element.
    #In this case, to get each quote, we will look for the "<span class="text" itemprop="text">" line.
    #NOTE: Basic Structure of an HTML website:
        #An HTML - defines the language used
            #A head - defines the header
            #A body - defines the body of the website.
                #A div - a method for sectioning out body elements
                #A span - another method for sectioning out body elements
            
    #typically during web scraping we will be mostly focused on the information in the body section.
    # In order to isolate the data, we will use the find_all function to hone in on the tag and class we specified.

#We will look within the span tag for any class which is text to find all of the quotes on the website
quotes = soup.find_all('span', class_='text')
#print(quotes)

#To just capture the text and exclude the extraneous resulting HTML, we can create a loop to look for just the text within
#each quote.
for quote in quotes:
    print(quote.text)

#Now we will look for the authors of each quote - went to the website and used inspect to find that the authors are contained within
#the small tag with class author
authors = soup.find_all('small',class_='author')
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)

#Get the tags for each quote. We can do this by inspecting the tags. Each quote seems to have multiple tags. So, instead, we should
#try to get the div tag and class='tags' section.
tags = soup.find_all('div',class_='tags')
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a',class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)