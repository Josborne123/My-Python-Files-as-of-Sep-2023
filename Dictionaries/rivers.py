rivers = {
	'nile': 'egypt',
	'mississippi': 'america',
	'volga': 'russia'
	}
# Loop through and print the key value pairs
for river, country in rivers.items():
	print(f"The {river.title()} river is in {country.title()}")	

print()

# Loop through and print the keys
for river in rivers.keys():
	print(river.title())

print()

# Loop through and print the value
for country in rivers.values():
	print(country.title())

