#########
#Notes 
#Need to check the userInput for error
#Need to calcualte net WPM instead of gross WPM

import time
from random_word import RandomWords
import random
from essential_generators import DocumentGenerator
import string

r = RandomWords()
#r = r.get_random_words(hasDictionaryDef="true", minCorpusCount=1, maxCorpusCount=1, minDictionaryCount=1, maxDictionaryCount=5, minLength=5, maxLength=10, sortBy="alpha", sortOrder="asc", limit=10)

print("Here is your random sentence")
gen = DocumentGenerator()   
sentence = print(gen.sentence())
time.sleep(5)

#sentence = "The quick brown fox jumps over the lazy dog"

#print(sentence)


userInput = ""

print("Ready")
time.sleep(1)
print("Set")
time.sleep(1)
print("Go")


start = time.time()
userInput += input()
  
end = time.time()
timetook = end - start
timetook = timetook / 60
charactersTyped = len(userInput)

grossWPM = (charactersTyped / 5) / timetook
print(f"Gross WPM is {grossWPM}")









#time_configuration = int(input("Please enter your time configuration: 10, 15, 30, 60, 120 (s): "))

#start = time.time()

#while (time.time() - start) < time_configuration:
   # r = RandomWords()
    #r = r.get_random_word()
    #print(r)
    #time.sleep(0.2)
    




#end = time.time()

#timetook = end - start


