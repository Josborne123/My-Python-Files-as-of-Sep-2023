# Creating an empty list to store the dictionarys in
pets = []

# Creating a dictionary called ken
ken = {
	'dog': 'golden retriever',
	'owner': 'john',
	}
# Adding ken to the list pets
pets.append(ken)

# Creating a dictionary called fifi
fifi = {
	'dog': 'labrador',
	'owner': 'fiona',
	}
# Adding fifi to the list pets
pets.append(fifi)

for pet in pets:
	print("Here is some information about the pets")
	for key, value in pet.items():
		print(key.title() + " : " + value.title())