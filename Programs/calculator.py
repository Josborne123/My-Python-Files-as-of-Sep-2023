calc = int(input("Enter your first number: "))
calc2 = int(input("Enter your second number: "))

do = input("What would you like to do with these numbers? add(+), subtract(-), divide(/), times(*) / (x): ")

if do == "add" or do == "+":
	print(calc * calc2)

if do == "subtract" or do == "-":
	print(calc - calc2)

if do == "divide" or do == "/":
	print(calc / calc2)

if do == "times" or do == "*" or do == "x":
	print(calc * calc2)		
