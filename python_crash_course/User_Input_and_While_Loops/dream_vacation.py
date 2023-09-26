prompt = "If you could visit one place in the world where would it be? "

# Creating empty list to store the places that the user enters.
places = []

polling_active = True

while polling_active:
	response = input(prompt)
	# Adding the users response the the list places
	places.append(response)

	# Asking if the user would like to enter another response
	repeat = input("Would you like to post another response (yes/no)? ")
	# If the user types no then you exit the while loop. If the user types anything else the loop will begin again.
	if repeat == 'no':
		break

# Print The poll results
print(f"And the results are in, drum roll please")
print("\n-----POLLING RESULTS-----")

for place in places:
	print(f"The user would like to visit {place.title()}")	
		
