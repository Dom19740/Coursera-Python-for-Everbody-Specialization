import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1761515.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the anchor tags
tags = soup('span')

# Initialize a variable to store the sum of integers from span tags
total_sum = 0

for tag in tags:
    try:
        # Get the text content of the span tag
        text_content = tag.contents[0].strip()

        # Convert the text content to an integer and add it to the total_sum
        number = int(text_content)
        total_sum += number
    except (ValueError, IndexError):
        # If the span tag does not contain a valid integer, ignore it
        pass

print("Sum of integers from span tags:", total_sum)