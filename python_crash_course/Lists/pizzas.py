pizzas = ['margarita', 'pepperoni', 'pineapple']
for pizza in pizzas:
	print(f"I like {pizza.title()}")
print("I just really like pizza")	

friend_pizzas = pizzas[:]

pizzas.append("kiwi")
friend_pizzas.append("ham")

print("My favourite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friends favourite pizzas are:")
for friend in friend_pizzas:
	print(friend)	