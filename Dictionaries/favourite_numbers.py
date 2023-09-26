fav_numbers = {
	'mum': [16, 86, 54 ,43], 
	'dad': [78, 54, 90, 67, 89,], 
	'john': [8, 4, 3, 12,], 
	'james': [55, 44 , 23, 64,]
	}

for name, numbers in fav_numbers.items():
	print(f"{name.title()}'s favourite numbers are:")
	for number in numbers:
		print(number)