from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")

@app.route("/")
def index():
    marsinfo = mongo.db.marsinfo.find_one()
    return render_template("index.html", marsinfo=marsinfo)


@app.route("/scrape")
def scraper():
    marsinfo = mongo.db.marsinfo
    mars_data = scrape_mars.scrape()
    # Insert scraped data
    marsinfo.update({}, mars_data, upsert=True)
    return redirect(url_for('index'), code=302)


if __name__ == "__main__":
    app.run(debug=True)
