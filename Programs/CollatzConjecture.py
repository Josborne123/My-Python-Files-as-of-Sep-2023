import random

n = random.randint(1,100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
print("Starting number is " + str(n))
steps = 0

while n != 1:
    if n % 2 == 0:
        n = n / 2
        steps += 1
    else: 
        n = (n * 3) + 1
        steps += 1


        
print("It took " + str(steps) + " steps")
print("Proof: " "n = " + str(n))