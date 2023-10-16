import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = 'http://dr-chuck.com/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
