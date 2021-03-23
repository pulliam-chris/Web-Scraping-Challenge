# Web-Scraping-Challenge
Use BeautifulSoup &amp; Splinter to scrape the NASA Mars News Site then use MongoDB and Flask to apply data to a webpage

## Primary Files
* mission_to_mars.ipynb (Jupyter Notebook scraping process)
* app.py (Flask local server)
* scrape_mars.py (Scrape function)
* templates/index.html (HTML Homepage)

## Part 1

* NASA Mars News (BeautifulSoup)
* JPL Mars Space Images - Featured Image (Splinter)
* Mars Facts (BeautifulSoup)
* Mars Hemispheres (Splinter)

## Part 2

![Index.html](https://github.com/pulliam-chris/Web-Scraping-Challenge/blob/main/images/index.JPG "Index.html")

**_Had issues with the Chrome driver particular to flask that I was unable to resolve locally_**
![Selenium Error](https://github.com/pulliam-chris/Web-Scraping-Challenge/blob/main/images/flask.JPG "Selenium Error")

* Flask Live Server - the website functions and attempts the data scrape on the button click.
![Flask](https://github.com/pulliam-chris/Web-Scraping-Challenge/blob/main/images/flask.JPG "Flask")
* PyMongo DB (mars.marsinfo) - data is commited to the database after being scraped.
![PyMongo](https://github.com/pulliam-chris/Web-Scraping-Challenge/blob/main/images/mongo.JPG "PyMongo")
* Data Scrape - Data collection does not include the JPL Mars Space Images or Mars Hemisphere captures performed by splinter due to the error.







