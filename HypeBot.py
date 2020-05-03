from html.parser import HTMLParser
from urllib.request import urlopen
import ssl


def start(page_url):
    try:
        # ssl certs, CERT_NONE is the default
        gcontext = ssl.SSLContext()
        page = urlopen(page_url, context=gcontext)
        # check if the content is html, and retrieve it
        if 'text/html' in page.getheader('Content-Type'):
            html_bytes = page.read()
            html_string = html_bytes.decode('utf-8')
            print(html_string)
    except Exception as e:
        print(e)
    print('finished fetching')


start('https://www.nike.com/launch')