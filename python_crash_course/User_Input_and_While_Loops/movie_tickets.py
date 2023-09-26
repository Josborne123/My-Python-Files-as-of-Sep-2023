age_prompt = "\nPlease enter your age"
age_prompt += "\nEnter 'quit' to exit the program: "

while True:
	age = input(age_prompt)
	
	if age == 'quit':
		break
	
	age = int(age)
	
	if age <= 3:
		print(f"\nYour ticket will cost nothing since you are {age} years old.")
	elif age <= 12:
		print(f"\nYour ticket will cost $10 since you are {age} years old")
	elif age > 12:
		print(f"\nYour ticket will cost $15 since you are {age} years old")