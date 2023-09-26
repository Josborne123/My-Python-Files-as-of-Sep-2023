import random

# Open a file called passwordAnduse.txt, if the file has not been created it will create the file
file = open('passwordAndUse.txt', 'a')

# Create a string of characters for the passwords
chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@'

# Ask the user how many passwords they want to generate
numOfPassword = int(input("How many passwords do you want to generate? "))



# If the user only wants to generate 1 password go into this if statement
if numOfPassword == 1:
	passwordUse = input("\nWhat is this password going to be used for? ")
	lengthOfPassword = int(input("\nWhat do you want the length of your password to be? "))
	# Loop through numOfPassword and re-assign the password variable each time
	for num in range(numOfPassword):
		password = ''
	# Loop through lenghOfPassword and randomly generate a passoword of the users specifications
		for p in range(lengthOfPassword):
			password += random.choice(chars)
	# num += 1 is so that when I print which number each password it is it won't start on 0, it will start on 1
	num += 1
	# print "Password" + which number the password is + "--" + the actual password
	print("\nPassword " + str(num) + " -- " + password)
	#Open the file and store the password in it and the password use
	file.write("\n" + str(password) + " is used for " + str(passwordUse))
	# Quit the program so that it doesn't execute anything else
	quit()



# If the user want to generate more than 1 password it will run this section of code instead

lengthOfPassword = int(input("\nWhat do you want the length of your password to be? "))


for num in range(numOfPassword):
	password = ''
	for p in range(lengthOfPassword):
		password += random.choice(chars)

	num += 1
	print("\nPassword " + str(num) + " -- " + password)	



# Thank you!