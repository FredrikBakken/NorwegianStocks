from db import db_delete, db_insert, db_search_ticker

from reader import covert_pdf, store_stocks

from scrape import download, scrape, status


def init():
    # Scrape pdf and check age
    url = scrape()
    s = status(url)

    if s:
        # Download pdf
        download(url)

        # Convert pdf to csv
        covert_pdf()

        # Csv data to tinydb
        store_stocks()

if __name__ == "__main__":
    init()