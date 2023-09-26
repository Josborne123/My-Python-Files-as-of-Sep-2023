sandwich_orders = ['veggie', 'grilled cheese', 'pastrami', 'turkey', 'pastrami', 'roast beef', 'pastrami']
finished_sandwiches = []

print(f"Sorry we have run out of {sandwich_orders[2]}")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
	print("I made a " + sandwich + " sandwich.")

print(sandwich_orders)
print(finished_sandwiches)