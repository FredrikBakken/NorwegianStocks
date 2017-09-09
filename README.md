# NorwegianStocks

NorwegianStocks is a tiny Python-script used for testing of event handling of .pdf documents with tabula-py, for scraping table contents. The script takes the latest .pdf of all norwegian stocks on Oslo Børs and scrapes all contents from the table into a .csv file, before storing the stock names and tickers into a NoSQL database, tinyDB.

## How to Use

The script is very easy to use. Make sure to have Python 2.7 installed and configured correctly before running the script.

### Libraries
 - py -2.7 -m pip install BeautifulSoup
 - py -2.7 -m pip install tinydb
 - py -2.7 -m pip install tabula-py

### Run
Download the project and run: py -2.7 main.py
