import requests
import selectorlib
import streamlit
import datetime

URL = "https://programmer100.pythonanywhere.com/"

def scrape(url):
    response = requests.get(url) # Scraping the webpage of the url
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["home"]
    return value

def store(extracted):
    with open("data.txt", "a") as file:
        file.write(str(datetime.datetime.now()) + "," + extracted + "\n")

def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)


