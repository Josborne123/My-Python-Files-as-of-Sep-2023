def sandwich(*items):
	print("\nI will add the following items to your sandwich")
	for item in items:
		print(f"-{item}")

sandwich('ham', 'lettuce')
sandwich('peperoni')
sandwich('chicken', 'cheese', 'cucumber')