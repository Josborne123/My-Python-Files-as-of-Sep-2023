import string
import random

longestword = [""]

S = 12
ran = ''.join(random.choices(string.ascii_uppercase, k = S))    


alphabet = 'abcdefghijklmnopqrstuvwxyz'


players = int(input("How many people are playing: "))
names = [""] * players
guess = [""] * players


#for index in range(players):
  
print("Lets play the game")

  
for index in range(players):
  names[index] = str(input("Please enter your name: "))

  print(names[index] + " turn")
  print("The anagram is " + ran)
  guess[index] = str(input("Enter your word: "))
    
  while len(guess[index]) >= 13 or len(guess[index]) <= 0:
    print("Error. Word length incorrect")
    guess[index] = str(input("Enter your word: "))


  longestword = max(guess, key=len)

print("")
print("Names \t Guess")
for index in range(players):
  print(names[index] + "\t" + guess[index])


print("Lets see who won")
print("")
print("The longest word is " + longestword)
#print( + " guessed this word")

  