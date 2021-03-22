from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import os
#import pymongo

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
#conn = 'mongodb://localhost:27017'
#client = pymongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
#db = client.marsinfo

#def init_browser():
    # Replace the path with your actual path to the chromedriver
    #executable_path = {"executable_path": "C:/Users/mrpar/.wdm/drivers/chromedriver/win32/89.0.4389.23"}
    #ChromeDriverManager().install()
    # "C:/Users/mrpar/.wdm/drivers/chromedriver/win32/89.0.4389.23"
    # "C:/Users/mrpar/Documents/bootcamp/chromedriver/"
    #return Browser("chrome", **executable_path, headless=True)

def scrape():

    marsinfo = {}
    #executable_path = {"executable_path": "C:/Users/mrpar/Documents/bootcamp/chromedriver"}
    #browser = Browser("chrome", **executable_path, headless=True)

    #base_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    #browser.visit(base_url)
    #time.sleep(1)

    #html = browser.html
    #soup = bs(html, 'html.parser')
    #image_location = ""

    #for i in soup.find_all('img', class_='headerimage fade-in'):
        #image_location = (i.get('src'))

    #featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + image_location

    #db.classroom.insert_one({'featured_image_url' : featured_image_url})

    #marsinfo = {'featured_image_url' : featured_image_url}

    url = "https://mars.nasa.gov/news"
    html = requests.get(url).text

    # Create a Beautiful Soup object
    soup = bs(html, 'html.parser')

    allTitleElements = soup.find_all('div', class_='content_title')

    # A blank list to hold the headlines
    newsTitles = []
    # Loop over div elementsz
    for element in allTitleElements:
        # If element has an anchor...
        if (element.a):
            # And the anchor has non-blank text...
            if (element.a.text):
                # Append the td to the list
                newsTitles.append(element)

    allParElements = soup.find_all('div', class_='rollover_description_inner')

    # A blank list to hold the descriptions
    newsParagraphs = []
    # Loop over div elements
    for element in allParElements:
        # And the element has non-blank text...
        if (element.text):
            # Append the text to the list
            newsParagraphs.append(element)

    #Construct Dictionary of Title w/ Paragraph
    #headlines = []

    #for i in range(len(newsTitles)):
    package = {}
    package['news_title'] = newsTitles[0].text.strip()
    package['news_p'] = newsParagraphs[0].text.strip()
    #headlines.append(package)
    marsinfo = package



    # Read HTML from website
    url = "https://space-facts.com/mars/"
    html = requests.get(url).text

    # Create a Beautiful Soup object
    soup = bs(html, 'html.parser')

    tableRows = []
    html = soup.find(id='tablepress-p-mars-no-2')
    justData = html.find_all('td')

    for r in justData:
        c1 = r.text
        tableRows.append(c1)

    for t in range(len(tableRows)-1):
        package = {}
        if t % 2 == 0:
            package[tableRows[t]] = tableRows[t+1]
            #t += 2
            marsinfo.update(package)



    return marsinfo
