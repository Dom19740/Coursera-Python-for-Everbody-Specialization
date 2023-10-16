import urllib.request, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1761518.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

results = json.loads(data)

total_count = 0  # Initialize a variable to store the total count

for item in results['comments']:
    name = item['name']
    count_text = item['count']

    # Extract and convert the numbers from the 'count' text
    try:
        count = int(count_text)
        total_count += count  # Add the count to the total_count
    except ValueError:
        print("Error converting count for", name)

    print('Name:', name)
    print('Comment Count:', count_text)

print('Sum of Comment Counts:', total_count)