#from splinter import Browser
from bs4 import BeautifulSoup as bs
#from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import requests
import time
import os

def scrape():

    # Singular appended dictionary to be returned at the end of the function
    marsinfo = {}

    # Define the path the selenium driver used instead of splinter (which wouldn't function with flask)
    executable_path = {"executable_path": "C:/Users/mrpar/.conda/envs/PythonData/Lib/site-packages/selenium/webdriver/common"}
    browser = webdriver.Chrome('C:\\Users\\mrpar\\Documents\\bootcamp\\chromedriver\\chromedriver.exe')

    # JPL Mars Space Images - Featured Image
    base_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.get(base_url)
    time.sleep(1)

    image_location = ""
    featured_image_url = ""

    image_locations = browser.find_elements_by_css_selector('img.headerimage fade-in')
    for i in image_locations:
        image_location = (i.get('src'))

    featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + image_location
    
    # Add to dictionary
    package = {}
    package['featured_image_url'] = featured_image_url
    marsinfo.update(package)

    browser.close()
    
    # NASA Mars News
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

    # Package the news
    package = {}
    package['news_title'] = newsTitles[0].text.strip()
    package['news_p'] = newsParagraphs[0].text.strip()
    marsinfo = package

    # Mars Facts
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

    # Return compiled dictionary to be loaded into PyMongo
    return marsinfo
