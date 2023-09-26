import requests
from bs4 import BeautifulSoup

URL = 'https://www.y1hockey.com/collections/low-bow'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='low-bow')

sticks = results.find_all('main', class_='main-content')

for stick in sticks:
	stick_name = stick.find('span', class_='grid-product__title')
	stick_price = stick.find('span', class_='grid-product__price-wrap')
	if None in (stick_name, stick_price):
		continue
	print(stick_name.text.strip())
	print(stick_price.text.strip())