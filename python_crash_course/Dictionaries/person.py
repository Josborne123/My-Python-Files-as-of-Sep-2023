peoples = []

mum = {'first_name': 'fiona', 'last_name': 'osborne', 'age': 48, 'city': 'milngavie', 'best': 'best'}
peoples.append(mum)

james =  {'first_name': 'james', 'last_name': 'osborne', 'age': 17, 'city': 'milngavie', 'best': 'smelly'}
peoples.append(james)

dad =  {'first_name': 'kenneth', 'last_name': 'osborne', 'age': 51, 'city': 'milngavie', 'best': 'amazing'}
peoples.append(dad)

for people in peoples:
	print(f"First name is {people['first_name'].title()}, Second name is {people['last_name'].title()}. They live in {people['city']}, They are the {people['best']}.")