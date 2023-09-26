favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

should_take_poll = ['fiona', 'john', 'phil', 'sarah', 'kenneth']

for person in should_take_poll:
	if person in favourite_languages:
		print(f"Thanks for taking the poll, {person.title()}")
	else:
		print(f"{person.title()}, please take the poll")