def build_person(first_name, last_name, age=None, year_born=None):
	""" Return a dictionary of information about a person. """
	person = {'first': first_name, 'last': last_name,}
	if age:
		person['age'] = age

	if year_born:
		person['year_born'] = 2005

	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

musician2 = build_person('john', 'osborne', year_born=2005)
print(musician2)