noOfDoors = int(input("How many doors would you like to order: "))


doorLength = float(input("Enter door length: "))
doorHeight = float(input("Enter door height: "))
paneLength = float(input("Enter pane length: "))
paneHeight = float(input("Enter pane height: "))

paneLength += 1
paneHeight += 1

doorArea = doorHeight * doorLength
paneArea = paneHeight * paneLength

paneNumber = (doorArea / paneArea) * noOfDoors

print("The number of panes of glass needed is " + str(paneNumber))