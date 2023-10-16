import urllib.request, urllib.parse, urllib.error
import collections
from bs4 import BeautifulSoup
import ssl
collections.Callable = collections.abc.Callable

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://dr-chuck.com/'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
