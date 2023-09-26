import random

rpc = ['rock', 'paper', 'scissors']

print("You have 3 options: rock, paper, scissors.")

user_score = 0
comp_score = 0

while True:
	user_choice = str(input("Please enter your choice: "))
	comp_choice = random.choice(rpc)

	if user_choice == 'rock' and comp_choice == 'rock' or user_choice == 'paper' and comp_choice == 'paper' or user_choice == 'scissors' and comp_choice == 'scissors':
		print(f"\n{user_choice} VS {comp_choice}")
		print("\nDraw")
			
	elif user_choice == 'paper' and comp_choice == 'rock' or comp_choice == 'paper' and user_choice == 'rock':
		print(f"\n{user_choice} VS {comp_choice}")
		print("\nPaper wins!")
		if user_choice == 'paper':
			print('\nUser wins')
			user_score += 1
		elif comp_choice == 'paper':
			print("Computer wins")	
			comp_score += 1

	elif user_choice == 'rock' and comp_choice == 'scissors' or comp_choice == 'rock' and user_choice == 'scissors':
		print(f"\n{user_choice} VS {comp_choice}")
		print("\nRock wins!")
		if user_choice == 'rock':
			print('\nUser wins')
			user_score += 1
		elif comp_choice == 'rock':
			print("Computer wins")	
			comp_score += 1

	elif user_choice == 'scissors' and comp_choice == 'paper' or comp_choice == 'scissors' and user_choice == 'paper':
		print(f"\n{user_choice} VS {comp_choice}")
		print("\nScissors wins!")
		if user_choice == 'scissors':
			print('\nUser wins')
			user_score += 1
		elif comp_choice == 'scissors':
			print("Computer wins")	
			comp_score += 1

	print("\nWould you like to play again (Yes/No)")
	answer = input()
	if answer == 'no':
		break	

print(f"User score is {user_score}")
print(f"Computer score is {comp_score}")
if user_score > comp_score:
	print("User wins!")
elif comp_score > user_score:
	print("Computer wins!")	
elif user_score == comp_score:
	print("Draw")	

print("Thanks for playing")



