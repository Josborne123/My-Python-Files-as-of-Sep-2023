word = str(input("Please enter a word to convert to pig latin: "))



while True:
    if (word[0] == "b" or word[0] == "c" or word[0] == "d" or word[0] == "e" or word[0] == "f" or word[0] == "g" or word[0] == "h" or word[0] == "j" or word[0] == "k" or word[0] == "l" or word[0] == "m" or word[0] == "bn" or 
        word[0] == "p" or word[0] == "q" or word[0] == "r" or word[0] == "s" or word[0] == "t" or word[0] == "v" or word[0] == "w" or word[0] == "x" or word[0] == "y" or word[0] == "z"):
        
        firstConstant = word[0]
        word += firstConstant
        word += "ay"
        word = word[1:]
        print(word)

    elif (word[0]) == "a" or (word[0]) == "e" or (word[0]) == "i" or (word[0]) == "o" or (word[0]) == "u":
        word += "way"
        print(word)

    again = str(input("Would you like to play again? (y or n) "))
    if again == "n".lower():
        break
    elif again == "y".lower():
        word = str(input("Please enter a word to convert to pig latin: "))
        continue
