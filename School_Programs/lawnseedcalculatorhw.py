lawnLength = float(input("Enter lawn length: "))
lawnBreadth = float(input("Enter lawn breadth: "))
area = lawnLength * lawnBreadth
lawnSeed = int

print("Please select your lawn use from the following options") 

print("Enter 'A' if your lawn will be used for chlidren's play")
print("Enter ‘B’ if your lawn will be used for general use")
print("Enter ‘C’ if your lawn will be purely ornamental")
lawnUse = str(input("").lower())

if lawnUse == "a":
	lawnSeed = 50 * area
elif lawnUse == "b":
	lawnSeed = 40 * area
elif lawnUse == "c":
	lawnSeed = 25 * area

print(str(lawnSeed) + " grams is of lawn seed is required") 