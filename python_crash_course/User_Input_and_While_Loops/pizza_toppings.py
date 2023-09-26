prompt = "\nPlease type in what toppings you would like"
prompt += "\nEnter 'quit' if you want to exit the program: "

while True:
	topping = input(prompt)

	if topping != 'quit':
		print(f"\nI will add {topping} to your pizza")
	else:
		break