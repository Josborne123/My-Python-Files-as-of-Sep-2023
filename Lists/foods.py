my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friends_foods)

print("\nThe first three items in my_foods are:")
print(my_foods[0:3])
# Alternativly you can do this:
for my_food in my_foods[0:3]:
	print(my_food)


other_friend = ['pizza', 'apple cake', 'steak', 'chicken', 'fish']
print("\nThree items in the middle of the list are:")
for other in other_friend[1:4]:
	print(other)

print("The last three items in the list are")
print(other_friend[2:])	