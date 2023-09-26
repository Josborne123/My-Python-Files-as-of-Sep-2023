import time

def room_a():
	while True:
		print("\nYou have come across an armoured skeleton with a great sword!")
		room_a_weapon_choice = input("\nYou have a choice of three weapons: A(bow and arrow), B(fireball), C(great sword): ")
		if room_a_weapon_choice == "A".lower():
			print("\nBow and arrow equipped.")
			time.sleep(2.5)
			print('\n"Hehehehe, you really think you can beat ME with a bow and arrow. You are more stupid than I thought.", says the Armoured Skeleton in a menacing voice.')
			time.sleep(2.5)
			print(f"\n{name.title()} draws and looses the arrow, the arrow soars through the sky and hits the skeleton straight in the chest. But the armour is too strong for the flimsy arrow and just bounces off.")
			time.sleep(2.5)
			print("\n'Hahaha', says the skeleton.")
			time.sleep(2.5)
			print("\nThe skeleton starts running towards you and lifts his great sword and slays you with the might of a thousand thors.")
			time.sleep(2.5)
			print("\nYOU DIED!!")
			re_try = input("\nWould you like to re-try this room? (yes), (no): ")
			if re_try == 'yes':
				continue
			elif re_try == 'no':
				print("Thanks for playing.")
				break	

		elif room_a_weapon_choice == "B".lower():
			print("\nFireball equipped")
			time.sleep(2.5)
			print(f"\n'I will defeat you!', says {name.title()}.")
			time.sleep(2.5)
			print("\n'I cannot be destroyed you fool!', exclaimed the skeleton.")
			time.sleep(2.5)
			print("\ncharging fireball --- charging fireball")
			time.sleep(2.5)
			print(f"\nThe armoured skeleton started to have a worried look on his face as {name.title()} charged his fireball")
			time.sleep(2.5)
			print(f"\nAaaahhhhhh, {name.title()} shouts as he throws his fireball at the armoured skeleton.")
			time.sleep(2.5)
			print(f"\n'Nooooooo, you have destroyed me. I will return stronger than ever', screams the ghost of the skeleton")
			time.sleep(2.5)
			print(f"\nWell Done {name.title()}. You have defeated the armoured skeleton and passed room A.")
			break
			
		elif room_a_weapon_choice == "C".lower():
			print("\nGreat sword equipped")
			time.sleep(2.5)
			print(f"\nAs {name.title()} pulls out his great sword, the skeleton laughs as it says 'You really think you can beat me with my own weapon. FOOL!' ")
			time.sleep(2.5)
			print(f"\n{name.title()} has engaged in a sword fight with the giant skeleton.")
			time.sleep(2.5)
			print(f"\n{name.title()} is trying to harm the skeleton but his armour is too strong and {name.title()} can not reach the skeletons head as he is much taller.")
			time.sleep(2.5)
			print(f"\nThe skeleton takes one swing and slices {name.title()}'s head in half.") 
			print(f"\n{name.title()}'s lifeless body drops to the floor as the skeleton smirks then walks away")
			time.sleep(2.5)
			print(f"\nYOU DIED")
			re_try1 = input("\nWould you like to re-try this room? (yes), (no): ")
			if re_try1 == 'yes':
				continue
			elif re_try1 == 'no':
				print("Thanks for playing.")
				break	




# Sword and shield works becuase you can block the spells.

def room_b():
	while True:
		print("\nYou have come across a sorcerer")
		room_b_weapon_choice = input("\nYou have a choice of three weapons: a(sword and shield), b(throwing star), c(axe): ")	
		if room_b_weapon_choice == "A".lower():
			print("\nSword and shield equipped")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print(f"\nWell done {name.title()} you have killed the sorcerer and passed room B")


		elif room_b_weapon_choice == "B".lower():
			print("\nThrowing star equipped")
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\nYOU DIED!!")
			re_try2 = input("Would you like to re-try this room? (yes), (no): ")
			if re_try2 == "yes":
				continue
			elif re_try2 == "no":
				print("Thanks for playing.")
				break

		elif room_b_weapon_choice == "C".lower():
			print("\nAxe equipped")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\n")
			time.sleep(2.5)
			print("\nYOU DIED!!")
			re_try3 = input("Would you like to re-try this room? (yes), (no): ")
			if re_try3 == "yes":
				continue
			if re_try3 == "no":
				print("Thanks for playing.")
				break		


name = input("Type in your username: ")

room_choice = input("Do you want to go into room A or B: ")

if room_choice == "A".lower():
	room_a()

elif room_choice == "B".lower():
	room_b()