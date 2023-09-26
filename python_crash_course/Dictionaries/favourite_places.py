favourite_places = {
	'mum': ['hong kong', 'orkney'],
	'dad': ['slovenia', 'the alps', 'scotland highlands'],
	'james': ['hong kong'],
	}

for name, places in favourite_places.items():
	print("\n" + name.title() + " likes the following places")
	for place in places:
		print(place.title())

