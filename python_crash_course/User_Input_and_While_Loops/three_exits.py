prompt = "\nPlease type in what toppings you would like"
prompt += "\nEnter 'quit' if you want to exit the program: "

active = True

while active:
	topping = input(prompt)

	if topping == 'quit':
		active = False
	else:
		print(f"\nI will add {topping} to your pizza")	