signalstrength = [0] * 5
pattern = ""

for index in range(5):
    signalstrength[index] = int(input("Please enter a reading from 0 to 100 "))

    while signalstrength[index] < 0 or signalstrength[index] > 100:
        print("Invalid Input. Enter again")
        signalstrength[index] = int(input("Please enter a reading from 0 to 100 "))

    signalstrength[index] = round(signalstrength[index]) 

    if signalstrength[index] > 80:
        pattern += "S"
    elif signalstrength[index] < 30:
        pattern += "P"
    else:
        pattern += "M"


print("The signal pattern is " + pattern)

for index in range(5):
    print("Reading " + str((index + 1)) + " " + " - " + str(signalstrength[index]))