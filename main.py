import requests
import selectorlib
import datetime
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

connection = sqlite3.connect("data.db")

def scrape(url):
    response = requests.get(url) # Scraping the webpage of the url
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["home"]
    return value

def store(extracted):
    now = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data VALUES(?, ?)", (now, extracted))
    connection.commit()

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)




