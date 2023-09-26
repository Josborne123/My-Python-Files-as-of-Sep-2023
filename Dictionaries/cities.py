cities = {
	'glasgow': {
		'country': 'scotland',
		'population': 598830,
		'fact': 'I live here',
		},
	'edinburugh': {
		'country': 'scotland',
		'population': 482005,
		'fact': 'This is the capital of Scotland',	
		},
	'aberdeen': {
		'country': 'scotland',
		'population': 207932,
		'fact': "Home to Scotland's oldest daily newspaper"	
	} 
}

for city, info in cities.items():
	print(f"\nCountry: {info['country'].title()}.")
	print(f"Population: {info['population']}.")
	print(f"Fact: {info['fact']}.")