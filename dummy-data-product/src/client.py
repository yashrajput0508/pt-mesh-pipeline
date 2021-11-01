from ADB-main.dummy-data-product.src.dependencies.scraping import scraper
from ADB-main.dummy-data-product.src.dependencies.cleaning import cleaner

class client:
    def __init__(self):
        pass

    def clean(self):
        # it can clean the data
        cleaner.clean()

    def scrap(self):
        # it can take data from url and save as json
        scraper.scrap()

if __name__ == "__main__":
    client = client()
    client.scrap()
    client.clean()
