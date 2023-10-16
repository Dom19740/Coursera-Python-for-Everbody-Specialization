import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

todo = list()
visited = list()
url = input('Enter starting URL - ')
todo.append(url)

position = int(input('Enter the position - '))
repeats = int(input('Enter the number of repeats - '))

while len(todo) > 0 and repeats > 0:

    url = todo.pop()
    repeats -= 1

    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print("*** Error in retrieval")
        continue

    soup = BeautifulSoup(html, 'html.parser')
    visited.append(url)

    # Retrieve all the anchor tags
    tags = soup('a')
    count = 0
    for tag in tags:
        newurl = tag.get('href', None)
        if newurl is not None:
            count += 1
            if count == position:
                todo.append(newurl)
                break

# Display the final page link
if len(todo) > 0:
    print("Final page link:", todo[-1])
else:
    print("No more links to follow.")
