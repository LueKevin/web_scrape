import urllib.request
import time
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            print("\n" + url)
            time.sleep(60)
           
scrape = Scraper('https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en')
scrape.scrape()
