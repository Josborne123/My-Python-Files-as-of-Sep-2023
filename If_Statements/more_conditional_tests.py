laptop = 'macbook'
print(laptop == 'dell')
print(laptop == 'macbook')

phone = 'Honor Play'
print(phone.lower() == 'honor play')

fav_number = 8
if fav_number < 9:
	print("My favourite number is less than nine")
if fav_number > 11:
	print("My favourite number is greater than eleven")

print(fav_number >= 7 and fav_number <= 11)
print(fav_number >= 67 and fav_number >= 8)
print(fav_number >= 7 or fav_number <= 11)
print(fav_number >= 67 or fav_number >= 8)
print(fav_number > 14 or fav_number <= 6)

users = ['John', 'Kenneth', 'Fiona', 'James']
user = 'John'
if user in users:
	print("Welcome to the party pal")
user2 = 'Jimmy'
if user2 not in users:
	print("Sorry pal you can't come into the party")