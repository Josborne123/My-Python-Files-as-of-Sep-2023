current_users = ['john', 'james', 'Fiona', 'kenneth', 'simon']

new_users = ['john', 'fiona', 'jimmy', 'alex', 'lewis']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
	if user in current_users:
		print(f"Sorry {user} that username is taken.")
	else:
		print(f"That username is availabe {user}.")
	