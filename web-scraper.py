import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.pinterest.com/eliseizzle/art/'




r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find_all('img')

for image in images:
    name = image['alt']
    link =image['src']
    with open(name.replace(' ', '-').replace('/', '').replace('|', '') + '.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)
