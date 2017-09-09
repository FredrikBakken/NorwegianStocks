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
            return True
        else:
            return False
    else:
        return False


# Delete from database
def db_delete(ticker):
    exist = db_search_ticker(ticker)
    if exist:
        before = len(db)
        db.remove(where('ticker') == ticker)
        after = len(db)

        if (before > after):
            return True
        else:
            return False
    else:
        return False


# Search name in database
def db_search_name(name):
    result = db.search(where('name') == name)
    return result


# Search ticker in database
def db_search_ticker(ticker):
    result = db.search(where('ticker') == ticker)
    return result