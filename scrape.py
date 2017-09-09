import os
import requests

from bs4 import BeautifulSoup

# Scrape website for pdf
def scrape():
    result = ''
    html = requests.get('http://www.oslobors.no/Oslo-Boers/Notering/Aksjer-egenkapitalbevis-og-retter-til-aksjer/Oslo-Boers-og-Oslo-Axess/Noterte-selskapers-hjemstat').text
    bs = BeautifulSoup(html)

    for link in bs.find_all('a'):
        if (link.has_attr('href')):
            l = link.attrs['href']
            if ('.pdf' in l):
                result = 'http://www.oslobors.no' + link.attrs['href']

    return result


# Check if pdf is new
def status(url):
    file = r'data/url.txt'

    # If file does not exist
    if not os.path.exists(file):
        f = open(file, 'w')
        f.write(url)
        f.close()
        return True

    # if file does exist
    else:
        content = ''
        with open(file, 'r') as f:
            content = f.readline()

        # If url is new
        if (content != url):
            f = open(file, 'w')
            f.write(url)
            f.close()
            return True

        # If url is old
        else:
            return False


#  Download pdf
def download(url):
    file = r'data/pdf/aksjer.pdf'
    r = requests.get(url, stream=True)

    with open(file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return file