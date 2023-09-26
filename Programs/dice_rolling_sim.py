import random

while True:
    die_choice = random.randint(1,6)
    print(die_choice)
    again = str(input("Would you like to roll again? (y/n) "))
    if again == "y":
        continue
    elif again == "n":
        print("Thanks for using.")
        break    
