# https://github.com/chezou/tabula-py

from tabula import convert_into
from db import db_insert, db_search_ticker

def covert_pdf():
    convert_into("data/pdf/aksjer.pdf", "data/csv/aksjer.csv", output_format="csv", pages="all", encoding="utf-8")
    return True

def store_stocks():
    f = open('data/csv/aksjer.csv', 'rU')

    lines = f.readlines()[2:]
    for line in lines:
        cells = line.split(",")
        ticker = cells[0].decode("utf-8", "ignore")
        name = cells[1].decode("utf-8", "ignore")

        exist_ticker = db_search_ticker(ticker)

        if not exist_ticker:
            db_insert(name, ticker)

    f.close()

    return True