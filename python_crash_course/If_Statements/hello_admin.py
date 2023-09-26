users = []

if users:
	for user in users:
		if user == 'admin':
			print("Hello Admin, would you like to see a status")
		elif user != 'admin':
			print(f"Welcome to my site {user.title()}.")
else:
	print("We need to find some users")