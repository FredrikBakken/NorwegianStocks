'''
What data is relevant to store?

TABLE STOCKS
STOCK NAME | STOCK TICKER
'''

from tinydb import TinyDB, where
db = TinyDB('db/db.json')

# Insert into database
def db_insert(name, ticker):
    exist = db_search_ticker(ticker)
    if not exist:
        before = len(db)
        db.insert({'name': name, 'ticker': ticker})
        after = len(db)

        if (after > before):
            print("insert: success")
            return True
        else:
            print("insert: failure")
            return False
    else:
        print("insert: already exist")
        return False


# Delete from database
def db_delete(ticker):
    exist = db_search_ticker(ticker)
    if exist:
        before = len(db)
        db.remove(where('ticker') == ticker)
        after = len(db)

        if (before > after):
            print("delete: success")
            return True
        else:
            print("delete: failure")
            return False
    else:
        print("delete: does not exist")
        return False


# Search name in database
def db_search_name(name):
    result = db.search(where('name') == name)
    return result


# Search ticker in database
def db_search_ticker(ticker):
    result = db.search(where('ticker') == ticker)
    return result