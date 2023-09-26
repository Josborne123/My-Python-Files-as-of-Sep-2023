def city_country(city, country):
	city_country = f"{city}, {country}"
	return city_country


c_country = city_country('glasgow', 'scotland').title()	
print(c_country)

c_country = city_country('bled', 'slovenia').title()
print(c_country)

c_country = city_country('piran', 'slovenia').title()
print(c_country)